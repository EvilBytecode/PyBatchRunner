# folder/batch2pymodule.py

import subprocess
import tempfile
import os

class BatchFile:
    def __init__(self):
        self.batch_script = "@echo off\n"


    def input(self, command):
        self.batch_script += command + "\n"

    def run(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.bat') as temp_file:
            temp_file.write(self.batch_script)

        try:
            result = subprocess.run(temp_file.name, capture_output=True, text=True, shell=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e}\nOutput: {e.output}\nCommand: {e.cmd}"
        finally:
            os.remove(temp_file.name)
