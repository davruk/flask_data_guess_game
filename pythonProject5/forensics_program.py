suspects = {"Eva": ["TTAGCTATCGC", "AGGCCTCA", "TTGTGGTGGC", "TGAAGGACCTTC", "AAAACCTCA"],
            "Larisa": ["GCCAGTGCCG", "AGGCCTCA", "AAGTAGTGAC", "TGAAGGACCTTC", "AAAACCTCA"],
            "Matej": ["CCAGCAATCGC", "AGGCCTCA", "TTGTGGTGGC", "TGCAGGAACTTC", "AAAACCTCA"],
            "Miha": ["GCCAGTGCCG", "GCCACGG", "GGGAGGTGGC", "TGCAGGAACTTC", "AAAACCTCA"]}


with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

for person in suspects:
    suspect = True
    for prop in suspects[person]:
        if prop not in dna:
            suspect = False
            break
    if suspect is True:
        print("{} is our perpetrator!".format(person.upper()))
