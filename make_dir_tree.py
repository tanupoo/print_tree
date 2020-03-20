from os import scandir, path

def make_dir_tree(top_dir):
    # assuming top_dir is a directory.
    L = []
    dir_attr = { "_id":path.basename(top_dir), "_child":[] }
    with scandir(top_dir) as fd:
        for entry in fd:
            if entry.is_dir():
                dir_attr["_child"].extend(make_dir_tree(entry.path))
            else:
                dir_attr["_child"].append({"_id":entry.name})
        L.append(dir_attr)
    return L

if __name__ == "__main__":
    from print_tree import print_tree
    from sys import argv
    if len(argv) == 1:
        top_dir = "."
    else:
        top_dir = argv[1]
    L = make_dir_tree(top_dir)
    print_tree(L, style=[" ", "+-", "'-", False])
