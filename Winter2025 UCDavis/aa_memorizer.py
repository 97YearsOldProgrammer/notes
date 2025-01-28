import random

amino_acids = [
    "Alanine", "A", "Ala",
    "Valine", "V", "Val",
    "Isoleucine", "I", "Ile",
    "Leucine", "L", "Leu",
    "Phenylalanine", "F", "Phe",
    "Tyrosine", "Y", "Tyr",
    "Tryptophan", "W", "Trp",
    "Serine", "S", "Ser",
    "Threonine", "T", "Thr",
    "Cysteine", "C", "Cys",
    "Methionine", "M", "Met",
    "Asparagine", "N", "Asn",
    "Glutamine", "Q", "Gln",
    "Aspartic Acid", "D", "Asp",
    "Glutamic Acid", "E", "Glu",
    "Lysine", "K", "Lys",
    "Arginine", "R", "Arg",
    "Histidine", "H", "His",
    "Proline", "P", "Pro",
    "Glycine", "G", "Gly"
]

random_item = random.choice(amino_acids)
print(random_item)