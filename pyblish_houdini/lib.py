"""Internal library for Pyblish Houdini

Attributes:
    cached_process: Temporarily stored Popen instance of Pyblish QML
    CREATE_NO_WINDOW: Flag from MSDN; see link below.
    PYBLISH_QML_CONSOLE: Environment variable for displaying
        the console upon launching Pyblish QML

"""

# Standard library
import os
import sys
import random
import inspect
import traceback
import subprocess
import contextlib

# Pyblish libraries
import pyblish.api

# Host libraries
import hou

# Local libraries
import plugins

cached_process = None

# https://msdn.microsoft.com/en-us/library/ms684863(v=VS.85).aspx
CREATE_NO_WINDOW = 0x08000000
PYBLISH_QML_CONSOLE = "PYBLISH_QML_CONSOLE"


def echo(text):
    print text


def show(console=False, prefer_cached=True):
    """Show the Pyblish graphical user interface

    An interface may already have been loaded; if that's the
    case, we favour it to launching a new unless `prefer_cached`
    is False.

    """

    global cached_process

    if cached_process and prefer_cached:
        still_running = cached_process.poll() is None
        if still_running:
            return _show_cached()
        else:
            cached_process = None
    return _show_new(console)


def _show_cached():
    """Display cached gui

    A GUI is cached upon first being shown, or when pre-loaded.

    """

    import pyblish_endpoint.client

    pyblish_endpoint.client.emit("show")

    return cached_process


def _show_new(console=False):
    """Create and display a new instance of the Pyblish QML GUI"""
    try:
        port = os.environ["ENDPOINT_PORT"]
    except KeyError:
        raise ValueError("Pyblish start-up script doesn't seem to "
                         "have been run, could not find the PORT variable")

    pid = os.getpid()
    kwargs = dict(args=["python", "-m", "pyblish_qml",
                        "--port", port, "--pid", str(pid)])

    if not console and os.name == "nt":
        if not os.environ.get(PYBLISH_QML_CONSOLE):
            kwargs["creationflags"] = CREATE_NO_WINDOW

    echo("Creating a new instance of Pyblish QML")
    proc = subprocess.Popen(**kwargs)

    global cached_process
    cached_process = proc

    return proc


def setup(preload=True, console=False):
    """Setup integration

    Registers Pyblish for Maya plug-ins and appends an item to the File-menu

    Attributes:
        preload (bool): Preload the current GUI
        console (bool): Display console with GUI

    """

    if console:
        os.environ[PYBLISH_QML_CONSOLE] = "1"

    register_plugins()

    try:
        port = setup_endpoint()

        if preload:
            pid = os.getpid()
            preload_(port, pid)

    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        message = "".join(traceback.format_exception(
            exc_type, exc_value, exc_traceback))
        echo(message)
        echo("pyblish: Running headless")

    echo("pyblish: Integration loaded..")


def preload_(port, pid=None):
    pid = os.getpid()

    kwargs = dict(args=["python", "-m", "pyblish_qml",
                        "--port", str(port), "--pid", str(pid),
                        "--preload"])

    if os.name == "nt":
        if not os.environ.get(PYBLISH_QML_CONSOLE):
            kwargs["creationflags"] = CREATE_NO_WINDOW

    proc = subprocess.Popen(**kwargs)

    global cached_process
    cached_process = proc

    return proc


def setup_endpoint():
    """Start Endpoint

    Raises:
        ImportError: If Pyblish Endpoint is not available

    """


    from service import HoudiniService
    from pyblish_endpoint import server

    port = find_next_port()
    server.start_async_production_server(service=HoudiniService, port=port)
    os.environ["ENDPOINT_PORT"] = str(port)

    echo("pyblish: Endpoint running @ %i" % port)

    return port


def register_plugins():
    # Register accompanying plugins
    plugin_path = os.path.dirname(plugins.__file__)
    pyblish.api.register_plugin_path(plugin_path)
    echo("pyblish: Registered %s" % plugin_path)



def find_next_port():
    return random.randint(6000, 7000)


def filemenu_publish():
    """Add Pyblish to file-menu"""

    try:
        import pyblish_houdini.lib
        pyblish_houdini.lib.show()
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        message = "".join(traceback.format_exception(
            exc_type, exc_value, exc_traceback))

        sys.stderr.write("Tried launching GUI, but failed.\n")
        sys.stderr.write("Message was: %s\n" % message)
        sys.stderr.write("Publishing in headless mode instead.\n")

        import pyblish.util
        pyblish.util.publish()


@contextlib.contextmanager
def maintained_selection():
    """Maintain selection during context

    Example:
        >>> with maintained_selection():
        ...     # Modify selection
        ...     node.setSelected(on=False, clear_all_selected=True)
        >>> # Selection restored

    """

    previous_selection = hou.selectedNodes()
    try:
        yield
    finally:
        if previous_selection:
            for node in previous_selection:
                node.setSelected(on=True)
        else:
            for node in previous_selection:
                node.setSelected(on=False)
