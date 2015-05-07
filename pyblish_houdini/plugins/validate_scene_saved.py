import pyblish.api
import sys


@pyblish.api.log
class ValidateSceneSaved(pyblish.api.Validator):
    """Validates whether the scene is saved"""

    families = ['*']
    hosts = ['*']
    version = (0, 1, 0)

    host = sys.executable.lower()

    def process_context(self, context):
        if "nuke" in self.host:
            scene_modified = self.process_nuke()
        elif "maya" in self.host:
            scene_modified = self.process_houdini()
        elif "houdini" in self.host:
            scene_modified = self.process_houdini()
        else:
            scene_modified = True

        if scene_modified:
            raise pyblish.api.ValidationError('Scene has not been saved since modifying. '
                                              'You can fix it using the repair button '
                                              'or save it manually.')


    def repair_context(self, context):
        """Saves the script
        """
        if "nuke" in self.host:
            self.repair_nuke()
        elif "maya" in self.host:
            self.repair_maya()
        elif "houdini" in self.host:
            self.repair_houdini()


    # NUKE
    def process_nuke(self):
        import nuke
        return nuke.Root().modified()

    def repair_nuke(self):
        import nuke
        nuke.scriptSave()


    # MAYA
    def process_maya(self):
        import cmds
        return cmds.file(q=True, modified=True)

    def repair_maya(self):
        import cmds
        cmds.SaveScene()


    # HOUDINI
    def process_houdini(self):
        import hou
        return hou.hipFile.hasUnsavedChanges()

    def repair_houdini(self):
        import hou
        hou.hipFile.save()


