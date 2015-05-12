import hou
import hdefereval
import threading

def houdini_command():
    hou.node('/obj').createNode('geo')

def worker():
    n = 0
    while n < 5:
        hdefereval.executeInMainThreadWithResult(houdini_command)
        n += 1

thread = threading.Thread(target=worker)
thread.daemon = True

thread.start()