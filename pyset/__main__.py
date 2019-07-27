#!/usr/bin/python3
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="performs set operations on csvs")
    parser.add_argument("csv", nargs="*")

    print(parser.parse_args())
