import os

def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

# Using the idea of flatten list exercise 
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

def print_files(path):
    """ Print listing of files """
    filelist = get_filelist(path)
    for f in filelist:
        print(f)

print_files('/home/baoanh/Desktop/Python/ThinkPython')
