from rdflib import Graph, Namespace, RDF, RDFS, SKOS, OWL
import os

def build_hierarchy(graph, class_uri, level=0, hierarchy=[]):    
    # Define the SKOS namespace
    skos = Namespace("http://www.w3.org/2004/02/skos/core#")
    
    # Append the current class to the hierarchy path
    prefLabel = graph.value(class_uri, skos.prefLabel) or class_uri.split('#')[-1]
    hierarchy.append((prefLabel, level))
    
    # Find subclasses of the current class
    subclasses = graph.subjects(predicate=RDFS.subClassOf, object=class_uri)
    
    for subclass in subclasses:
        # Recursive call for each subclass
        build_hierarchy(graph, subclass, level + 1, list(hierarchy))
    
    if level > 0 and not any(graph.subjects(predicate=RDFS.subClassOf, object=class_uri)):
        # Print the hierarchy for leaf classes
        print(" / ".join([h[0] for h in hierarchy]))

def print_class_hierarchy(turtle_file_path):
    g = Graph()
    g.parse(turtle_file_path, format="turtle")
    
    # Define the SKOS namespace
    skos = Namespace("http://www.w3.org/2004/02/skos/core#")

    # Find all classes
    all_classes = set(g.subjects(RDF.type, OWL.Class))
    #print(list(dict.fromkeys(all_classes)))

    # Find top-level classes (those not being a subclass of another class)
    top_level_classes = set(g.objects(None, RDFS.subClassOf))
    print(list(dict.fromkeys(top_level_classes)))

    for top_class in top_level_classes:
        # For each top-level class, build and print its hierarchy
        build_hierarchy(g, top_class)

scriptDir = os.path.dirname(os.path.abspath(__file__))
inputFile = os.path.join(scriptDir, 'wpo_v0.3.0-alpha.ttl')
#outputFile = os.path.join(scriptDir, 'all_labels.txt')       

print_class_hierarchy(inputFile)
