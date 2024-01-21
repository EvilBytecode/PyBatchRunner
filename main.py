# main.py
# Rewritten clean version.
from module.advanced import advscript
from module.reg import hcku, hklm
from module.admin import check
from module.oneliner import runsingleline
from module.powershellrun import runpscommand

def main():
    print("\n1. Running single-line script:")
    output_single_line = runsingleline("echo Running a single-line script")
    print(output_single_line)

    print("\n2. Running PowerShell command:")
    output_powershell = runpscommand("Get-Process")
    print(output_powershell)


    print("\n3. Running advanced script:")
    output_advanced = advscript("""
        mkdir example_folder
        echo This is content for file1 > example_folder\\file1.txt
        echo Content for file2 > example_folder\\file2.txt
        echo Another file content > example_folder\\file3.txt
        dir example_folder
        echo Additional content >> example_folder\\file2.txt
    """)
    print(output_advanced)

    print("\n4. Modifying the registry (HKEY_CURRENT_USER):")
    output_hcku = hcku("ExampleKey", "Software\\MyApp", "NewValue")
    print(output_hcku)

    print("\n5. Modifying the registry (HKEY_LOCAL_MACHINE):")
    output_hklm = hklm("AnotherKey", "Software\\MyApp", "AnotherValue")
    print(output_hklm)

    print("\n6. Checking administrative permissions:")
    if check():
        print("Performing administrative operations...")
    else:
        print("Exiting because admin permissions are required.")

if __name__ == "__main__":
    main()
