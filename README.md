print_tree
==========

A command line tool and python functions to print a linked list
for a dum terminal.

- print_tree.py: the main function to print a linked list that is structed
  by a top-down tree.
- make_from_bottom_up_tree.py: a function to convert from a bottom-up tree.
- make_dir_tree.py: a function to make a top-down tree of a directory.
- 
## Sample

You can see below results by executing print_tree.py with a number from 0 to 3.

```
% python print_tree.py 0
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

% python print_tree.py 1
+-> C
|   '-> B
|       +-> D
|       |   '-> H
|       |       '-> I
|       '-> G
'-> F
    +-> A
    |   +-> E
    |   '-> J
    '-> K

% python print_tree.py 2
+- C
|  +- B
|     +- D
|     |  +- H
|     |     +- I
|     +- G
+- F
   +- A
   |  +- E
   |  +- J
   +- K

% python print_tree.py 3
+- C
|  '- B
|     +- D
|     |  '- H
|     |     '- I
|     '- G
'- F
   +- A
   |  +- E
   |  '- J
   '- K
```

## Usage

*COPIED FROM help(print_tree)*

```
print_tree(L, sorting=True, style=['> ', '+-', '+-', False])
```

The input L must be a linked list structure formed a top-down tree
like below.  '_id' is the name of the node.  '_child' contains its
child nodes.  Any other keys will be ignored.

The example of L:

```
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
```

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

```
["> ", "+-", "'-", False]
[" ", "+-", "+-", False]
[" ", "+-", "'-", False]
```

