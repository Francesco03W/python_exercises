import os
import hashlib
import collections


def is_image(path,extensions):
    """
    Check whether the path ends with one of the extensions
    
    path: string file path
    extensions: list of extensions
    """
    if isinstance(path,str):
        if isinstance(extensions,list):
            if len(extensions) != 0:
                #se i parametri sono corretti
                #per ricavare l'ultimo segmento del percorso, non possiamo fare assegnazioni di str.split a tupla (non noto numero di elementi) -> lista
                segments=path.split("/")
                file=segments[len(segments)-1]
                #per endswith devo usare tupla
                extensions_tuple=tuple(extensions)
                #ammette anche il caso di lista vuota con 1 elemento
                # ovvero tutte le estensioni sono valide
                if file.endswith(extensions_tuple):
                    return True
            else:
                 print("Empty list error")
        else:
            print("List argument error")
    else:
        print("Path argument error")
    
    return False

def add_path(path, d):
    """
    Compute the digest of path, add the digest to d as key and append path to a list as value

    path : path to a file
    d : defaultdict of lists

    >>> add_path('photos/feb-2023/photo1.jpg', collections.defaultdict(list))
    defaultdict(<class 'list'>, {'dace5bcdd614b5a23e465b1edc406bc3': ['photos/feb-2023/photo1.jpg']})
    """
    data=open(path,"rb").read()
    md5_hash=hashlib.md5()
    md5_hash.update(data)
    d[md5_hash.hexdigest()].append(path)

# domanda: perché istanziare oggetto hashlib.md5 qui non fa funzionare il
# programma? Sarà perché istanze contemporanee sono con salt diversi?
def walk_images(dirname, d):
    """
    Walk the directory tree and return a defaultdict of lists where
    - the key is the digest of the image
    - the value is a list of paths to the images with the same digest

    dirname : path to a directory
    d : defaultdict of lists
    """
    #listdir senza argomenti prende la $PWD del file .py!!!
    ls=os.listdir(dirname)
    #md5_hash=hashlib.md5()
    for p in ls:
        p_path=dirname+'/'+p
        if os.path.isfile(p_path):
            if is_image(p_path,['.jpg','.jpeg']):
                add_path(p_path,d)
        else:
            if os.path.isdir(p_path):
                walk_images(p_path,d)

def main():
    d = collections.defaultdict(list)
    walk_images(".", d)
    for digest, paths in d.items():
        if len(paths) > 1:
            for path in paths:
                print(path)

if __name__ == "__main__":
    main()
