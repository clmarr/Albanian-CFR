import argparse
import UTILS

#just checking column consistency for now...

parser = argparse.ArgumentParser(description="Script to check consistency of columns") 
parser.add_argument("-f","--file", default="ALLAPS.txt")
parser.add_argument("-n","--numcols", default=False)
args = parser.parse_args()


error_rows, rows_w_commented_delim = UTILS.col_check(args.file, args.numcols)

if len(error_rows) > 0:
    print("Rows with errant sizes: " + ", ".join([str(ri) for ri in error_rows]))
if len(rows_w_commented_delim) > 0:
    print("Rows with column delimiters in comments: " + ", ".join([str(ri) for ri in rows_w_commented_delim]))

if len(error_rows) == 0:
    print("no errant rows!")
else:
    print("error rows:")
    if len(error_rows) > 0:
        for eri in error_rows:
            print(str(eri) + ": " + lines[eri][:lines[eri].index(CMT_FLAG)])

