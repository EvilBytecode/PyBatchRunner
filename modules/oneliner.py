# module/basicscript.py

from .PyBatchRunner import BatchFile

def runsingleline(script):
    file = BatchFile()
    file.input(script)
    return file.run()
