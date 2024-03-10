import json
import os
import shutil
import string


# Get the labels for the data set

def get_labels(label_path : string) :
    with open(label_path, "r") as f :
        return json.load(f)
