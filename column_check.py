import argparse

HEADER_FLAG = "="
HEADER_DELIM = ","
CMT_FLAG = "$"
LEX_DELIM = " , "
#just checking column consistency for now...

parser = argparse.ArgumentParser(description="Script to check consistency of columns") 
parser.add_argument("-f","--file", default="ALLAPS.txt")
parser.add_argument("-n","--numcols", default=False)
args = parser.parse_args()

file_loc = args.file
ncol = args.numcols if args.numcols else len(lines[startloc].split("$")[0].split([HEADER_DELIM,LEX_DELIM][startloc]))

f = open(file_loc, encoding="utf-8")
lines = [line for line in f.readlines() if len(line.strip()) > 0] 
f.close()

startloc = int(lines[0][0] == HEADER_FLAG) #1 if true else 0

error_rows = []
rows_w_commented_delim = []

for li in range(startloc,len(lines)):
	commented = CMT_FLAG in lines[li]
	cols_here = len(lines[li].split(CMT_FLAG)[0].split(LEX_DELIM))
	if cols_here != ncol:
		error_rows += [li]
	if commented:
		if len(lines[li].split(CMT_FLAG)[1].split(LEX_DELIM)) > 1:
			rows_w_commented_delim += [li]

if len(error_rows) > 0:
	print("Rows with errant sizes: "+ ", ".join(error_rows))
if len(rows_w_commented_delim) > 0:
	print("Rows with column delimiters in comments: "+ ", ".join(rows_w_commented_delim))
	
		
	

