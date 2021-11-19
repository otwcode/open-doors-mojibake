import random
from .detector import InteractiveDetector
import os
import sys
import difflib
import textwrap
import unicodedata
import re
import itertools

FILE_EXTENSIONS = [".txt", ".html", ".htm"]

control_chars = ''.join(map(chr, itertools.chain(range(0x00,0x20), range(0x7f,0xa0))))
control_char_re = re.compile('[%s]' % re.escape(control_chars))

def remove_control_chars(s: str) -> str:
    return control_char_re.sub('', s)

def get_all_files(root_dir: str) -> list[str]:
    filenames = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if any([file.endswith(x) for x in FILE_EXTENSIONS]):
                filenames.append(os.path.join(root, file))
    return filenames

def detect_encodings_in_dir(root_dir: str):
    filenames = get_all_files(root_dir)
    # We will try to read files in random order, so we have more representative
    # dataset, rather then reading stories from the same era
    random.shuffle(filenames)
    detector = InteractiveDetector()
    try:
        for i, filename in enumerate(filenames):
            print(
                    f"{i + 1}/{len(filenames)}",
                    f"{round(((i + 1) * 100)/len(filenames))}%",
                    sep="  ", end="\r", file=sys.stderr
            )
            with open(filename, "rb") as f:
                detector.feed(f.read())
            if detector.done:
                break
    except KeyboardInterrupt:
        pass
    detector.close()
    print(file=sys.stderr)
    if isinstance(detector.result, dict):
        return [detector.result]
    return detector.result

def compare_diffrences(root_dir: str, encoding_a: str, encoding_b: str):
    filenames = get_all_files(root_dir)
    differ = difflib.Differ()
    for filename in filenames:
        with open(filename, "rb") as f:
            content = f.read()
            encoded = [content.decode(x, errors='ignore').split("\n") for x in (encoding_a, encoding_b)]
            diff = differ.compare(*encoded)
            res = []
            for line in diff:
                if any([line.startswith(x) for x in "-+"]):
                    res.append(line)
            if len(res) > 0:
                lines = []
                for line in res:
                    if line.startswith("- "):
                        line = line.replace("- ", f'{encoding_a} >>>> ', 1)
                    elif line.startswith("+ "):
                        line = line.replace("+ ", f'{encoding_b} >>>> ', 1)
                    line = remove_control_chars(line)
                    lines.append("\n".join(textwrap.wrap(line, width=78, subsequent_indent="\t\t\t")))
                yield "\n".join(lines) + f"\n\n-----\nIn file {filename}" + \
                    "\nPress <Enter> to continue"

            


