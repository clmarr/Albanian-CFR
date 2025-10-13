HEADER_FLAG = "="
HEADER_DELIM = ","
CMT_FLAG = "$"
LEX_DELIM = " , "
ABSENT_ETYM = "..."
UNATTD_ETYM = ">*"
STAGES = ["Proto-Indo-European", "Proto-Balkan-Indo-European",
          "Archaic Proto-Albanian", "Classical Proto-Albanian",
          "Middle Proto-Albanian I", "Middle Proto-Albanian II",
          "Late Proto-Albanian I", "Late Proto-Albanian II", "Proto-Tosk",
          "Old North Tosk", "Modern Standard Albanian"]


def col_check(file_loc, numcols=False):
    f = open(file_loc, encoding="utf-8")
    lines = [line for line in f.readlines() if len(line.strip()) > 0]
    f.close()

    startloc = int(lines[0][0] == HEADER_FLAG)  # 1 if true else 0
    ncol = numcols if numcols else len(lines[startloc].split(CMT_FLAG)[0].split([HEADER_DELIM, LEX_DELIM][startloc]))

    error_rows = []
    rows_w_commented_delim = []

    for li in range(startloc, len(lines)):
        commented = CMT_FLAG in lines[li]
        content = lines[li] if not commented else lines[li].split(CMT_FLAG)[0]
        if len(content.strip()) == 0:
            continue
        cols_here = len(content.split(LEX_DELIM))
        if cols_here != ncol:
            error_rows += [li]
        if commented:
            if len(lines[li].split(CMT_FLAG)[1].split(LEX_DELIM)) > 1:
                rows_w_commented_delim += [li]

    return error_rows, rows_w_commented_delim


def col_check_report (file, ncols = False):
    error_rows, rows_w_commented_delim = col_check(file, ncols)

    if len(error_rows) > 0:
        print("Rows with errant sizes: " + ", ".join([str(ri) for ri in error_rows]))
    if len(rows_w_commented_delim) > 0:
        print("Rows with column delimiters in comments: " + ", ".join([str(ri) for ri in rows_w_commented_delim]))

    if len(error_rows) == 0:
        print("no errant rows!")
    else:
        print("error rows:")
        f = open(file, encoding="utf-8")
        lines = [line for line in f.readlines() if len(line.strip()) > 0]
        f.close()
        for eri in error_rows:
            print(str(eri) + ": " + lines[eri][:lines[eri].index(UTILS.CMT_FLAG)])


# f file, c column number, m mutandum (thing being changed), r result
def change_transcription(f,c,m,r):
    # checking for column errors....
    err_rows= col_check(f)[0]

    if len(err_rows) > 0:
        print("Warning: there are errant rows present...")
        f = open(f, encoding="utf-8")
        lines = [line for line in f.readlines() if len(line.strip()) > 0]
        f.close()
        for eri in err_rows:
            print(str(eri) + ": " + lines[eri][:lines[eri].index(UTILS.CMT_FLAG)])
        raise Exception("Tried to change a transcription in a file with inconsistent columns. Aborting for security purposes.")
    else:
        print("No inconsistency in column count among rows, thankfully.")



