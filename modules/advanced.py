# module/advanced.py

from .PyBatchRunner import BatchFile

def advscript(script):
    file = BatchFile()
    file.input(script)
    return file.run()
