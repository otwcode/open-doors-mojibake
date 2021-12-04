from . import detect_encodings_in_dir, compare_differences
import argparse
import os
import pathlib
import sys

def main():
    parser = argparse.ArgumentParser(
            prog="mojibake",
            description="Wrapper script around chardet to guess character encodings of archive backups." +
                "\nYou can press ctrl-c during lengthy processing to skip some files",
            epilog="Made by OpenDoors"
        )
    parser.add_argument(
            'path',
            metavar="PATH",
            type=pathlib.Path,
            help="Path to the folder containing stories",
            nargs='?'
        )
    arguments = parser.parse_args()
    if arguments.path is None:
        path = os.path.curdir
    else:
        path = arguments.path

    if not os.path.isdir(path):
        print("Specified directory does not exist or is a file!")
        sys.exit(1)

    detected = detect_encodings_in_dir(path)
    if len(detected) == 1:
        print("This archive was detected as", end=" ", file=sys.stderr, flush=True)
        print(detected[0]['encoding'])
    elif len(detected) == 0:
        print("Failed to detect any encoding!")
        sys.exit(1)
    else:
        print(
                "We are not quite sure, here is what we have detected:",
                file=sys.stderr, flush=True
            )
        print(
                "\tEncoding",
                "Confidence",
                sep="\t",
        )
        for i, encoding in enumerate(detected):
            index = i + 1
            print(
                    f"{index}.",
                    encoding['encoding'],
                    f"{round(encoding['confidence'] * 100)}%",
                    sep="\t"
            )

        print()
        print(f"Press <Enter> to compare differences between {detected[0]['encoding']}"+
                f" and {detected[1]['encoding']}")
        input()
        different_files = 0
        for x in compare_differences(path, *[x['encoding'] for x in detected][:2]):
            if len(x) > 0:
                different_files += 1
                print(x)
            input()
        print(f"Detected differences in {different_files} files")

if __name__ == "__main__":
    main()

