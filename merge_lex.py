

OUTPUT = "gjALex.txt"
STAGE_DELIM = " , "
ABSENT_ETYM = "..."
UNATTD_ETYM = ">*"
STAGES = ["Proto-Indo-European", "Proto-Balkan-Indo-European",
          "Archaic Proto-Albanian", "Classical Proto-Albanian",
          "Middle Proto-Albanian I", "Middle Proto-Albanian II",
          "Late Proto-Albanian I", "Late Proto-Albanian II", "Proto-Tosk",
          "Old North Tosk", "Modern Standard Albanian"]

INPUT_FILES = ["ALLAPS", #various stages of Latincurrently working from here, rather than ALLex or the Christian Latin file.
    "APIELex", #PIE inheritance
    "APBalkLex", #Balkan Indo-European formations and substrate etyma
    "AGrAPALex" #Ancient Greek into Archaic PRoto-Albanian, from three Greek sources.
               # TODO add in other Greek phases
               # TODO add in Slavic phases
               ]
