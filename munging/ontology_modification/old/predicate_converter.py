# For converting all owl:sameAs and rdfs:seeAlso statements because Protege and PyLode, respectively, give issues
# Somewhat one-off

from rdflib import Graph, Namespace, URIRef
import os

RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")

def convert_predicates(input_ttl, output_ttl):
    g = Graph()
    g.parse(input_ttl, format="turtle")

    # Replacement mappings
    replacements = {
        RDFS.seeAlso: SKOS.example,
        OWL.sameAs: OWL.equivalentClass,
    }

    # Perform replacements
    for old_predicate, new_predicate in replacements.items():
        # Find all triples with the old predicate
        triples = list(g.triples((None, old_predicate, None)))
        for s, p, o in triples:
            # Remove the old triple
            g.remove((s, p, o))
            # Add the new triple with the new predicate
            g.add((s, new_predicate, o))

    g.serialize(destination=output_ttl, format="turtle")
    print(f"Conversion complete. Output saved to {output_ttl}")

scriptDir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(scriptDir, '_DO_NOT_MODIFY.ttl')
output_file = os.path.join(scriptDir, 'please_work.ttl')

convert_predicates(input_file, output_file)