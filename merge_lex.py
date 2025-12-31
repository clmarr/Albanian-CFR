import UTILS

# Script to create merged lexicon from multiple sources (at OUTPUT)
# they will be organized (quasi phonemically alphabetized) by reflex form, unless modern reflex is obsolesced,
# ... in which case the last stage with content will be used.
# Source language and the point from which it exists in the lexicon are marked in the comment, surrounded by
    # the "circumfix" : STAGE_CIRCUMFIX


OUTPUT ="gjALex.txt"
STAGE_CIRCUMFIX = "_"
NATIVE_NAMES = UTILS.STAGES + ["Albanian"]
OUTPUT_HEADER = UTILS.STAGES

# TODO note error -- this always marks things as the OUTPUT stage.
def cmt_stage_marking(line, header_in_use, src):
    content = UTILS.get_lex_line_content(line)
    if content.strip() == "":
        print("contentless column: "+line)
        return line

    cols = content.split(UTILS.LEX_DELIM)

    infix = ""
    for iter in range(0, len(cols)):
        if cols[iter].strip() not in [UTILS.ABSENT_ETYM, UTILS.UNATTD_ETYM]:
            infix = STAGE_CIRCUMFIX + \
                ("Inherited from " if src in NATIVE_NAMES else "Borrowed from "+src+" into " ) \
                + header_in_use[iter] + STAGE_CIRCUMFIX
            break
    cmt_loc = line.find(UTILS.CMT_FLAG)
    return line + (UTILS.CMT_FLAG if cmt_loc == -1 else "") + infix

# makes sure all lines are going to work with the same output header.
# input_stages : hte ones that are in the input!
def digest_line(ln, inp_stage_names, src):
    outp_si , inp_si = 0 , 0

    inp_st_forms = UTILS.get_lex_line_content(ln).split(UTILS.LEX_DELIM)
    cmt = "" if UTILS.CMT_FLAG not in ln else ln[ln.index(UTILS.CMT_FLAG):]

    if len(inp_st_forms) == 1 and inp_st_forms[0].strip() == "":
        return ln

    if len(inp_stage_names) != len(inp_st_forms):
        raise Exception ("Columnation mismatch error! line : "+ln)

    present_atm = False
    output = []

    while inp_si < len(inp_stage_names):
        if OUTPUT_HEADER[outp_si] == inp_stage_names[inp_si]:
            output += [inp_st_forms[inp_si]]
            present_atm = inp_st_forms[inp_si] != UTILS.ABSENT_ETYM
            outp_si += 1
            inp_si += 1
        else: # output stage not in input
            if inp_stage_names[inp_si] not in OUTPUT_HEADER:
                raise Exception("invalid input stage: "+inp_stage_names[inp_si])
            output += [UTILS.UNATTD_ETYM if present_atm else UTILS.ABSENT_ETYM ]
            outp_si += 1

    # fill in remainder if there are any
    while outp_si < len(OUTPUT_HEADER):
        output += [UTILS.UNATTD_ETYM if present_atm else UTILS.ABSENT_ETYM ]
        outp_si += 1

    return cmt_stage_marking(UTILS.LEX_DELIM.join(output)+" "+cmt,OUTPUT_HEADER,src)

# dictionary with input stage file names as keys and the stage they are marked as as values.
INPUTS = {"ALLAPS.txt" : "Latin"  #various stages of Latin currently working from here, rather than ALLex or the Christian Latin file.
          #"APIELex.txt": "Proto-Indo-European", #PIE inheritance #TODO don't do until reasonably confident with later layers (and fulL)
          #,"APBalkLex.txt": "Proto-Balkan-Indo-European", #Balkan Indo-European formations and substrate etyma #TODO don't do until reasonably confident with later layers (and fulL)
          ,"EPSEALLex.txt" : "Proto-Slavic" #First wave of Slavic loans -- into Late Proto-Albanian I
          ,"MPSEALLex.txt" : "Proto-Slavic" #Middle wave of early Slavic loans -- into Late Proto-Albanian II. To be used sparingly
          ,"LPSEALLex.txt" : "Proto-Slavic" #Last early wave of Slavic loans -- into Late Proto-Albanian III

          , "MGrALAPS.txt" : "Middle Greek" #later waves of Greek.
          ,"ADoLex.txt" : "Doric Greek dialects" #Doric loans into Archaic Proto-Albanian, variously per Huld, Cabej, etc.
          ,"AAttLex.txt" : "Attic Greek dialects" #Attic loans into Archaic Proto-Albanian, variously per Huld, Cabej, etc.
          ,"AMacLex.txt" : "Macedonian, per Huld, " #Macedonian loans into Archaic Proto-Albanian (a likely later time than above tho),
                # as assumed by Huld; TODO maybe move to later era?
          ,"AHesLex.txt" : "Classical Proto-Albanian" #Indo-European inheritance attested by Hesychius of Alexandria
                    # as loans presumably from Proto-Albanian into Greek dialects, currently attributed by me to Classical Proto-Albanian
          # currently not using later Greek layers bc of ambiguities; may revise this tho.
                #TODO not doing until more confident in later stuff etc. They're also in AMacLex.txt.
        }

def extract_file_lines(path):
    f = open(path, encoding="utf-8")
    lines = f.readlines()
    f.close()

    # strip out lines without (uncommented) content
    lines = [li.strip() for li in lines if UTILS.get_lex_line_content(li).strip() != ""]

    #TODO debugging
    print("header: "+lines[0])

    init_by_header = lines[0][0] == UTILS.HEADER_FLAG
    working_header = UTILS.get_lex_line_content(lines[0][1:]).split(UTILS.HEADER_DELIM)
    if not init_by_header:
        if len(working_header) != len(UTILS.STAGES):
            raise Exception("Error: no header, but column count doesn't match global stages. Fix this.")
        working_header = UTILS.STAGES

    source = INPUTS.get(path)
    lines = lines[init_by_header:] # 0 if false
    return [digest_line(li, working_header, source) for li in lines if li.strip() != ""]

#begin to assemble lines.
outplines = []

for inpi in INPUTS.keys():
    print("extracting from : "+inpi)
    outplines += extract_file_lines(inpi)

#outplines = [UTILS.HEADER_FLAG + UTILS.HEADER_DELIM.join(UTILS.STAGES)] + UTILS.linesort(outplines)

outf = open(OUTPUT, encoding="utf-8", mode="w")
outf.write(UTILS.HEADER_FLAG + UTILS.HEADER_DELIM.join(OUTPUT_HEADER)+"\n")
outf.write("\n".join(UTILS.linesort(outplines)))
outf.close()

