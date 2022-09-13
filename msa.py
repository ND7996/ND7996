import Bio
from Bio import AlignIO
alignment = AlignIO.read(open("PF00255_seed.txt"), "stockholm")
print(alignment)