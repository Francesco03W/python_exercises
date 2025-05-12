import os
import collections
import hashlib

def md5_digest(path):
    data=open(path,"rb").read()
    hasher=hashlib.md5()
    hasher.update(data)
    return hasher.hexdigest()

# il controllo se il percorso è file o cartella è eseguito dalla funzione walk
def is_image(path, extensions):

    """
    Check whether the path ends with one of the extensions
    
    path: string file path
    extensions: list of extensions
    
    >>> is_image('photo.jpg', ['jpg', 'jpeg'])
    True
    >>> is_image('PHOTO.JPG', ['jpg', 'jpeg'])
    True
    >>> is_image('notes.txt', ['jpg', 'jpeg'])
    False
    """
    if path.lower().endswith(tuple(extensions)):
        return True
    return False

def add_path(path, d):
    """
    Compute the digest of path, add the digest to d as key and append path to a list as value

    path : path to a file
    d : defaultdict of lists

    >>> add_path('data/photos/feb-2023/photo1.jpg', collections.defaultdict(list))
    defaultdict(<class 'list'>, {'dace5bcdd614b5a23e465b1edc406bc3': ['data/photos/feb-2023/photo1.jpg']})
    """
    digest=md5_digest(path)
    # se digest è già una chiave, appendi il percorso alla lista (valore), altrimenti creala, (appende a lista vuota)
    d[digest].append(path)
    return d

def walk_images(dirname, d) :
    """
    Walk the directory tree and return a defaultdict of lists where
    - the key is the digest of the image
    - the value is a list of paths to the images with the same digest

    dirname : path to a directory
    d : defaultdict of lists
    """
    for element in os.listdir(dirname):
        element_path = os.path.join(dirname,element)
        if os.path.isfile(element_path):
            if is_image(element_path,['jpg','jpeg']):
                add_path(element_path,d)
        else:
            if os.path.isdir(element_path):
                walk_images(element_path,d)


def main():
    d = collections.defaultdict(list)
    walk_images(".", d)
    for digest, paths in d.items():
        if len(paths) > 1:
            for path in paths:
                print(path)

if __name__ == "__main__":
    main()
