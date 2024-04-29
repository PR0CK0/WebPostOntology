from rdflib import Graph, Namespace, URIRef, RDF, OWL
import os

RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")

new_iri = URIRef("https://hooray.media/ontology/wpo/version/0.4.0-alpha#")

def update_is_defined_by(input_ttl, output_ttl):
    g = Graph()
    g.parse(input_ttl, format="turtle")
    
    # Find all subjects that are of type owl:Class
    updated = False
    for s in g.subjects(RDF.type, OWL.Class):
        # Check if there is an existing rdfs:isDefinedBy and update it
        current_iri = g.value(s, RDFS.isDefinedBy)
        if current_iri:
            g.remove((s, RDFS.isDefinedBy, current_iri))
            g.add((s, RDFS.isDefinedBy, new_iri))
            updated = True
        else:
            # Add the new rdfs:isDefinedBy triple if not present
            g.add((s, RDFS.isDefinedBy, new_iri))
            updated = True
    
    if updated:
        g.serialize(destination=output_ttl, format="turtle")
        print(f"Updated Turtle file saved to {output_ttl}")
    else:
        print("No updates necessary.")

scriptDir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(scriptDir, 'wpo_v0.4.0-alpha.ttl')
output_file = os.path.join(scriptDir, 'wpo_v0.4.0-alpha-new.ttl')

update_is_defined_by(input_file, output_file)