from rdflib import Graph, Namespace, RDF, OWL, URIRef
import os

# Define the namespaces
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")

# Define the IRI value for rdfs:isDefinedBy
is_defined_by_iri = URIRef('https://hooray.media/ontology/wpo/version/0.3.0-alpha#')

def add_is_defined_by(input_ttl, output_ttl):
    # Load the Turtle file into a graph
    g = Graph()
    g.parse(input_ttl, format="turtle")

    # Iterate over all classes in the graph
    for class_ in g.subjects(RDF.type, OWL.Class):
        # Add the rdfs:isDefinedBy annotation to each class
        g.add((class_, RDFS.isDefinedBy, is_defined_by_iri))

    # Save the modified graph back to a Turtle file
    g.serialize(destination=output_ttl, format="turtle")
    print(f"Updated Turtle file saved to {output_ttl}")

scriptDir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(scriptDir, 'wpo_v0.3.0-alpha.ttl')
output_file = os.path.join(scriptDir, 'wpo_v0.3.0-alpha-new.ttl')

add_is_defined_by(input_file, output_file)
