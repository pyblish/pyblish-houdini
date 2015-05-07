import pyblish.api
import os
import sys
import pprint

@pyblish.api.log
class SelectWorkfile(pyblish.api.Selector):
    """Selects current workfile"""

    hosts = ['*']
    version = (0, 1, 0)

    host = sys.executable.lower()

    def process_context(self, context):
        if "nuke" in self.host:
            current_file = self.process_nuke()
        elif "maya" in self.host:
            current_file = self.process_houdini()
        elif "houdini" in self.host:
            current_file = self.process_houdini()
        else:
            current_file = None
            self.log.warning('Workfile selection in current host is not supported yet!')

        # Normalise the path
        normalised = os.path.normpath(current_file)

        directory, filename = os.path.split(normalised)
        if current_file:
            context.set_data('current_file', value=normalised)
            instance = context.create_instance(name=filename)
            instance.set_data('family', value='workFile')
            # instance.set_data("publish", False)
            instance.set_data("path", value=normalised)
            instance.add(normalised)


    # NUKE
    def process_nuke(self):
        import nuke
        return nuke.root().name()

    # MAYA
    def process_maya(self):
        import cmds
        return cmds.file(q=True, location=True)

    # HOUDINI
    def process_houdini(self):
        import hou
        return hou.hipFile.path()
