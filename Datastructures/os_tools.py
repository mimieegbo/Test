import shutil
import os


# exception handler
def handler(func, path, exc_info):
    print("Inside handler")
    print(exc_info)


# location
location = "D:/Pycharm projects/GeeksforGeeks/"

# directory
dir = "Authors"

# path
path = os.path.join(location, dir)

# removing directory
shutil.rmtree(path, onerror=handler)