import os

def search(filename,dirpath=None):
    if not dirpath:
        dirpath=os.path.abspath('.')
        
    L=[]
    for x in [x for x in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath,x))]:        
        if filename in x:
            L.append(os.path.relpath(x))
    for x in [x for x in os.listdir(dirpath) if os.path.isdir(os.path.join(dirpath,x))]:
        sub_dir_files=search(filename,os.path.join(dirpath,x))
        for file in sub_dir_files:
            L.append(file)
    return L
            
if __name__=='__main__':
    print(search('py','..'))