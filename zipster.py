#! /usr/bin/python3

import os
import sys
import argparse

import zipfile


def zip_utility(archive_name, paths, mode):
    with zipfile.ZipFile(archive_name, mode) as zip_archive:
        for path in paths:
            file_name = os.path.basename(path)
            new_path = os.path.dirname(path)
            current_dir = os.getcwd()
            os.chdir(new_path)
            zip_archive.write(file_name, compress_type=zipfile.ZIP_DEFLATED)
            os.chdir(current_dir)
    print(f"Zip archive {archive_name} has been created.")


def view_archive_details(archive_name):
    archive = zipfile.ZipFile(archive_name)
    for info in archive.infolist():
        print(f"Displaying data for archive {archive_name}")
        print(f"\t\tUncompressed file size\t{info.file_size} bytes")
        print(f"\t\tCompressed file size\t{info.compress_size} bytes")


if __name__ == "__main__":
    archive_name = "myfolder.zip"

    parser = argparse.ArgumentParser(description="Zipster -- Zip CLI utility")
    parser.add_argument(
        "-z",
        "--zip_archive",
        dest="archive_name",
        action="store",
        help="Zip archive name for the archive created.",
    )
    parser.add_argument(
        "--files",
        nargs="*",
        action="store",
        help="List of paths of files that are to be included in zip archive.",
    )
    parser.add_argument(
        "-v",
        "--view",
        dest="view",
        action="store_true",
        default=False,
        help="Display information about uncompressed and compressed file size.",
    )
    args = parser.parse_args()

    if not (args.archive_name or args.files):
        print(
            "No command line arguments supplied. Please check the help section for relevant information."
        )
        sys.exit(1)

    if args.archive_name in os.listdir(os.curdir):
        choice = input(
            "The archive name that you've provided already exists. Do you want to replace it? (y/n) "
        )
        while choice not in ["y", "n"]:
            choice = input(
                "The archive name that you've provided already exists. Do you want to replace it? (y/n) "
            )
        if choice == "n":
            print(
                "Zip archive not created. Please input the correct archive name again."
            )
            sys.exit(1)

    zip_utility(args.archive_name, paths=args.files, mode="w")
    if args.view:
        view_archive_details(args.archive_name)
