import sys
import os
import random

instance_dir = sys.argv[1]
number = random.randint(1, 50)
with open(os.path.join(instance_dir, "number"), "w") as f:
    f.write(str(number))
