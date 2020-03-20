#!/bin/sh

#     +-> C
#     |   +-> B
#     |       +-> G
#     |       |   +-> H
#     |       |       +-> I
#     |       +-> D
#     +-> F
#       +-> A
#       |   +-> J
#       |   +-> E
#       +-> K

top_dir=test_dir
mkdir -p ${top_dir}/c/b/g/h
touch ${top_dir}/c/b/g/h/i
touch ${top_dir}/c/b/d
mkdir -p ${top_dir}/f/a
touch ${top_dir}/f/a/j
touch ${top_dir}/f/a/e
touch ${top_dir}/f/k
