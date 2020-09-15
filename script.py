#!/usr/bin/python3

import csv
import sys

    
def escape_sequences(c):
    if c == '"':
        return r'\"'
    elif c == '\\':
        return r"\\"
    return c
    
    
for arg in sys.argv[1:]:
    structure = "<doc title=\"{}\">\n".format(arg)

    data = []
    with open(arg, "r") as f:
        data = list(csv.DictReader(f))

    for entry in data:
        structure += "<comment"
        for key, value in entry.items():
            if key == "comment_text" or value == "":
                continue
            structure += ' {}=\"{}\"'.format(key, value)
        structure += ">\n"

        if not "comment_text" in entry.keys():
            structure += "</comment>\n"
            continue
        structure += "<comment_text>\n"

        # wasn't sure if it was required, alternative to add paragraphs is this
        # paragraphs = "".join(map(escape_sequences, entry["comment_text"])).split('\n')
        # for par in paragraphs:
        #    structure += "<p>\n" + par + "\n</p>\n"

        structure += "".join(map(escape_sequences, entry["comment_text"])) + "\n"
        structure += "</comment_text>\n</comment>\n"
        
    structure += "</doc>\n"
    sys.stdout.writelines(structure)
