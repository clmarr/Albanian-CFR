import argparse
import UTILS

#just checking column consistency for now...

parser = argparse.ArgumentParser(description="Script to check consistency of columns") 
parser.add_argument("-f","--file", default="ALLAPS.txt")
parser.add_argument("-n","--numcols", default=False)
args = parser.parse_args()

UTILS.col_check_report(args.file, args.numcols)

