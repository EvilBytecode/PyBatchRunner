# main.py
# Rewritten clean version.
from module.advanced import advscript
from module.reg import hcku, hklm
from module.admin import check
from module.oneliner import runsingleline
from module.powershellrun import runpscommand

def main():
    print("\n1. Running single-line script:")
    singleline_put = runsingleline("echo Running a single-line script")
    print(singleline_put)

    print("\n2. Running PowerShell command:")
    powershell_put = runpscommand("Get-Process")
    print(powershell_put)


    print("\n3. Running advanced script:")
    put_advanced = advscript("""
        mkdir example_folder
        echo This is content for file1 > example_folder\\file1.txt
        echo Content for file2 > example_folder\\file2.txt
        echo Another file content > example_folder\\file3.txt
        dir example_folder
        echo Additional content >> example_folder\\file2.txt
    """)
    print(put_advanced)

    print("\n4. Modifying the registry (HKEY_CURRENT_USER):")
    hcku_put = hcku("ExampleKey", "Software\\MyApp", "NewValue")
    print(hcku_put)

    print("\n5. Modifying the registry (HKEY_LOCAL_MACHINE):")
    put_hklm = hklm("AnotherKey", "Software\\MyApp", "AnotherValue")
    print(put_hklm)

    print("\n6. Checking administrative permissions:")
    if check():
        print("Performing administrative operations...")
    else:
        print("Exiting because admin permissions are required.")

if __name__ == "__main__":
    main()
