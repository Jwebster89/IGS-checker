from Bio import SeqIO
from collections import defaultdict
import sys
import json
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

test = "AAGCTACCCGGGAATTGGAAGCTACCCGGGAATTGGAAGCTACCCGGGAATTGGACCAGTTTTGAGGCTGGAAGCTACCCGGGAATTGG"
IGS_1A = "TCAAGGTGGAAAGCTACCCGGGAATTGGACCAGTTTTGAGGCTGGCAGCTACCCGGGAGTTGGCTGAAAAACGACCAAGTCGGACACCTTGGAGCTACCCGGGAATTGGAAATTTGGAGAACGGATTTTGGTGAGTTGGCTGAAAAAACGACCAAGTCAGACATCTGGGAGCTACCCTGGAATTGGGAGCTACCCGGGAATTGGGAGCTACCCGGGAATTGGGAGCTACCCGGGAATTGGGAGCTACCCGGGAATTGGGAGACGAATTCGCCGATTCCTCC"
IGS_2A = "AGTGGCCAGAGACAGCCCCAAGTCCTACCATCTATGGAGGTGGTGGGGTTTTTGGCGTCAAGGTGGAAAGCTACCCGGGAATTGGACCAGTTTTGAGGCTGGCAGCTACCCGGGAGTTGGCTGAAAAACGACCAAGTCGGACACCTTGGAGCTACCCGGGAATTGGGAGCTACCCGGGAATTGGACCAGTTTTGAGGCTGGCAGCTACCCGGGAGTTGGCTGAAAAACGACCAAGTCGGACACCTTGGAGCTACCCGGGAATTGGGAGCTACCCGGGAATTGGGAGACGAATTCGCCGATTCCTCCACCACCAGGCCGTTTCCCGTTACTCTTCTTAGTGCACTGGAAAGAACGTATCGTCCTTAGTATATT"

d={"GAGCTACCCGGGAATTGG" : "R","CAGCTACCCGGGAATTGG" : "R","AAGCTACCCGGGAATTGG" : "R","GAGCTACCCTGGAATTGG" : "R","CAGCTACCCTGGAATTGG" : "R","AAGCTACCCTGGAATTGG" : "R","GAGCTACCCGGGAGTTGG" : "R","CAGCTACCCGGGAGTTGG" : "R","AAGCTACCCGGGAGTTGG" : "R","GAGCTACCCTGGAGTTGG" : "R","CAGCTACCCTGGAGTTGG" : "R","AAGCTACCCTGGAGTTGG" : "R","GAGCTACCCGGGAATCGG" : "R","CAGCTACCCGGGAATCGG" : "R","AAGCTACCCGGGAATCGG" : "R","GAGCTACCCTGGAATCGG" : "R","CAGCTACCCTGGAATCGG" : "R","AAGCTACCCTGGAATCGG" : "R","GAGCTACCCGGGAGTCGG" : "R","CAGCTACCCGGGAGTCGG" : "R","AAGCTACCCGGGAGTCGG" : "R","GAGCTACCCTGGAGTCGG" : "R","CAGCTACCCTGGAGTCGG" : "R","AAGCTACCCTGGAGTCGG" : "R","GAGCTACCCGGGAATTGC" : "R","CAGCTACCCGGGAATTGC" : "R","AAGCTACCCGGGAATTGC" : "R","GAGCTACCCTGGAATTGC" : "R","CAGCTACCCTGGAATTGC" : "R","AAGCTACCCTGGAATTGC" : "R","GAGCTACCCGGGAGTTGC" : "R","CAGCTACCCGGGAGTTGC" : "R","AAGCTACCCGGGAGTTGC" : "R","GAGCTACCCTGGAGTTGC" : "R","CAGCTACCCTGGAGTTGC" : "R","AAGCTACCCTGGAGTTGC" : "R","GAGCTACCCGGGAATCGC" : "R","CAGCTACCCGGGAATCGC" : "R","AAGCTACCCGGGAATCGC" : "R","GAGCTACCCTGGAATCGC" : "R","CAGCTACCCTGGAATCGC" : "R","AAGCTACCCTGGAATCGC" : "R","GAGCTACCCGGGAGTCGC" : "R","CAGCTACCCGGGAGTCGC" : "R","AAGCTACCCGGGAGTCGC" : "R","GAGCTACCCTGGAGTCGC" : "R","CAGCTACCCTGGAGTCGC" : "R","AAGCTACCCTGGAGTCGC" : "R",
   "ACCAGTTTTGAGGCTGG": "A", "ACCAGTTTCGAGGCTGG" : "A",
   "CTGAAAAGACGACCAAGTCGGACACCCTG" : "B", "CTGAAGAGACGACCAAGTCGGACACCCTG" : "B", "CTGAAAAACGACCAAGTCGGACACCCTG" : "B", "CTGAAGAAACGACCAAGTCGGACACCCTG" : "B", "CTGAAAAGACGACCAAGTCAGACACCCTG" : "B", "CTGAAGAGACGACCAAGTCAGACACCCTG" : "B", "CTGAAAAACGACCAAGTCAGACACCCTG" : "B", "CTGAAGAAACGACCAAGTCAGACACCCTG" : "B", "CTGAAAAGACGACCAAGTCGGACATCCTG" : "B", "CTGAAGAGACGACCAAGTCGGACATCCTG" : "B", "CTGAAAAACGACCAAGTCGGACATCCTG" : "B", "CTGAAGAAACGACCAAGTCGGACATCCTG" : "B", "CTGAAAAGACGACCAAGTCAGACATCCTG" : "B", "CTGAAGAGACGACCAAGTCAGACATCCTG" : "B", "CTGAAAAACGACCAAGTCAGACATCCTG" : "B", "CTGAAGAAACGACCAAGTCAGACATCCTG" : "B", "CTGAAAAGACGACCAAGTCGGACACCTTG" : "B", "CTGAAGAGACGACCAAGTCGGACACCTTG" : "B", "CTGAAAAACGACCAAGTCGGACACCTTG" : "B", "CTGAAGAAACGACCAAGTCGGACACCTTG" : "B", "CTGAAAAGACGACCAAGTCAGACACCTTG" : "B", "CTGAAGAGACGACCAAGTCAGACACCTTG" : "B", "CTGAAAAACGACCAAGTCAGACACCTTG" : "B", "CTGAAGAAACGACCAAGTCAGACACCTTG" : "B", "CTGAAAAGACGACCAAGTCGGACATCTTG" : "B", "CTGAAGAGACGACCAAGTCGGACATCTTG" : "B", "CTGAAAAACGACCAAGTCGGACATCTTG" : "B", "CTGAAGAAACGACCAAGTCGGACATCTTG" : "B", "CTGAAAAGACGACCAAGTCAGACATCTTG" : "B", "CTGAAGAGACGACCAAGTCAGACATCTTG" : "B", "CTGAAAAACGACCAAGTCAGACATCTTG" : "B", "CTGAAGAAACGACCAAGTCAGACATCTTG" : "B", "CTGAAAAGACGACCAAGTCGGACACCCGG" : "B", "CTGAAGAGACGACCAAGTCGGACACCCGG" : "B", "CTGAAAAACGACCAAGTCGGACACCCGG" : "B", "CTGAAGAAACGACCAAGTCGGACACCCGG" : "B", "CTGAAAAGACGACCAAGTCAGACACCCGG" : "B", "CTGAAGAGACGACCAAGTCAGACACCCGG" : "B", "CTGAAAAACGACCAAGTCAGACACCCGG" : "B", "CTGAAGAAACGACCAAGTCAGACACCCGG" : "B", "CTGAAAAGACGACCAAGTCGGACATCCGG" : "B", "CTGAAGAGACGACCAAGTCGGACATCCGG" : "B", "CTGAAAAACGACCAAGTCGGACATCCGG" : "B", "CTGAAGAAACGACCAAGTCGGACATCCGG" : "B", "CTGAAAAGACGACCAAGTCAGACATCCGG" : "B", "CTGAAGAGACGACCAAGTCAGACATCCGG" : "B", "CTGAAAAACGACCAAGTCAGACATCCGG" : "B", "CTGAAGAAACGACCAAGTCAGACATCCGG" : "B", "CTGAAAAGACGACCAAGTCGGACACCTGG" : "B", "CTGAAGAGACGACCAAGTCGGACACCTGG" : "B", "CTGAAAAACGACCAAGTCGGACACCTGG" : "B", "CTGAAGAAACGACCAAGTCGGACACCTGG" : "B", "CTGAAAAGACGACCAAGTCAGACACCTGG" : "B", "CTGAAGAGACGACCAAGTCAGACACCTGG" : "B", "CTGAAAAACGACCAAGTCAGACACCTGG" : "B", "CTGAAGAAACGACCAAGTCAGACACCTGG" : "B", "CTGAAAAGACGACCAAGTCGGACATCTGG" : "B", "CTGAAGAGACGACCAAGTCGGACATCTGG" : "B", "CTGAAAAACGACCAAGTCGGACATCTGG" : "B", "CTGAAGAAACGACCAAGTCGGACATCTGG" : "B", "CTGAAAAGACGACCAAGTCAGACATCTGG" : "B", "CTGAAGAGACGACCAAGTCAGACATCTGG" : "B", "CTGAAAAACGACCAAGTCAGACATCTGG" : "B", "CTGAAGAAACGACCAAGTCAGACATCTGG" : "B", "CTGAAAAAACGACCAAGTCGGACACCCTG" : "B", "CTGAAAAAACGACCAAGTCAGACACCCTG" : "B", "CTGAAAAAACGACCAAGTCGGACATCCTG" : "B", "CTGAAAAAACGACCAAGTCAGACATCCTG" : "B", "CTGAAAAAACGACCAAGTCGGACACCTTG" : "B", "CTGAAAAAACGACCAAGTCAGACACCTTG" : "B", "CTGAAAAAACGACCAAGTCGGACATCTTG" : "B", "CTGAAAAAACGACCAAGTCAGACATCTTG" : "B", "CTGAAAAAACGACCAAGTCGGACACCCGG" : "B", "CTGAAAAAACGACCAAGTCAGACACCCGG" : "B", "CTGAAAAAACGACCAAGTCGGACATCCGG" : "B", "CTGAAAAAACGACCAAGTCAGACATCCGG" : "B", "CTGAAAAAACGACCAAGTCGGACACCTGG" : "B", "CTGAAAAAACGACCAAGTCAGACACCTGG" : "B", "CTGAAAAAACGACCAAGTCGGACATCTGG" : "B", "CTGAAAAAACGACCAAGTCAGACATCTGG" : "B",
   "GAATTTGGAGAACGGATTTTGG" : "I", "AAATTTGGAGAACGGATTTTGG" : "I"}


def repeats(DNA):
    """Takes an input IGS sequence in plain text format and finds repeat regions and prints the sequence of repeats to the screen. If the sequence of repeats matches a known
IGS-VCG combo, it will also print out the corresponding VCG.
Example IGS("TCAAGGTGGAAAGCTACCCGGGAATTGGACCAGTTTTGAGGCTGGCAGCTACCCGGGAGTTGGCTGAAAAACGACCAAGTCGGACACCTTGGAGCTACCCGGGAATTGGGAGCTACCCGGGAATTGGACCAGTTTTGAGGCTGGCAGCTACCCGGGAGTTGG
CTGAAAAACGACCAAGTCGGACACCTTGGAGCTACCCGGGAATTGGGAGCTACCCGGGAATTGGACCAGTTTTGAGGCTGGCAGCTACCCGGGAGTTGGCTGAAAAACGACCAAGTCGGACACCTTGGAGCTACCCGGGAATTGGGAGCTACCCGGGAATTGGGAGACG")
Prints:
VCG2A
RARBRRARBRRARBRR
"""
    sequence=[]
    
    for i in range(len(DNA)):
        out_dictionary = defaultdict(int)    
        if len(DNA[i:i+29])>16:
           if DNA[i:i+18] in d.keys() or DNA[i:i+17] in d.keys() or DNA[i:i+29] in d.keys() or DNA[i:i+28] in d.keys() or DNA[i:i+22] in d.keys():
               if DNA[i:i+18] in d.keys():
                   sequence.append(DNA[i:i+18])
               elif DNA[i:i+17] in d.keys():
                   sequence.append(DNA[i:i+17])
               elif DNA[i:i+29] in d.keys():
                   sequence.append(DNA[i:i+29])
               elif DNA[i:i+28] in d.keys():
                   sequence.append(DNA[i:i+28])
               else:
                   DNA[i:i+22] in d.keys()
                   sequence.append(DNA[i:i+22])
    for item in sequence:
        out_dictionary[item] +=1
    return(dict(out_dictionary))


        
def multifasta_repeats_to_json(fasta):
    
    dictionary_list=[]
    with open(fasta, "rU") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            dictionary={}
            dictionary.update({"Sample Name":record.description})
            dictionary.update(repeats(record.seq))
            dictionary_list.append(dictionary)
    json=str(dictionary_list)
    json=json.replace(', SingleLetterAlphabet())','')
    json=json.replace('Seq(','')
    return(json)



fasta=r'C:\Path\to\fasta.fasta'

json_file=json.dumps(multifasta_repeats_to_json(fasta))
file = open('R_VCG_phyl_input.txt','w')
file.write(json_file)
file.close()


