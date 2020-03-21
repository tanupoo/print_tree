def print_tree(L, sorting=True, keys=("__id", "__children"),
               style=("> ", "+-", "+-", False)):
    """
    The input L must be a list of tree structures formed a top-down tree
    like below.  By default, '__id' is the identifier of the node.
    '__children' is the key containing its child nodes.  You can change
    the name of both keys by redefining the keys option:
    
        keys[0]: the key string of the node.
        keys[1]: the key string of the list of the children.

    Any other keys in L will be ignored.

    The example of L:

        L = [
            { "__id":"C", "__children": [
                { "__id":"B", "__children": [
                    { "__id":"G", "__children": [] },
                    { "__id":"D", "__children": [
                        { "__id":"H", "__children": [
                                { "__id":"I", "__children": [] }
                        ] },
                    ] },
                ] },
            ] },
            { "__id":"F", "__children": [
                { "__id":"A", "__children": [
                    { "___id":"J", "___children": [] },
                    { "__id":"E", "__children": [] },
                ] },
                { "__id":"K", "__children": [] },
            ] },
        ]

    The order of nodes doesn't matter.  These are alphabetically sorted
    by default.  You can stop it when you specify False to the sorting
    option.

    The style option is used to change the form of tree:

        style[0]: the string closest to each child node.
        style[1]: the rest of the string in the normal child node.
        style[2]: the rest of the string in the last child node.
        style[3]: whether to add a line specing.

    The default value of the style option is ("> ", "+-", "+-", False),
    which results like below:

        +-> C
        |   +-> B
        |       +-> D
        |       |   +-> H
        |       |       +-> I
        |       +-> G
        +-> F
            +-> A
            |   +-> E
            |   +-> J
            +-> K

    For example, The possible styles would be:

        ("> ", "+-", "'-", False)
        (" ", "+-", "'-", False)
        (" ", "+-", "+-", False)

    """
    def sort_tree(xlist, key_node_id, key_children):
        for x in xlist:
            if x.get(key_children):
                x[key_children] = sort_tree(x[key_children],
                                            key_node_id, key_children)
        return sorted(xlist, key=lambda x:(x[key_node_id]))

    def walk_tree(xlist, header, keys, style):
        (key_node_id, key_children) = keys
        (HDR1, HDR_NRM, HDR_END, add_line) = style
        padlen = len(HDR_NRM + HDR1)
        n = 0
        for x in xlist:
            n += 1
            #
            if add_line:
                print(header + "|")
            #
            if n == len(xlist):
                print(header + HDR_END + HDR1 + x[key_node_id])
            else:
                print(header + HDR_NRM + HDR1 + x[key_node_id])
            #
            c = x.get(key_children)
            if c:
                if n == len(xlist):
                    walk_tree(c, header + " ".ljust(padlen), keys, style)
                else:
                    walk_tree(c, header + "|".ljust(padlen), keys, style)

    if sorting:
        L = sort_tree(L, keys[0], keys[1])
    walk_tree(L, "", keys, style)

if __name__ == "__main__":
    from sys import argv
    L = [
        { "ID":"C", "NODES": [
            { "ID":"B", "NODES": [
                { "ID":"G", "NODES": [] },
                { "ID":"D", "NODES": [
                    { "ID":"H", "NODES": [
                            { "ID":"I", "NODES": [] }
                    ] },
                ] },
            ] },
        ] },
        { "ID":"F", "NODES": [
            { "ID":"A", "NODES": [
                { "ID":"J", "NODES": [] },
                { "ID":"E", "NODES": [] },
            ] },
            { "ID":"K", "NODES": [] },
        ] },
    ]
    #
    keys = ("ID", "NODES")
    style = [
        ("> ", "+-", "+-", False),
        ("> ", "+-", "'-", False),
        (" ", "+-", "+-", False),
        (" ", "+-", "'-", False),
    ]
    # % python print_tree.py 0
    # +-> C
    # |   +-> B
    # |       +-> D
    # |       |   +-> H
    # |       |       +-> I
    # |       +-> G
    # +-> F
    #     +-> A
    #     |   +-> E
    #     |   +-> J
    #     +-> K
    # % python print_tree.py 1
    # +-> C
    # |   '-> B
    # |       +-> D
    # |       |   '-> H
    # |       |       '-> I
    # |       '-> G
    # '-> F
    #     +-> A
    #     |   +-> E
    #     |   '-> J
    #     '-> K
    # % python print_tree.py 2
    # +- C
    # |  +- B
    # |     +- D
    # |     |  +- H
    # |     |     +- I
    # |     +- G
    # +- F
    #    +- A
    #    |  +- E
    #    |  +- J
    #    +- K
    # % python print_tree.py 3
    # +- C
    # |  '- B
    # |     +- D
    # |     |  '- H
    # |     |     '- I
    # |     '- G
    # '- F
    #    +- A
    #    |  +- E
    #    |  '- J
    #    '- K
    style_index = 0
    if len(argv) == 2:
        style_index = int(argv[1])
    print_tree(L, keys=keys, style=style[style_index])
