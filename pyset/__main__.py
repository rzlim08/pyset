#!/usr/bin/python3
import argparse

if __name__ == "__main__":
    """read in csvs and options"""
    parser = argparse.ArgumentParser(description="performs set operations on csvs")
    parser.add_argument("csvs", nargs="*")

    print(parser.parse_args())
