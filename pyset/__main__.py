#!/usr/bin/python3
import argparse
import pyset.pyset

if __name__ == "__main__":
    """read in csvs and options"""
    parser = argparse.ArgumentParser(description="performs set operations on csvs")
    parser.add_argument("csvs", nargs="*")
    parser.add_argument("--")
    print(parser.parse_args())
