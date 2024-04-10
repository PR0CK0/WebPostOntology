# Munging
This directory contains lots of one-off Python scripts used for very particular tasks, like refactoring old predicates to new ones, e.g., skos:prefLabel to rdfs:label, and for printing all the labels in a text file. There are two sub-directories:

* ```classifier``` contains a script and some other related files for a small sub-project where we tried to classify posts using GPT and our ontology file
* ```ontology_modification``` contains scripts for actually modifying an input .ttl file with RDFLib
* ```ontology_outputting``` contains scripts for reading a .ttl file and outputting the content in some way, e.g., as a textual hierarchy for WordPress