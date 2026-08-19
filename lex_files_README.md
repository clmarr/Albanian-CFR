#Lexicon files and coordination

## gjALex -- gjithë (all) Albanian Lexicon

will be automatically compiled via merge_lex.py, used properly

for periods -- see PeriodizationPolicy (file)

##Lexica in this folder 

(MSTA = Modern Standard (Tosk) Albanian)

###Single stage lexica

####ALLex = Albanian Latin Lexicon 
	Classical Latin loans in to Classical Proto-Albanian, inherited into MSTA 
	longest running lexicon
	work began in 2022
	
	Exclusions justification : "ExclusionsFromALLex"
			-- may be worth considering for insertions at later layers! 
			
	best to build gjALex off of ALLex though as some work was done in late June onto gjALex 
		but now basing off ALLAPS
	
####APIELex 

Proto-Indo-European etyma inherited into modern Albanian

####APIECorrLEx

Only the relatively secure inherited PIE lexis. 
	
####APBalkLex.txt

from Balkan substrata into tentative common ancestor of Greek, Albanian (Armenian?) 
	
####EPSEALLex 
	loans from Slavic into LPA I 
		
####MPSEALLex
	loans from Slavic into LPA II

####LPSEALLex
	loans from Slavic into LPA III

####MGrALAPS
	loans from Middle Greek into MPA I and LPA II 
	
####ADoLex
	Doric loans into Archaic Proto-Albanian

####AMacLex
	proposed Macedonian loans into Archaic Proto-Albanian (and Hesychius unless commented) 

####AGrLex
	general ancient Greek loans, dialect neutral. 

####some decisions let over on these legacy files: 

"ExclusionsFromALLex" 
"Excluded Greek etyma.txt" 
etc.
	
###Multistage lexica


####ALLAPS 
also with intermediate forms worked in
	should use this as a basisǃ 
largely Latin etyma, used in mid 2025, seems to differ from ALLex by 15 -- ID which these are. 
	1. consideration of alternate hypotheses for dating of allegoria > logori
	2. MPA I evigl-aː- > yej, per Lopuhaa 2015
	3. MPA I faʎ-aː > fyej, per Lopuhaa 2015
	4. alternative dating of causa > kafshë 
	5-6. two alternatives for cavula > gavër 
	7. alternative dating for collare > kular
	8-9. alternative datings for lëvdoj, lavd
	10. pagav-å- > paguaj from Italo-Romance, per Lopuhaa			[this one also into ALLex. ] 
	11. prohib-eː- > pruaj per Meyer apud Lopuhaa		[also into ALLex]
	12. sclawi > shqe "Slav.PL", in addition to shqa
	13. sed-aː-> shuoaj per Lopuhaa 2015 			[also into ALLex]
	14. val-eː- > vyej per Lopuhaa 2015			[also into ALLex]
	15. alt hypoth for miraculum's regular outcome
	(16.??) debitoːritium > detorës 
	17 .strambinu > shtrembër
	?? 
		a couple things not mutually co-addressed, but long story short, should work off ALLAPSǃ 

(this is now outdated ^ )

### Automatically merged stage lexica

####created via python script merge_lex.py

to run: 
	specify name of file on line 9 : OUTPUT = {file name}

	specify which lexicon files to combine to form it by commenting in or out different file names on lines 70-88 , variable INPUTS. 

####gjALex.txt

all layers from Greek lexis into APA onward

####slavALex.txt

EPSEALLex + MPSEALLex + LPSEALLex

