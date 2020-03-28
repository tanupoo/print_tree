#!/usr/bin/env python

from os import scandir, path

def make_dir_tree(top_dir):
    # assuming top_dir is a directory.
    L = []
    dir_attr = { "__id":path.basename(top_dir), "__children":[] }
    with scandir(top_dir) as fd:
        for entry in fd:
            if entry.is_dir():
                dir_attr["__children"].extend(make_dir_tree(entry.path))
            else:
                dir_attr["__children"].append({"__id":entry.name})
        L.append(dir_attr)
    return L

if __name__ == "__main__":
    from print_tree import print_tree
    from sys import argv
    if len(argv) == 1:
        top_dir = "."
    else:
        top_dir = argv[1]
    try:
        L = make_dir_tree(top_dir)
    except NotADirectoryError as e:
        print(f"ERROR: {top_dir} is not a directory.")
        exit(0)
    print_tree(L, style=[" ", "+-", "'-", False])
