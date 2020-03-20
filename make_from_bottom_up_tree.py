def make_from_bottom_up_tree(L):
    def suspend(obj, xlist):
        for x in xlist:
            if obj["PID"] == x["_id"]:
                x.setdefault("_child", []).append(obj)
                return True
            elif x.get("_child"):
                if suspend(obj, x.get("_child")):
                    return True

    for i in range(len(L)):
        x = L.pop(0)
        if x["PID"]:
            suspend(x, L)
        else:
            L.append(x)

if __name__ == "__main__":
    from print_tree import print_tree
    from random import shuffle
    from sys import argv
    L = [
        { "_id":"H", "PID":"D" },
        { "_id":"A", "PID":"F" },
        { "_id":"C", "PID":None },
        { "_id":"G", "PID":"B" },
        { "_id":"J", "PID":"A" },
        { "_id":"I", "PID":"H" },
        { "_id":"B", "PID":"C" },
        { "_id":"E", "PID":"A" },
        { "_id":"F", "PID":None },
        { "_id":"K", "PID":"F" },
        { "_id":"D", "PID":"B" },
    ]
    shuffle(L)
    make_from_bottom_up_tree(L)
    #
    style_index = 0
    if len(argv) == 2:
        style_index = int(argv[1])
    print_tree(L)
