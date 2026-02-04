import os
import shutil
import hashlib

def ValidateDirectory(dirname):
    if os.path.exists(dirname)==False:
        print("Directory does not exist")
        return

    if os.path.isdir(dirname)==False:
        print("Given path is not a directory")
        return


def GetFilesByExtension(dirname, ext):
    files = []

    for fname in os.listdir(dirname):
        if fname.endswith(ext):
            files.append(fname)

    return files


def RenameFiles(dirname, oldext, newext):
    renamedFiles=[]

    for fname in os.listdir(dirname):

        if fname.endswith(oldext):

            oldpath = os.path.join(dirname, fname)

            newname = fname.replace(oldext, newext)
            newpath = os.path.join(dirname, newname)

            os.rename(oldpath, newpath)
            renamedFiles.append(newname)

    return renamedFiles



def CreateDestinationDirectory(dest):
    if os.path.exists(dest)==False:
        os.mkdir(dest)


def CopyAllFiles(src, dest,ext):
    copied_files = []

    for fname in os.listdir(src):

        src_path = os.path.join(src, fname)

        if(os.path.isfile(src_path))and(src_path.endswith(ext)):

            dest_path = os.path.join(dest, fname)
            shutil.copy2(src_path, dest_path)
            copied_files.append(fname)

    return copied_files


def CalculateChecksum(filepath):
    hashobj = hashlib.md5()

    fobj=open(filepath, "rb")
    while True:
        data = fobj.read(1024)
        if not data:
            break
        hashobj.update(data)

    return hashobj.hexdigest()


def GetAllChecksums(dirname):
    result = {}

    for fname in os.listdir(dirname):
        path = os.path.join(dirname, fname)

        if os.path.isfile(path):
            result[fname] = CalculateChecksum(path)

    return result


def FileChecksum(path):
    hashobj = hashlib.md5()

    with open(path, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            hashobj.update(data)

    return hashobj.hexdigest()


def FindDuplicates(dirname):
    checksum_map = {}
    duplicates = []

    for fname in os.listdir(dirname):
        path = os.path.join(dirname, fname)

        if os.path.isfile(path):
            chksum = FileChecksum(path)

            if chksum in checksum_map:
                duplicates.append(fname)
            else:
                checksum_map[chksum] = fname

    return duplicates


def RemoveDuplicates(dirname):
    checksum_map = {}
    removed_files = []

    for fname in os.listdir(dirname):
        path = os.path.join(dirname, fname)

        if os.path.isfile(path):

            chksum = FileChecksum(path)

            if chksum in checksum_map:
                os.remove(path)
                removed_files.append(fname)
            else:
                checksum_map[chksum] = fname

    return removed_files