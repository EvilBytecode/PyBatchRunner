from .PyBatchRunner import BatchFile

def runpscommand(command):
    file = BatchFile()
    file.input(f"""
        @echo off
        powershell -Command "{command}"
    """)
    return file.run()