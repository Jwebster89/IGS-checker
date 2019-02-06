# IGS-checker
A python script to annotate repeat regions in an IGS sequence and report back the associated VCG

usage python3.5 IGS_checker.py [fasta file]

IGS_checker.py can take a single or multifasta file in the fasta format. Packaged in the script are also two reference sequences for a VCG 1A (IGS_1A) and a 2A (IGS_2A).

# IGS_phylo_R.py
A python script to scan for repeats in a multifasta of IGS and output a file in json format. Note: to import this into the R script, slight editing of the json file needs to be performed.
To edit json file, replace all ' with " by find and replace. Also remove beginning and terminal " so that file starts and ends with an open square bracket and a close square bracket.

#R_IGS_phylo
Takes the output json formatted file from the previous script (Note: json format, output as a .txt file) and imports into R and clusters samples based on repeat frequency and sequence.

![alt text](https://raw.githubusercontent.com/Jwebster89/IGS-checker/Rplot02.png)
