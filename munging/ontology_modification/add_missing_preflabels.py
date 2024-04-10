from rdflib import Graph, Literal, URIRef

def addSkosPrefLabel(graph):
    SKOS = URIRef("http://www.w3.org/2004/02/skos/core#")
    prefLabel = SKOS + "prefLabel"

    classQuery = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    SELECT ?class
    WHERE {
      ?class a owl:Class .
    }
    """
    classes = graph.query(classQuery)

    for row in classes:
        classUri = row[0]

        queryCheckPrefLabel = """
        ASK WHERE {
          <%s> <http://www.w3.org/2004/02/skos/core#prefLabel> ?label .
        }
        """ % classUri
        hasPrefLabel = graph.query(queryCheckPrefLabel).askAnswer

        if not hasPrefLabel:
            className = classUri.split("#")[-1]
            classNameWithSpaces = className.replace('_', ' ')  # Replace underscores with spaces
            classLabel = Literal(classNameWithSpaces, lang="en")
            graph.add((classUri, prefLabel, classLabel))

    return graph

# Reading the Turtle file
graph = Graph()
graph.parse("v1.ttl", format="turtle")

# Adding skos:prefLabel to classes
graph = addSkosPrefLabel(graph)

# Serializing the graph to Turtle format and saving it
with open("v1_modified.ttl", "w") as file:
    file.write(graph.serialize(format="turtle"))