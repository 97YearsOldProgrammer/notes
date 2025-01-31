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
    "Glycine", "G", "Gly",
    "What's the most basic R group?",
    "What's the three have resonance ring on it?",
    "What's the two have ketone NH2",
    "What's the two have the carboxylic Acid?",
    "What's the five simple hydrophobic carbohydrate R group?",
    "Which have a disulfide on it?",
    "What's the two have the alcohol group on there?",
    "What's the one have the thiol on there?",
    "What's the one have guanidino on it?",
    "What's the one with pyrrole on it?",
    "Which one have the imidazole ring on it",
    "Which one have pyrrolidine on it?"
]

i = 0 
while i < 10:
    i += 1
    random_item = random.choice(amino_acids)
    print(random_item)