from rdflib import Graph, Namespace, RDF, RDFS, SKOS, OWL, URIRef
import os

scriptDir = os.path.dirname(os.path.abspath(__file__))

#########################################################################
#########################CHANGE ME AS NEEDED#############################
#########################################################################
input_file = os.path.join(scriptDir, 'wpo_v0.4.0-alpha.ttl')
output_file = os.path.join(scriptDir, 'class_hierarchy.txt')       
#########################################################################

# Recursive!
def build_hierarchy(graph, class_uri, file, level=0, hierarchy=None):
    if hierarchy is None:
        hierarchy = []  # Initialize a new list if none is provided
        file.write(graph.value(class_uri, RDFS.label) +'\n')
    
    # Your existing code to build the hierarchy
    label = graph.value(class_uri, RDFS.label) or class_uri.split('#')[-1]
    hierarchy.append((label, level))
    
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
    g = Graph()
    g.parse(turtle_file_path, format="turtle")
    
    with open(output_file_path, 'w') as file:
        top_level_class_iris = {
        URIRef("https://hooray.media/ontology/wpo#Animals"),
        URIRef("https://hooray.media/ontology/wpo#Audience"),
        URIRef("https://hooray.media/ontology/wpo#Family"),
        URIRef("https://hooray.media/ontology/wpo#Health"),
        URIRef("https://hooray.media/ontology/wpo#Home"),
        URIRef("https://hooray.media/ontology/wpo#News"),
        URIRef("https://hooray.media/ontology/wpo#People"),
        URIRef("https://hooray.media/ontology/wpo#Region"),
        URIRef("https://hooray.media/ontology/wpo#SpecialContent"),
        URIRef("https://hooray.media/ontology/wpo#ThingsToDo"),
        URIRef("https://hooray.media/ontology/wpo#Work")
        }
        top_level_classes = set(top_level_class_iris)

        for top_class in top_level_classes:
            # For each top-level class, build and write its hierarchy
            build_hierarchy(g, top_class, file)

print_class_hierarchy(input_file, output_file)