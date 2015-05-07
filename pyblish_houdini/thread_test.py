
import hou
import time
import hdefereval

import threading
import hou


def houdini_command():
    hou.node('/obj').createNode('geo')


def worker():
    internal_start  = time.time()
    n = 0
    while n < 5:
        hdefereval.executeInMainThreadWithResult(houdini_command)
        n += 1
    internal_end = time.time()
    print("Time taken to process all commands: %s" % str(internal_end - internal_start))

thread = threading.Thread(target=worker)
thread.daemon = True

start = time.time()
thread.start()
end = time.time()