import UTILS

HEADER_FLAG = "="
HEADER_DELIM = ","
CMT_FLAG = "$"
LEX_DELIM = " , "
PH_DELIM = " "
ABSENT_ETYM = "..."
UNATTD_ETYM = ">*"
STAGES = ["Proto-Indo-European", "Proto-Balkan-Indo-European",
          "Archaic Proto-Albanian", "Classical Proto-Albanian",
          "Middle Proto-Albanian I", "Middle Proto-Albanian II",
          "Late Proto-Albanian I", "Late Proto-Albanian II", "Proto-Tosk-SGheg", "Proto-Tosk",
          "Old North Tosk", "Modern Standard Albanian"]
STRESS_MARKERS = ["ˈ", "ˌ"]
SORT_ORDER = ["a̯","a","ã","aː","ãː","ˌa","ˌã","ˌaː","ˌãː","ˈa","ˈã","ˈaː","ˈãː",
              "ħ","ʕ","ɑ̯","ɑ","ɑ̃","ɑː","ɑ̃ː","ˌɑ","ˌɑ̃","ˌɑː","ˌɑ̃ː","ˈɑ","ˈɑ̃","ˈɑː","ˈɑ̃ː",
              "ɒ̯","ɒ","ɒ̃","ɒː","ɒ̃ː","ˌɒ","ˌɒ̃","ˌɒː","ˌɒ̃ː","ˈɒ","ˈɒ̃","ˈɒː","ˈɒ̃ː",
              "æ̯","æ","æ̃","æː","æ̃ː","ˌæ","ˌæ̃","ˌæː","ˌæ̃ː","ˈæ","ˈæ̃","ˈæː","ˈæ̃ː",
              "χ","ʁ","ɐ̯","ɐ","ɐ̃","ɐː","ɐ̃ː","ˌɐ","ˌɐ̃","ˌɐː","ˌɐ̃ː","ˈɐ","ˈɐ̃","ˈɐː","ˈɐ̃ː",
              "ʔ","h","ɦ","ə̯","ə̯̃","ə","ə̃","əː","ə̃ː","ˌə","ˌə̃","ˌəː","ˌə̃ː","ˈə","ˈə̃","ˈəː","ˈə̃ː",
              "ɛ̯","ɛ","ɛ̃","ɛː","ɛ̃ː","ˌɛ","ˌɛ̃","ˌɛː","ˌɛ̃ː","ˈɛ","ˈɛ̃","ˈɛː","ˈɛ̃ː",
              "œ̯","œ","œ̃","œː","œ̃ː","ˌœ","ˌœ̃","ˌœː","ˌœ̃ː","ˈœ","ˈœ̃","ˈœː","ˈœ̃ː",
              "e̯","e","ẽ","eː","ẽː","ˌe","ˌẽ","ˌeː","ˌẽː","ˈe","ˈẽ","ˈeː","ˈẽː",
              "ø̯","ø","ø̃","øː","ø̃ː","ˌø","ˌø̃","ˌøː","ˌø̃ː","ˈø","ˈø̃","ˈøː","ˈø̃ː",
              "ç","ʝ","j","j̃","i","ĩ","iː","ĩː","ˌi","ˌĩ","ˌiː","ˌĩː","ˈi","ˈĩ","ˈiː","ˈĩː",
              "ʋ","ɥ","ɥ̃","y","ỹ","yː","ỹː","ˌy","ˌỹ","ˌyː","ˌỹː","ˈy","ˈỹ","ˈyː","ˈỹː",
              "ɔ̯","ɔ","ɔ̃","ɔː","ɔ̃ː","ˌɔ","ˌɔ̃","ˌɔː","ˌɔ̃ː","ˈɔ","ˈɔ̃","ˈɔː","ˈɔ̃ː",
              "o̯","o","õ","oː","õː","ˌo","ˌõ","ˌoː","ˌõː","ˈo","ˈõ","ˈoː","ˈõː",
              "q","ɢ","k","kʰ","ɡ","ɡʰ","g","gʰ","ŋ","ŋ̩","x","ɣ","lˠ","l̩ˠ","ɰ",
              "xʷ","ɣʷ","w","w̃","u","ũ","uː","ũː","ˌu","ˌũ","ˌuː","ˌũː","ˈu","ˈũ","ˈuː","ˈũː",
              "c","ɟ","ɟʰ","ɲ","ɲ̩","ʎ","ʎ̩",
              "t͡ʃ","d͡ʒ","ʃ","ʒ",
              "t","t̪","tʰ","d","d̪","dʰ","t͡s","d͡z","t͡θ","d͡ð","s","z","θ","ð","n","n̩","n̪","l","l̩","ɾ","ɾ̩","ɾ̃","ɾ̩̃","r","r̩","ɹ","ɹ̩",
              "p","pʰ","b","bʰ","ɸ","β","f","v","m","m̩",
              ABSENT_ETYM,UNATTD_ETYM,"*",""] #last three shouldn't really be happening...
PH_ORDERING = {String: index for index, String in enumerate(SORT_ORDER)}

def linesort(lines):
    return sorted(lines, key=lambda ln : [SORT_ORDER.index(str) for str in last_content_col_in_line(ln).split(PH_DELIM)])

def last_content_col_in_line(line):

    #TODO debugging
    if "MPL" in line:
        print("MPL in "+line)

    cmt_start = line.find(CMT_FLAG)
    content = line+""
    if cmt_start != -1:
        content = content[:cmt_start].strip()
    if LEX_DELIM not in content:
        return content
    content = content.split(LEX_DELIM)

    for ci in range(1, len(content)):
        if content[-ci] not in [ABSENT_ETYM,UNATTD_ETYM]:
           return content[-ci]

    return content[0]


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
        raise Exception("Tried to change a transcription in a file with inconsistent columns. Should have "+str(n_cols)+" columns. Aborting for security purposes.")

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

