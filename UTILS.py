
HEADER_FLAG = "="
HEADER_DELIM = ","
CMT_FLAG = "$"
LEX_DELIM = " , "

def col_check(file_loc, numcols = False):
    f = open(file_loc, encoding="utf-8")
    lines = [line for line in f.readlines() if len(line.strip()) > 0]
    f.close()

    startloc = int(lines[0][0] == HEADER_FLAG) #1 if true else 0
    ncol = numcols if numcols else len(lines[startloc].split(CMT_FLAG)[0].split([HEADER_DELIM, LEX_DELIM][startloc]))

    error_rows = []
    rows_w_commented_delim = []

    for li in range(startloc, len(lines)):
        commented = CMT_FLAG in lines[li]
        content = lines[li] if not commented else lines[li].split(CMT_FLAG)[0]
        if len(content.strip()) == 0 :
            continue
        cols_here = len(content.split(LEX_DELIM))
        if cols_here != ncol:
            error_rows += [li]
        if commented:
            if len(lines[li].split(CMT_FLAG)[1].split(LEX_DELIM)) > 1:
                rows_w_commented_delim += [li]

    if len(error_rows) > 0:
        print("Rows with errant sizes: " + ", ".join([str(ri) for ri in error_rows]))
    if len(rows_w_commented_delim) > 0:
        print("Rows with column delimiters in comments: "+ ", ".join([str(ri) for ri in rows_w_commented_delim]))

    if len(error_rows) == 0:
        print("no errant rows!")
    else:
        print("error rows:")
        if len(error_rows) > 0:
            for eri in error_rows:
                print(str(eri)+": "+lines[eri][:lines[eri].index(CMT_FLAG)])

