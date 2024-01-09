'''data = open ('rosalind_cons (5).txt', 'r').read()
if '>' in data :
    data_string = data.split('>')
    for i in data_string:
        if i == '':
            data_string.remove(i)
            print(data_string)
    for i in data_string : data_string[data_string.index(i)] = i.split('\n', 1)
    for i in data_string : data_string[data_string.index(i)] = [i[0], i[1].replace('\n','')]
    
sequence = []

for i in data_string:
    data_string[data_string.index(i)] = i [1]
    sequence.append(i[1])

n = len (sequence[0])

profile_matrix = {
    'A' : [0]*n,
    'C' : [0]*n,
    'G' : [0]*n,
    'T' : [0]*n,
}

for DNA in sequence:
    for position, neuclotide in enumerate(DNA):
        profile_matrix[neuclotide][position] += 1

result =[]
for position in range (n):
    max_count = 0
    max_nueclotide = None
    for neuclotide in profile_matrix:
        if profile_matrix[neuclotide][position] > max_count:
            max_count = profile_matrix[neuclotide][position]
            max_nueclotide = neuclotide
    result.append(max_nueclotide)


    print(''.join(result))
    print('A:',''.join(map(str, profile_matrix['A'])))
    print('C:',''.join(map(str, profile_matrix['C'])))
    print('G:',''.join(map(str, profile_matrix['G'])))
    print('T:',''.join(map(str, profile_matrix['T'])))

'''

from Bio import SeqIO, motifs


sequence=[]


for seq_record in SeqIO.parse("rosalind_cons (6).txt", "fasta"):
    sequence.append(seq_record.seq)
cons_seq= motifs.create(sequence)
matrix=cons_seq.counts

print(cons_seq.consensus)

good_matrix = {}
for base, values in matrix.items():
    integer_values = [int(value) for value in values]
    good_matrix[base] = integer_values


for base, values in good_matrix.items():
    print(base + ":  " + " ".join(map(str, values)))