import argparse
import UTILS

#TODO check that this handles unicode in the argparse...?

parser = argparse.ArgumentParser(
    description="Script to change a phoneme's transcription (beware of accidentally merging transcriptions!)")
parser.add_argument("-f","--file", help="Lexicon file in which to carry out the change", default=False)
parser.add_argument("-s","--stage", help="Stage at which to carry out the transcription change", default=False)
parser.add_argument("-c","--column", help="(stage) Column in which to carry out the transcription change", default=False)
parser.add_argument("-m","--mutandum", help="The phoneme for which transcription is being changed", default=False)
parser.add_argument("-r","--result", help="The new transcription for this phoneme", default=False)
parser.add_argument("-n","--numcols", default=False)
args = parser.parse_args()

if not args.file or not args.mutandum or not args.result:
    raise Exception("Error: need to specify file (-f), transcription to change(-m), and result(-r)")
if not args.column and not args.stage:
    raise Exception("Error: need to specify stage (-s) or column (-c)!")

if UTILS.LEX_DELIM in args.mutandum or UTILS.CMT_FLAG in args.mutandum:
    raise Exception("Can't have lex delim or cmt delim in mutandum!")
if UTILS.LEX_DELIM in args.result or UTILS.CMT_FLAG in args.result:
    raise Exception("Can't have lex delim or cmt delim in result!")

if not args.column:
    args.stage = args.stage.strip()
    if args.stage not in UTILS.STAGES:
        raise Exception("Error: stage '"+args.stage+"' not in stage list!")
    f = open(args.file, encoding="utf-8")
    header = f.readline()
    while len(header.strip()) == 0 :
        header = f.readline()

    headed_by_header = header[0] == UTILS.HEADER_FLAG
    if headed_by_header:
        header = header[len(UTILS.HEADER_FLAG):]

    if UTILS.CMT_FLAG in header:
        header = header[:header.index(UTILS.CMT_FLAG)]

    header = header.strip()

    if UTILS.HEADER_DELIM not in header: #then have to be using only one column and that's the stage
        # can't be output
        if args.stage == UTILS.STAGES[-1]:
            raise Exception("Error: can't use output stage for file with only one column...")
        args.numcols = 1
        args.column = 0

        if headed_by_header:
            if header != args.stage:
                raise Exception("Error: set stage as '"+args.stage+"' but only stage in header is "+header)
    else:
        header_stages = header.split(UTILS.HEADER_DELIM)

        if args.numcols != False:
            if args.numcols != len(header_stages):
                raise Exception("Error: mismatch in numcols!")
        else:
            args.numcols = len(header_stages)

        if headed_by_header:# then will be able to get column by what's there.
            header_stages = [si.strip() for si in header_stages]
            if args.stage not in header_stages:
                raise Exception("Error: set stage as '"+args.stage+"' but it's not detected in the header! (: "+header+")")
            args.column = header_stages.index(args.stage)

        else: # must be same number of stages then.
            if len(UTILS.STAGES) != len(header_stages):
                raise Exception("Error: set stage but no header in this lex file, and number of columns != number of globally specified stages!")
            if args.stage not in UTILS.STAGES:
                raise Exception("Error: set stage but there's no header and the stage set ('"+args.stage+"') is not a globally specified stage!")
            args.column = UTILS.STAGES.index(args.stage)

UTILS.change_transcription(args.file, args.column, args.mutandum, args.result, n_cols = args.numcols)
