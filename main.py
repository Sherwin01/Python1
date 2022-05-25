import os
if os.path.exists("python_files.txt"):
    os.remove("python_files.txt")
else:
    print("File not exist")
