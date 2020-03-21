print_tree
==========

A command line tool and python functions to print a linked list
for a dum terminal.

- print_tree.py: the main function to print a linked list that is structed
  by a top-down tree.
- make_from_bottom_up_tree.py: a function to convert from a bottom-up tree into   a top-down tree.
- make_dir_tree.py: a function to make a top-down tree of a directory.

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
print_tree(L, sorting=True, keys=('__id', '__children'),
           style=('> ', '+-', '+-', False))
```

The input L must be a list of tree structures formed a top-down tree
like below.  By default, '__id' is the identifier of the node.
'__children' is the key containing its child nodes.  You can change
the name of both keys by redefining the keys option:

```
keys[0]: the key string of the node.
keys[1]: the key string of the list of the children.
```

Any other keys in L will be ignored.

The example of L:

```
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
```

The order of nodes doesn't matter.  These are alphabetically sorted
by default.  You can stop it when you specify False to the sorting
option.

The style option is used to change the form of tree:

```
style[0]: the string closest to each child node.
style[1]: the rest of the string in the normal child node.
style[2]: the rest of the string in the last child node.
style[3]: whether to add a line specing.
```

The default value of the style option is ("> ", "+-", "+-", False),
which results like below:

```
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
```

For example, The possible styles would be:

```
("> ", "+-", "'-", False)
(" ", "+-", "'-", False)
(" ", "+-", "+-", False)
```


