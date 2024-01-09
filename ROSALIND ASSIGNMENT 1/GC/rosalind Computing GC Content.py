

from Bio import SeqIO
highest_gc=0
rosalind_xxxx= None

for seq_record in SeqIO.parse("rosalind_gc (5).txt", "fasta"):
    seq=seq_record.seq

    gc_percent=(seq.count('G')+ seq.count('C'))/len(seq)*100
    if gc_percent>highest_gc:
        highest_gc=gc_percent
        rosalind_xxxx= seq_record.id

print(rosalind_xxxx)
print(highest_gc)