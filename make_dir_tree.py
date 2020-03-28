#!/usr/bin/env python

from os import scandir, path

def make_dir_tree(top_dir, show_hidden_file=False):
    # assuming top_dir is a directory.
    L = []
    dir_attr = { "__id":path.basename(top_dir), "__children":[] }
    with scandir(top_dir) as fd:
        for entry in fd:
            if show_hidden_file and len(entry.name) > 1 and entry.name.startswith("."):
                continue
            if entry.is_dir():
                dir_attr["__children"].extend(make_dir_tree(entry.path))
            else:
                dir_attr["__children"].append({"__id":entry.name})
        L.append(dir_attr)
    return L

if __name__ == "__main__":
    from print_tree import print_tree
    from sys import argv
    from argparse import ArgumentParser
    from argparse import ArgumentDefaultsHelpFormatter
    ap = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    ap.add_argument("dir", nargs="*", help="1st item.")
    ap.add_argument("-a", action="store_true", dest="show_hidden_file",
                    help="show hidden files.")
    opt = ap.parse_args()
    if len(opt.dir) == 0:
        top_dir = ["."]
    else:
        top_dir = opt.dir
    try:
        for d in top_dir:
            L = make_dir_tree(d)
            print_tree(L, style=[" ", "|--", "'--", False])
    except NotADirectoryError as e:
        print(f"ERROR: {top_dir} is not a directory.")
        exit(0)
