import os

# Your path of root directory
PATH = '/home/baoanh/Desktop/Python/ThinkPython'

def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def get_filelist(path):
    dirlist = get_dirlist(path)

    filelist = []
    for f in dirlist:
        fullname = os.path.join(path, f)    # Turn name into full pathname
        if os.path.isdir(fullname):
            filelist.extend(get_filelist(fullname))
        else:
            filelist.append(fullname)
    return filelist

def clean_trash(path):
    fileList = get_filelist(path)
    removeList = [f for f in fileList if 'trash.txt' in f]
    for f in removeList:
        os.remove(f)

clean_trash(PATH)
