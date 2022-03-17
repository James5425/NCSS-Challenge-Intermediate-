def get_sample(sample_filename):
    # Given the name of a sample file, get the DNA chunk from the file.
    # Return the DNA chunk as a string
    pass


def get_known_dna_pairs(pair_filename):
    # Given the name of a file containing DNA pairs, return a dictionary that contains these pairs.
    # The animal names should be dictionary keys and the DNA sequences should be the values.
    # (You'll always call this function with 'dna_pairs.txt')
    pass


def match_dna(sample_dna, dna_dict):
    # Take a DNA sample to identify as a string & a dictionary of known animal DNA sequences/names.
    # Find all the known animals that contain the sample DNA as a substring of their DNA sequence.
    # Return the list of animal names.
    pass


# Write the rest of your program here
dna = ""
lists = []
sample = input("Enter sample file name: ")

with open(sample) as f:
    dna = f.readlines()
with open("dna_pairs.txt") as pairs:
    pairs = pairs.readlines()
    for x in pairs:
        x = x.split()
        try:
            if x[1].index(dna[0]):
                lists.append(x[0])
        except ValueError:
            pass

if len(lists) == 1:
    print(f"That appears to be from a {lists[0]}.")
elif len(lists) == 0:
    print(f"This is a new one!")
else:
    lists = sorted(lists)
    print(f"It could be for any of these animals: {', '.join(map(str, lists))}.")

