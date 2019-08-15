import os

# Your path or root 
PATH = '/home/baoanh/Desktop/Python/ThinkPython'

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

def extract_dir(file_path):
    split = file_path.split('/')
    new_split = split[:-1]
    new_path = '/'.join(new_split)
    return new_path

def get_dir_recursive(path):
    filelist = get_filelist(path)
    result = [extract_dir(f) for f in filelist]
    result = list(set(result))
    result.sort()
    return result

def make_trash_files(root):
    """ Create empty trash.txt file in each subdirectory of root directory"""
    dirlist = get_dir_recursive(root)
    for dir in dirlist:
        os.chdir(dir)
        f = open('trash.txt', 'w')
        f.close()

make_trash_files(PATH)
