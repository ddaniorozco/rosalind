def kmer_composition(dna):

    nucleotides = ['A', 'C', 'G', 'T']
    freq_dict = {}
    k = 4
    n = len(dna)

    for i in range(4 ** k):
        kmer = ''.join([nucleotides[(i // (4 ** j)) % 4] for j in range(k - 1, -1, -1)])
        freq_dict[kmer] = 0

    for i in range(n - k + 1):
        kmer = dna[i:i + k]
        freq_dict[kmer] += 1

    result = ([freq_dict[kmer] for kmer in sorted(freq_dict.keys())])

    print(result)


sequence = 'CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGGCCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGT' \
           'GCAGTCCCTATTGAGTTTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCAAATGACGTTGGAATATCCCTGTCTAGCT' \
           'CACGCAGTACTTAGTAAGAGGTCGCTGCAGCGGGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGACTTGCCCGTGTT' \
           'AAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTACCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG'

kmer_composition(sequence)
