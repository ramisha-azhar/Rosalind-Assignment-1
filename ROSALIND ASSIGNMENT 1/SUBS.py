s='TTCATGGTTCATGGGTATCAAGGAGGTCATTCATGGATGATTTCATGGTTTCATGGGGTATTCATGGGTTCATGGTACGATTCATGGGCGTTCATGGTTTGTTCATGGTCAAGCTCTTCATGGCGTATCACTTCATGGGGAACTTCATGGTTCATGGGGTTCATGGAGAAACCTTGAGTTCATGGATGAAATTCATGGTTCATGGGAATTCATGGTTCATGGCGTTTCATGGGTTCATGGTTCATGGATTTCATGGTTCATGGATTCATGGAAGTTCATGGAGCCTCTTCATGGTCCGCAAAGAGGGTTCATGGATTCATGGGCGATTCATGGTTGCTTCATGGCATTCATGGATACCGCTTTTCATGGATCTGGGCAATTCATGGGCATTCATGGGTCCTTTCATGGCGGTTCATGGTTCATGGTACTGATTCATGGTTCATGGACATTTCATGGTTTTCATGGTTGTTTCATGGGAATTCATGGTTCATGGTTCATGGTTCATGGTTCATGGTTCATGGCAATTGCTTATTCATGGTTCATGGGCGCATTCATGGTTCATGGAGGGTTCATGGAGTTTCATGGCAGCATTTCATGGCCCTTCATGGTTCATGGGTTCATGGTTCATGGTCTCCTTCATGGCCCGAATTATTCATGGTTCATGGGTTCATGGTGGACTATTGTTCATGGGATTCATGGTCCCTTCATGGCGGTTCATGGATGTTTTCATGGTTCATGGTTCTTTCATGGATTCATGGGAAATACCTTCATGGAGATTCATGGCTCCTATTCATGGTTCATGGTTTCATGGTTCATGGGGGTTCATGGGATGGCCGTTCATGGTTCATGGATCTTCATGGTTCATGGTGTATGTTTCATGG'
t='TTCATGGTT'

def subs(s, t):
    pos = []
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            pos.append(i + 1)
    return pos

print(subs(s,t))