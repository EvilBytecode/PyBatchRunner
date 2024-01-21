import subprocess

def check():
    try:
        subprocess.run(['fltmc'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Has admin permissions")
        return True
    except subprocess.CalledProcessError:
        print("Does NOT have admin permissions")
        return False
