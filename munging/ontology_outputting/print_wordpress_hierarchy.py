from rdflib import Graph, Namespace, RDF, RDFS, SKOS, OWL, URIRef
import os

def build_hierarchy(graph, class_uri, file, level=0, hierarchy=None):
    skos = Namespace("http://www.w3.org/2004/02/skos/core#")
    """
    Recursive function to build class hierarchy from an RDF graph and write it to a file.
    """
    if hierarchy is None:
        hierarchy = []  # Initialize a new list if none is provided
        file.write(graph.value(class_uri, skos.prefLabel) +'\n')
    
    # Your existing code to build the hierarchy
    prefLabel = graph.value(class_uri, skos.prefLabel) or class_uri.split('#')[-1]
    hierarchy.append((prefLabel, level))
    
    # Find subclasses of the current class
    subclasses = graph.subjects(predicate=RDFS.subClassOf, object=class_uri)
    
    for subclass in subclasses:
        # Recursive call for each subclass with file parameter
        build_hierarchy(graph, subclass, file, level + 1, list(hierarchy))
    
    if level > 0 and not any(graph.subjects(predicate=RDFS.subClassOf, object=class_uri)):
        # Write the hierarchy for leaf classes to the file
        hierarchy_line = "/".join([h[0] for h in hierarchy]) + "\n"
        file.write(hierarchy_line)

def print_class_hierarchy(turtle_file_path, output_file_path):
    """
    Parses a Turtle file and writes the class hierarchy to a text file.
    """
    g = Graph()
    g.parse(turtle_file_path, format="turtle")
    
    # Open the output file in write mode
    with open(output_file_path, 'w') as file:
        top_level_class_iris = {
        URIRef("https://hooray.media/ontology/wpo/version/0.2.0-alpha#Animals"),
        URIRef("https://hooray.media/ontology/wpo/version/0.2.0-alpha#Audience"),
        URIRef("https://hooray.media/ontology/wpo/version/0.2.0-alpha#Family"),
        URIRef("https://hooray.media/ontology/wpo/version/0.2.0-alpha#Health"),
        URIRef("https://hooray.media/ontology/wpo/version/0.2.0-alpha#Home"),
        URIRef("https://hooray.media/ontology/wpo/version/0.2.0-alpha#News"),
        URIRef("https://hooray.media/ontology/wpo/version/0.2.0-alpha#People"),
        URIRef("https://hooray.media/ontology/wpo/version/0.2.0-alpha#Region"),
        URIRef("https://hooray.media/ontology/wpo/version/0.2.0-alpha#SpecialContent"),
        URIRef("https://hooray.media/ontology/wpo/version/0.2.0-alpha#ThingsToDo"),
        URIRef("https://hooray.media/ontology/wpo/version/0.2.0-alpha#Work")
        # Add more IRIs as needed
        }
        top_level_classes = set(top_level_class_iris)

        for top_class in top_level_classes:
            # For each top-level class, build and write its hierarchy
            build_hierarchy(g, top_class, file)

scriptDir = os.path.dirname(os.path.abspath(__file__))
inputFile = os.path.join(scriptDir, 'wpo_v0.2.2-alpha.ttl')
outputFile = os.path.join(scriptDir, 'class_hierarchy.txt')       

print_class_hierarchy(inputFile, outputFile)