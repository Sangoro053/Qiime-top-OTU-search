import argparse

from qiimetophitsearch import qiimetophitsearch

def q_search():
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='input file')
    parser.add_argument('--module', choices=['tophit', 'tophit_all'], required=True, help='module name')
    parser.add_argument('--scpname')
    args = parser.parse_args()

    if args.module == 'tophit':
        x = qiimetophitsearch.qiimetophitsearch(args.arg1)
        ans = x.tophit(args.scpname)
        print(ans)
    
    elif args.module == 'tophit_all':
        x = qiimetophitsearch.qiimetophitsearch(args.arg1)
        ans = x.tophit_all()
        print(ans)
