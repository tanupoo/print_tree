def __walk_tree(xlist, header, style):
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
            print(header + HDR_END + HDR1 + x["_id"])
        else:
            print(header + HDR_NRM + HDR1 + x["_id"])
        #
        c = x.get("_child")
        if c:
            if n == len(xlist):
                __walk_tree(c, header + " ".ljust(padlen), style)
            else:
                __walk_tree(c, header + "|".ljust(padlen), style)

def __sort_tree(xlist):
    for x in xlist:
        if x.get("_child"):
            x["_child"] = __sort_tree(x["_child"])
    return sorted(xlist, key=lambda x:(x["_id"]))

def print_tree(L, sorting=True, style=["> ", "+-", "+-", False]):
    """
    The input L must be a linked list structure formed a top-down tree
    like below.  '_id' is the name of the node.  '_child' contains its
    child nodes.  Any other keys will be ignored.

    The example of L:

        L = [
            { "_id":"C", "_child": [
                { "_id":"B", "_child": [
                    { "_id":"G", "_child": [] },
                    { "_id":"D", "_child": [
                        { "_id":"H", "_child": [
                                { "_id":"I", "_child": [] }
                        ] },
                    ] },
                ] },
            ] },
            { "_id":"F", "_child": [
                { "_id":"A", "_child": [
                    { "_id":"J", "_child": [] },
                    { "_id":"E", "_child": [] },
                ] },
                { "_id":"K", "_child": [] },
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

    The default value of the style option is ["> ", "+-", "+-", False],
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

        ["> ", "+-", "'-", False]
        [" ", "+-", "+-", False]
        [" ", "+-", "'-", False]

    """
    if sorting:
        L = __sort_tree(L)
    __walk_tree(L, "", style)

if __name__ == "__main__":
    from sys import argv
    L = [
        { "_id":"C", "_child": [
            { "_id":"B", "_child": [
                { "_id":"G", "_child": [] },
                { "_id":"D", "_child": [
                    { "_id":"H", "_child": [
                            { "_id":"I", "_child": [] }
                    ] },
                ] },
            ] },
        ] },
        { "_id":"F", "_child": [
            { "_id":"A", "_child": [
                { "_id":"J", "_child": [] },
                { "_id":"E", "_child": [] },
            ] },
            { "_id":"K", "_child": [] },
        ] },
    ]
    _style = [
        ["> ", "+-", "+-", False],
        ["> ", "+-", "'-", False],
        [" ", "+-", "+-", False],
        [" ", "+-", "'-", False],
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
    print_tree(L, sorting=True, style=_style[style_index])
