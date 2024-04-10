# Since I cannot directly access external files or execute Python code that interacts with them in real-time,
# I'll provide a Python script using RDFlib to print the skos:prefLabel of all classes in a Turtle file.

from rdflib import Graph, Namespace, RDF

def print_skos_prefLabels(turtle_file_path):
    """
    This function prints the skos:prefLabel of all classes defined in a Turtle file.
    """
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

# Assuming the Turtle file is named 'ontology.ttl' and located in the same directory as this script
turtle_file_path = 'ontology.ttl'
print_skos_prefLabels('wpo_v0.2.0-alpha.ttl')

# Note: This script requires RDFlib. Ensure RDFlib is installed in your Python environment before running the script.
# You can install RDFlib using pip: pip install rdflib
# Please adjust 'ontology.ttl' to the path of your Turtle file.
