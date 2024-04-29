from rdflib import Graph, Namespace, RDF, OWL, URIRef
import os

scriptDir = os.path.dirname(os.path.abspath(__file__))

#########################################################################
#########################CHANGE ME AS NEEDED#############################
#########################################################################
input_file = os.path.join(scriptDir, 'wpo_v0.4.1-alpha-new.ttl')
output_file = os.path.join(scriptDir, 'wpo_v0.4.1-alpha-newer.ttl')
#########################################################################

RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")

is_defined_by_iri = URIRef('https://hooray.media/ontology/wpo#')

def add_is_defined_by(input_ttl, output_ttl):
    g = Graph()
    g.parse(input_ttl, format="turtle")

    # Iterate over all classes in the graph
    for class_ in g.subjects(RDF.type, OWL.Class):
        # Add the rdfs:isDefinedBy annotation to each class
        g.add((class_, RDFS.isDefinedBy, is_defined_by_iri))

    g.serialize(destination=output_ttl, format="turtle")
    print(f"Updated Turtle file saved to {output_ttl}")

add_is_defined_by(input_file, output_file)