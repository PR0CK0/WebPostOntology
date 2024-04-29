import rdflib
from rdflib.namespace import RDF, SKOS, RDFS

def parseTurtleFile(filePath):
  # Load the Turtle file
  g = rdflib.Graph()
  g.parse(filePath, format="turtle")

  qres = g.query(
    """
    SELECT ?class ?superclass ?label
    WHERE {
      ?class rdfs:subClassOf ?superclass .
      OPTIONAL { ?superclass skos:prefLabel ?label }
    }
    """
  )

  for row in qres:
    classUri, superclassUri, label = row
    if label:
      # Create a definition using the actual skos:prefLabel of the superclass
      definition = rdflib.Literal(f"A {label} that ", lang="en")
      g.add((classUri, SKOS.definition, rdflib.Literal(definition)))

  # Output the modified graph
  g.serialize(destination=filePath, format="turtle")

### Change as needed
parseTurtleFile('munging/wpo_v0.2.0-alpha.ttl')