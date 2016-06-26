### ![](https://cloud.githubusercontent.com/assets/2152766/6998101/5c13946c-dbcd-11e4-968b-b357b7c60a06.png)

[![Build Status](https://travis-ci.org/pyblish/pyblish-houdini.svg?branch=master)](https://travis-ci.org/pyblish/pyblish-houdini)

Pyblish integration for SideFx Houdini 8-15.

<br>
<br>
<br>

### What is included?

A set of common plug-ins and functions shared across other integrations - such as getting the current working file. It also visually integrates Pyblish into the File-menu for easy access.

- Common [plug-ins](https://github.com/pyblish/pyblish-houdini/tree/master/pyblish_houdini/plugins)
- Common [functionality](https://github.com/pyblish/pyblish-houdini/blob/master/pyblish_houdini/__init__.py)
- File-menu shortcut

<br>
<br>
<br>

### Installation

pyblish-houdini depends on [pyblish-base](https://github.com/pyblish/pyblish-base) and is available via PyPI.

```bash
$ pip install pyblish-houdini
```

You may also want to consider a graphical user interface, such as [pyblish-qml](https://github.com/pyblish/pyblish-qml) or [pyblish-lite](https://github.com/pyblish/pyblish-lite).

<br>
<br>
<br>

### Usage

To get started using pyblish-houdini, run `setup()` at startup of your application.

```python
# 1. Register your favourite GUI
import pyblish.api
pyblish.api.register_gui("pyblish_lite")

# 2. Set-up Pyblish for Houdini
import pyblish_houdini
pyblish_houdini.setup()
```

<br>
<br>
<br>

### Persistence

In order to have Pyblish become a permanent member of each Houdini session, you can add the supplied `houdini_path/` folder to your `HOUDINI_PATH` environment variable.

Take care however, for this variable has an unexpected quirk on Windows platforms.

```bash
$ set "HOUDINI_PATH=&;C:\pythonpath\pyblish_houdini\houdini_path"
```

Note the `&` sign, and the fact that the entire expression is wrapped in quotation marks.

With this variable set, you should find a new File-menu item.

![image](https://cloud.githubusercontent.com/assets/2152766/16362652/866de682-3bac-11e6-818a-cc711e04a1af.png)

<br>
<br>
<br>


### Documentation

- [Under the hood](#under-the-hood)
- [Manually show GUI](#manually-show-gui)
- [Teardown pyblish-houdini](#teardown-pyblish-houdini)
- [No GUI](#no-gui)

<br>
<br>
<br>

##### Under the hood

The `setup()` command will:

1. Register Houdini related ["hosts"](http://api.pyblish.com/pages/Plugin.hosts.html), allowing plug-ins to be filtered accordingly.
3. Register a minimal set of plug-ins that are common across all integrations.

<br>
<br>
<br>

##### Manually show GUI

The menu-button is set to run `show()`, which you may also manually call yourself, such as from a shelf-button.

```python
import pyblish_houdini
pyblish_houdini.show()
```

<br>
<br>
<br>

##### Teardown pyblish-houdini

To get rid of the menu, and completely remove any trace of pyblish-houdini from your Houdini session, run `teardown()`.

```python
import pyblish_houdini
pyblish_houdini.teardown()
```

This will do the opposite of `setup()` and clean things up for you.

<br>
<br>
<br>

##### No GUI

In the event that no GUI is registered upon running `setup()`, the button will provide the *user* with this information on how they can get up and running on their own.

![image](https://cloud.githubusercontent.com/assets/2152766/16318872/d63b7f60-3988-11e6-9431-f64991aabef3.png)

![image](https://cloud.githubusercontent.com/assets/2152766/16318883/ddf159f0-3988-11e6-8ef5-af5fd8dde725.png)

![image](https://cloud.githubusercontent.com/assets/2152766/16318893/e7d4cc9a-3988-11e6-92e9-c16037e51fb7.png)
