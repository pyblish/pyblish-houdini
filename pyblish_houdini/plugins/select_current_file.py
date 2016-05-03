import pyblish.api

import hou


class SelectCurrentFile(pyblish.api.ContextPlugin):
    """Inject the current working file into context

    .. note:: This plug-in is implemented in all relevant host integrations

    """

    label = "Current Scene File"
    hosts = ['houdini']
    version = (0, 1, 0)

    def process(self, context):
        """inject the current working file"""
        current_file = hou.hipFile.path()
        context.data['currentFile'] = current_file
