# Mojibake

> **Mojibake** is the garbled text that is the result of text being decoded
> using an unintended character encoding.

This tool uses [chardet]() to detect what character encoding was used in original
backup. When the tool is not certain about what encoding was used it will show
you differences between the most probable ones.

## How to install:

Run `python setup.py install` in repository, on Linux you might need to use `sudo`.

This should make the utility available to you as the `mojibake` command, or by 
running `python -m mojibake`

## How to use:

You can run `mojibake -h` in order to view a help menu.

To detect encoding run `mojibake PATH_TO_FOLDER`. The tool will go through any 
subdirectories as needed. By default `mojibake` will only check `*.txt` and 
`*.html` files. It reads files in a random order.

You can stop `mojibake` by pressing `ctrl-c` at any point during the scanning 
process, it will cause the tool to skip the remaining files.

## Options

More to come!

