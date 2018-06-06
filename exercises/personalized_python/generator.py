import sys
import os
import random

instance_dir = sys.argv[1]

with open("names") as name_list_file:
    names = name_list_file.readlines()
    word = random.choice(names)
    with open(os.path.join(instance_dir, "name"), "w") as f:
        f.write(word.strip())
