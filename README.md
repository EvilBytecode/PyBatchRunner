
PyBatchRunner
=====================

This script demonstrates the usage of various modules for running different types of commands and scripts.

Modules Used
------------

### 1\. Single-Line Script Execution Module

**Usage:**

    from module.oneliner import runsingleline
    
    output_single_line = runsingleline("echo Running a single-line script")
    print(output_single_line)

### 2\. PowerShell Command Execution Module

**Usage:**

    from module.powershellrun import runpscommand
    
    output_powershell = runpscommand("Get-Process")
    print(output_powershell)

### 3\. Advanced Script Execution Module

**Usage:**

    from module.advanced import advscript
    
    output_advanced = advscript("""
        mkdir example_folder
        echo This is content for file1 > example_folder\\file1.txt
        echo Content for file2 > example_folder\\file2.txt
        echo Another file content > example_folder\\file3.txt
        dir example_folder
        echo Additional content >> example_folder\\file2.txt
    """)
    print(output_advanced)

### 4\. Registry Modification Module

**Usage:**

    from module.reg import hcku, hklm
    
    output_hcku = hcku("ExampleKey", "Software\\MyApp1", "NewValue")
    print(output_hcku)
    
    output_hklm = hklm("ExampleKey1", "Software\\MyApp1", "AnotherValue") ## will need uac if im right not sure rn
    print(output_hklm)

### 5\. Administrative Permission Check Module

**Usage:**

    from module.admin import check
    
    if check():
        print("Performing administrative operations...")
    else:
        print("Exiting because admin permissions are required.")

Script Execution
----------------

To execute the script, run the following command in your terminal:

    python main.py

This will run through various functionalities provided by the modules and showcase the output.


## Todo:
reg add
reg del
idk
