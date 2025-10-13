import UTILS
import argparse

# Script to create merged lexicon from multiple sources (at OUTPUT)
# they will be organized (quasi phonemically alphabetized) by reflex form, unless modern reflex is obsolesced,
# ... in which case the last stage with content will be used.
# Source language and the point from which it exists in the lexicon are marked in the comment, surrounded by
    # the "circumfix" STAGE_CIRCUMFIX


OUTPUT = "gjALex.txt"
STAGE_CIRCUMFIX = "_"
NATIVE_NAMES = UTILS.STAGES + ["Albanian"]

def cmt_stage_marking(line, header_in_use, src):
    content = UTILS.get_lex_line_content(line)
    cols = content.split(UTILS.LEX_DELIM)

    infix = ""
    for iter in range(0, len(cols)):
        if cols[iter].strip() not in [UTILS.ABSENT_ETYM, UTILS.UNATTD_ETYM]:
            infix = STAGE_CIRCUMFIX + \
                "Inherited from " if src in NATIVE_NAMES else src+" into " \
                + header_in_use[iter] + STAGE_CIRCUMFIX
    if content.strip() != "":
        print("contentless column: "+line)
        return line

    cmt_loc = line.find(UTILS.CMT_FLAG)
    if cmt_loc != -1:
        return line[:cmt_loc+1] + infix + line[cmt_loc+1:]
    else:
        return line + UTILS.CMT_FLAG + infix


# dictionary with input stage file names as keys and the stage they are marked as as values.
INPUTS = {"ALLAPS.txt" : "Latin",  #various stages of Latin currently working from here, rather than ALLex or the Christian Latin file.
          "APIELex": "Proto-Indo-European", #PIE inheritance
          "APBalkLex": "Proto-Balkan-Indo-European"} #Balkan Indo-European formations and substrate etyma
         # "AGrAPALex": "Greek" #Ancient Greek into Archaic Proto-Albanian, from three Greek sources.
                # -- but currently won't work because multiple headers!
# TODO add in other Greek phases
# TODO add in Slavic phases

def extract_file_lines(path):
    f = open(path, encoding="utf-8")
    lines = f.readlines()
    f.close()

    # strip out lines wihtout (uncommented) content
    lines = [li.strip() for li in lines if UTILS.get_lex_line_content(li).strip() != ""]

    init_by_header = lines[0][0] == UTILS.HEADER_FLAG
    working_header = UTILS.get_lex_line_content(lines[0][1:]).split(UTILS.HEADER_DELIM)
    if not init_by_header:
        if len(working_header) != len(UTILS.STAGES):
            raise Exception("Error: no header, but column count doesn't match global stages. Fix this.")
        working_header = UTILS.STAGES

    source = INPUTS.get(path)
    lines = lines[init_by_header:] # 0 if false
    return [cmt_stage_marking(li, working_header, source) for li in lines]

#begin to assemble lines.
outplines = []

for inpi in INPUTS.keys():
    outplines += extract_file_lines(inpi)

#outplines = [UTILS.HEADER_FLAG + UTILS.HEADER_DELIM.join(UTILS.STAGES)] + UTILS.linesort(outplines)

outf = open(OUTPUT, encoding="utf-8", mode="w")
outf.writeline(UTILS.HEADER_FLAG + UTILS.HEADER_DELIM.join(UTILS.STAGES))
outf.writelines(UTILS.linesort(outplines))
outf.close()

