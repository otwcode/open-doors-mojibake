# Mojibake

> **Mojibake** is the garbled text that is the result of text being decoded
> using an unintended character encoding.

This tool uses [chardet]() to detect what character encoding was used in original
backup. When the tool is not certain about what encoding was used it will show
you differences between the most probable ones.

## How to install:

Run `python setup.py install` in repository, on Linux you might need to use `sudo`.

This should make the utility available to you as the `mojibake` command, or by 
running `python -m mojibake`.

If the tool fails to install for you, you can use it by running `python -m mojibake`
in repository.

## How to use:

- `mojibake` will detect encoding of files in current directory.
- `mojibake ./some/path/to/foo/` will detect encoding in specified directory.
- `mojibake -h` will show a help message.

You can stop `mojibake` by pressing `ctrl-c` at any point during the scanning 
process, it will cause the tool to skip the remaining files. 

`mojibake` scans files in a random order, so you should have a representative 
sample by scanning a fraction of files.

### Example output

If you run mojibake on this repository, you will get the following output:

```
~/D/p/open-doors-mojibake $ mojibake .
7/7  100%
We are not quite sure, here is what we have detected:
	Encoding	Confidence
1.	utf-8	94%
2.	Windows-1254	36%
3.	Windows-1252	1%

Press <Enter> to compare differences between utf-8 and Windows-1254

utf-8 >>>> µ - micro aka greek lowercase mu
Windows-1254 >>>> Âµ - micro aka greek lowercase mu
utf-8 >>>> π - pi
Windows-1254 >>>> Ï€ - pi
utf-8 >>>> „” - fancy quotes
Windows-1254 >>>> â€â€ - fancy quotes

-----
In file ./mojibake/tests/test_data/fail0.txt
Press <Enter> to continue

Detected differences in 1 files
```

