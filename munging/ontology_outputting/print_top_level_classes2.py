from rdflib import Graph, RDF, RDFS, Namespace, OWL

def print_top_level_classes(turtle_file_path):
    """
    This function identifies and prints top-level classes from a Turtle file.
    Top-level classes are defined as those which are not a subclass of any other class.
    """
    # Initialize the RDF graph
    g = Graph()
    
    # Parse the Turtle file
    g.parse(turtle_file_path, format="turtle")
    
    # Fetch all classes
    all_classes = set(g.subjects(RDF.type, RDFS.Class)) | set(g.subjects(RDF.type, OWL.Class))
    
    # Find and exclude classes that are subclasses of others
    subclass_relations = set(g.objects(None, RDFS.subClassOf))
    
    # Top-level classes are those not found as objects in subclass relations
    top_level_classes = [cls for cls in all_classes if cls not in subclass_relations]
    
    for cls in top_level_classes:
        # Print the URI of each top-level class
        print(cls)

# Replace 'path_to_your_file.ttl' with the actual path to your Turtle file
turtle_file_path = 'wpo_v0.2.0-alpha.ttl'
print_top_level_classes(turtle_file_path)
