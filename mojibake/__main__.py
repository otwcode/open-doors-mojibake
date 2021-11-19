from . import detect_encodings_in_dir, compare_diffrences
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
            default=os.path.curdir,
        )

    arguments = parser.parse_args()
    detected = detect_encodings_in_dir(arguments.path)
    if len(detected) == 1:
        print("This archive was detected as", end=" ", file=sys.stderr, flush=True)
        print(detected[0]['encoding'])
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
        print(f"Press <Enter> to compare diffrences beetween {detected[0]['encoding']}"+
                f" and {detected[1]['encoding']}")
        input()
        diffrent_files = 0
        for x in compare_diffrences(arguments.path, *[x['encoding'] for x in detected][:2]):
            if len(x) > 0:
                diffrent_files += 1
                print(x)
            input()
        print(f"Detected diffrences in {diffrent_files} files")

if __name__ == "__main__":
    main()

