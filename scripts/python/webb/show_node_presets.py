import hou
import subprocess,os


def get_node_preset(node):
    prefPath = os.path.normpath(hou.getenv("HOUDINI_USER_PREF_DIR"))
    node_path =  node.type().definition().libraryFilePath()
    base = os.path.basename(node_path)
    # .hda -> .idx
    base = os.path.splitext(base)[0]
    base += ".idx"
    node_type = node.type()
    node_type_name = node_type.category().name()

    preset_path = os.path.normpath(os.path.join(prefPath, os.path.normpath(f"presets/{node_type_name}"), base))
    if not os.path.exists(preset_path):
        raise hou.NodeError("File {} does not exist".format(preset_path))
    else:
        subprocess.Popen(f'explorer /select, {os.path.realpath(preset_path)}')

def main(kwargs):
    node = kwargs["node"]
    get_node_preset(node)
