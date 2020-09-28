import argparse

from qiimetophitsearch import qiimetophitsearch

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='input file')
    parser.add_argument('--module', choices=['tophit', 'tophit_all'], required=True, help='module name')
    parser.add_argument('--scpname')
    args = parser.parse_args()

    if args.module == 'tophit':
        x = qiimetophitsearch(args.arg1)
        x.tophit(args.scpname)
    
    elif args.module == 'tophit_all':
        x = qiimetophitsearch(args.arg1)
        x.tophit_all()

