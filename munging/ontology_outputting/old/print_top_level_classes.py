from rdflib import Graph, RDF, RDFS, OWL

def print_top_level_classes(turtle_file_path):
    # Initialize the RDF graph
    g = Graph()
    
    # Parse the Turtle file
    g.parse(turtle_file_path, format="turtle")
    
    # Find all subjects that are of type rdfs:Class or owl:Class
    classes = set(g.subjects(RDF.type, RDFS.Class)) | set(g.subjects(RDF.type, OWL.Class))
    
    # Find all subjects that are subclasses of another class
    subclasses = set(g.subjects(RDF.type, RDFS.subClassOf))
    
    # Identify top-level classes by removing subclasses from the set of all classes
    top_level_classes = classes - subclasses
    
    # Print the URIs of top-level classes
    for cls in top_level_classes:
        print(cls)

turtle_file_path = 'wpo_v0.2.0-alpha.ttl'
print_top_level_classes(turtle_file_path)
