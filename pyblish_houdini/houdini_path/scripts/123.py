try:
    __import__("pyblish_houdini")

except ImportError as e:
    print "pyblish: Could not load integration: %s" % e

else:
    from pyblish_win import util
    util.augment_pythonpath()
    util.augment_path()
    import pyblish_houdini
    pyblish_houdini.setup()
