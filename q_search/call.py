import argparse

from qiimetophitsearch import qiimetophitsearch

def q_search():
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='input file')
    parser.add_argument('--module', choices=['tophit', 'tophit_all'], required=True, help='module name')
    parser.add_argument('--scpname')
    args = parser.parse_args()

    if args.module == 'tophit':
        ist_tph = qiimetophitsearch.qiimetophitsearch(args.arg1)
        tph = ist_tph.tophit(args.scpname)
        print(tph)
    
    elif args.module == 'tophit_all':
        ist_tpa = qiimetophitsearch.qiimetophitsearch(args.arg1)
        tpa = ist_tpa.tophit_all()
        print(tpa)
