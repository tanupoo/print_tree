def make_from_bottom_up_tree(L, keys=("__id", "__parent")):
    """
    convert into a top-down tree from a bottom up tree.
    """
    def suspend(obj, xlist, keys):
        (key_node_id, key_parent) = keys
        for x in xlist:
            if obj[key_parent] == x[key_node_id]:
                x.setdefault("__children", []).append(obj)
                return True
            elif x.get("__children"):
                if suspend(obj, x.get("__children"), keys):
                    return True

    (key_node_id, key_parent) = keys
    for i in range(len(L)):
        x = L.pop(0)
        if x[key_parent]:
            suspend(x, L, keys)
        else:
            L.append(x)

if __name__ == "__main__":
    from print_tree import print_tree
    from random import shuffle
    L = [
        { "ID":"H", "PID":"D" },
        { "ID":"A", "PID":"F" },
        { "ID":"C", "PID":None },
        { "ID":"G", "PID":"B" },
        { "ID":"J", "PID":"A" },
        { "ID":"I", "PID":"H" },
        { "ID":"B", "PID":"C" },
        { "ID":"E", "PID":"A" },
        { "ID":"F", "PID":None },
        { "ID":"K", "PID":"F" },
        { "ID":"D", "PID":"B" },
    ]
    shuffle(L)
    make_from_bottom_up_tree(L, keys=("ID", "PID"))
    #
    print_tree(L, keys=("ID", "__children"))
