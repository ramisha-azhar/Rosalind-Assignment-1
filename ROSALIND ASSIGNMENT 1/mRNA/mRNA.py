rna_table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
"UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
"UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
"UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
"CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
"CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
"CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
"AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
"AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
"GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

with open("rosalind_mrna.txt") as myfile: 
    
    data = myfile.readlines()

charData = list(data[0].strip())
#print(charData)

frequency_list = {}

for k,v in rna_table.items():

  if v not in frequency_list:
    frequency_list[v] = 1
  else:
    frequency_list[v] += 1

answer = frequency_list['STOP']
for aa in charData:
  answer = ((answer * frequency_list[aa]) % 1000000)

print (answer)

