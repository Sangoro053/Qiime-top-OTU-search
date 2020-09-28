import argparse

from qiimetophitsearch import qiimetophitsearch

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='input file')
    parser.add_argument('--module', choices=['tophit', 'tophit_all'], help='module name')
    parser.add_argument('--scpname')
    args = parser.parse_args()

    if args.arg2 == 'tophit':
        x = qiimetophitsearch(args.arg1)
        x.tophit(args.scpname)
    
    elif args.arg2 == 'tophit_all':
        x = qiimetophitsearch(args.arg1)
        x.tophit_all()

