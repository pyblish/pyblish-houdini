import hou
import pyblish.api


@pyblish.api.log
class SelectMantraNodes(pyblish.api.Selector):
    """Selects all mantra nodes"""

    hosts = ['*']
    version = (0, 1, 0)

    def process_context(self, context):

        renderNode = hou.node( "/out" )
        render_nodes = renderNode.children()

        for node in list(render_nodes):

            if node.type().name() == 'ifd':
                instance = context.create_instance(name=node.name())
                instance.set_data('family', value='mantra')
                instance.set_data('output_path_expanded', value=node.parm('vm_picture').eval())
                instance.set_data('output_path', value=node.parm('vm_picture').unexpandedString())
                instance.add(node)
