from rdflib import Graph, Namespace, URIRef
import os

SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")

def convert_preflabel_to_label(input_ttl, output_ttl):
    g = Graph()
    g.parse(input_ttl, format="turtle")
    
    preflabel_triples = list(g.triples((None, SKOS.prefLabel, None)))
    
    for s, p, o in preflabel_triples:
        g.remove((s, p, o))
        g.add((s, RDFS.label, o))
    
    g.serialize(destination=output_ttl, format="turtle")
    print(f"Conversion complete. Output saved to {output_ttl}")

scriptDir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(scriptDir, 'wpo_v0.3.0-alpha.ttl')
output_file = os.path.join(scriptDir, 'wpo_v0.3.0-alpha-new.ttl')

convert_preflabel_to_label(input_file, output_file)