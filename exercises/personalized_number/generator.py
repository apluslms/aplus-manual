import sys
import os
import random

instance_dir = sys.argv[1]
number = random.randint(1, 50)
if not os.path.exists(instance_dir):
    os.makedirs(instance_dir)
with open(os.path.join(instance_dir, "number"), "w") as f:
    f.write(str(number))
