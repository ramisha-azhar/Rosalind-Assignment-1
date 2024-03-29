sequence = 'TCGCTTCCTCTTTTAAGCACCGCCAGAAATGAATAAAACCCTTGTTTGTGATATGCTCTATCGTGAGAGTGGGGTCCCTCCGATCGCACCGACGTGTGATTGCACTTACGGTATTGTTCCGTCGGTGATCTGTTAGGTAGTGTGCACAACAGGATAAGTTAACATCGCATTTTCCCCATCGCTTAGAGCTCTTCTACCCGCACTTACGATCGGCAGTGCTGTCATCATCCCGGTGTTAAGTGCTACTCATGCAGTACGTCGCCTAGACGCCGTAGCCCCGACGAAGTAGTGTCGTCTTCTTGTACACGCGTCCTGATTAGGCCATGAGTAATTCCGCACCCGTGCATTATTGTGTCGCGAAGTACTTGTCCTCATTCAAGTTTTGGGAGATCTTATTGCGTTTGCTGCTTACGGACGGGTGTTGCGACGGTGGAGACTCGTACTAAGTTCACTGATGTTTCCACGTAGCCTGAGGACCTGGCGCCGTTCGTCGCACCAAATACCGGTCCGAGCCCCAGTTTTGCGTGATGAGCAGGATGTCTCCGCCTCGCGTTGCCTCCATCCGAGTGGATGCTAGGCAACGGTATGGCGTATGATCTCATTCTGCTCATCACTTGACTTTGTCAGGCTCCAACAAGTAACCCTTCCAACCCGTTCGTTGGAGGATTGAAAGCCAACTGCGAGTCCGGCTAGCCAGTGCTTCGTGATTTCTTGACTAACAATGGCCGCAAGGACAGATGCTTTATGATTATCTTATACGATCCCAGTTTGGTTACTATGTTGTCGGCCACTGGCAACCACGATCGAAAAGGTCTTGCCCGTTTAGCTCG'
new_sequence = ''

dict_conversion = {
    'A':'T', 
    'T':'A',
    'C':'G',
    'G':'C'}
for pos in range(len(sequence) - 1, -1, -1):
   new_sequence += dict_conversion[sequence[pos]]
print(new_sequence)   

