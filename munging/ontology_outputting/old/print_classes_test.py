from rdflib import Graph, Namespace, RDF

def print_skos_prefLabels(turtle_file_path):
    # Initialize the RDF graph
    g = Graph()
    
    # Parse the Turtle file
    g.parse(turtle_file_path, format="turtle")
    
    # Define the SKOS and RDF namespaces
    SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
    OWL = Namespace("http://www.w3.org/2002/07/owl#")
    
    # Query for all instances of owl:Class
    for class_uri in g.subjects(RDF.type, OWL.Class):
        # Fetch the skos:prefLabel for each class
        for label in g.objects(class_uri, SKOS.prefLabel):
            print(f"{class_uri} - {label}")

turtle_file_path = 'ontology.ttl'
print_skos_prefLabels('wpo_v0.2.0-alpha.ttl')