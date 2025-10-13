import UTILS

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


def col_check_report(file, ncols = False, verbose = False):
    error_rows, rows_w_commented_delim = col_check(file, ncols)

    if len(error_rows) > 0 and verbose:
        print("Warning: there are errant rows present...")
        print("Rows with errant sizes: " + ", ".join([str(ri) for ri in error_rows]))
    if len(rows_w_commented_delim) > 0 and verbose:
        print("Rows with column delimiters in comments: " + ", ".join([str(ri) for ri in rows_w_commented_delim]))

    if len(error_rows) == 0 and verbose:
        print("No inconsistency in column count among rows, thankfully.")
    elif verbose:
        print("error rows:")
        f = open(file, encoding="utf-8")
        lines = [line for line in f.readlines() if len(line.strip()) > 0]
        f.close()
        for eri in error_rows:
            print(str(eri) + ": " + lines[eri][:lines[eri].index(CMT_FLAG)])

    return len(error_rows) > 0

# given a line, change inp sequence to outp sequence in the given column "col"
def linewise_transcription_change (line, col, inp, outp):
    cmt_start = line.find(CMT_FLAG)
    cmt , content = "", line

    if cmt_start != -1:
        if cmt_start == 0: # whole line is a comment--return it
            return line
        cmt = line[cmt_start:]
        content = line[:cmt_start]

    if content.strip() == "":
        return content + cmt

    if LEX_DELIM not in content:
        if col != 0:
            raise Exception("Error: lack of columns when columns expected")
        return content.replace(inp,outp) + cmt

    cols = content.split(LEX_DELIM)
    cols[col] = cols[col].replace(inp,outp)

    return LEX_DELIM.join(cols) + cmt

def get_lex_line_content(ln):
    if CMT_FLAG in ln:
        ln = ln[:ln.index(CMT_FLAG)]
    return ln

# f file, c column number, m mutandum (thing being changed), r result
def change_transcription(f,c,m,r,n_cols=False):
    # checking for column errors....
    if col_check_report(f,ncols=n_cols,verbose=True):
        raise Exception("Tried to change a transcription in a file with inconsistent columns. Aborting for security purposes.")

    vars = [f,c,m,r]
    if False in vars:
        raise Exception("Error: "
                        + ["file", "column", "mutandum", "result"][vars.index(False)]+" left unspecified!")

    file = open(f, encoding="utf-8")
    lines = file.readlines()
    file.close()

    iter = 0
    while get_lex_line_content(lines[iter]).strip() == "" if iter < len(lines) else False:
        iter += 1

    # lines was just blank in this case. (which would be weird)
    if iter == len(lines):
        return lines

    if lines[iter][0] == HEADER_FLAG:
        iter += 1

    while iter < len(lines):
        lines[iter] = linewise_transcription_change(lines[iter], c, m, r)
        iter += 1

    file = open(f, encoding="utf-8", mode="w")
    file.writelines(lines)
    file.close()

    print("Transcription change from '"+m+"' to '"+r+"' complete!")
