from rdflib import Graph, Namespace, URIRef, RDF, RDFS
import os

RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")

# New IRI for rdfs:isDefinedBy
new_iri = URIRef("abcdefg#")
# and then find and replace in notepad because this script is buggy

def update_is_defined_by(input_ttl, output_ttl):
    g = Graph()
    g.parse(input_ttl, format="turtle")
    
    # Find all subjects with rdfs:isDefinedBy predicate
    for s, p, o in g.triples((None, RDFS.isDefinedBy, None)):
        # Remove the old triple
        g.remove((s, RDFS.isDefinedBy, o))
        # Add the new triple with updated IRI
        g.add((s, RDFS.isDefinedBy, new_iri))
    
    g.serialize(destination=output_ttl, format="turtle")
    print(f"Updated Turtle file saved to {output_ttl}")

scriptDir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(scriptDir, 'wpo_v0.5.0-alpha.ttl')
output_file = os.path.join(scriptDir, 'wpo_v0.5.0-alpha-newest.ttl')

update_is_defined_by(input_file, output_file)