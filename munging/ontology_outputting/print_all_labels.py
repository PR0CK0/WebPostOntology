# For use with a trained GPT in categorizing web posts

import rdflib
import os

scriptDir = os.path.dirname(os.path.abspath(__file__))
inputFile = os.path.join(scriptDir, 'wpo_v0.3.0-alpha.ttl')
outputFile = os.path.join(scriptDir, 'all_labels3.txt')

# Load the Turtle (TTL) file
g = rdflib.Graph()
g.parse(inputFile, format="turtle")

# Namespace for SKOS (change if necessary)
SKOS = rdflib.Namespace("http://www.w3.org/2004/02/skos/core#")

# Extract all prefLabels
pref_labels = g.objects(None, SKOS.prefLabel)

# Write the prefLabels to a file
with open(outputFile, "w") as file:
    for label in pref_labels:
        file.write(f"{label}\n")

print("Finished writing prefLabels")