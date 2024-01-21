# module/reg.py

from .PyBatchRunner import BatchFile

def hcku(key, path, value):
    return modify_registry("HKEY_CURRENT_USER", key, path, value)

def hklm(key, path, value):
    return modify_registry("HKEY_LOCAL_MACHINE", key, path, value)

def modify_registry(root, key, path, value):
    file = BatchFile()
    file.input(f"""
        @echo off
        echo Modifying the {root} registry...
        REG ADD "{root}\\{path}" /v {key} /d {value} /f
    """)
    return file.run()
