import os
if not os.path.exists("../raw/data/train.csv"):
    os.symlink(source="../Downloads/train.csv", destination="../input/train.csv") # Create a symlink at "../raw/data/train.csv" that points to "../Downloads/train.csv"
    os.symlink(source="../Downloads/test.csv", destination="../input/test.csv") 

