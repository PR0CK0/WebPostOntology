# For converting RDF/RDFS/OWL taxonomies into JSON for nice visualization in jsoncrack

import json, os
from rdflib import Graph, RDFS

scriptDir = os.path.dirname(os.path.abspath(__file__))

#########################################################################
#########################CHANGE ME AS NEEDED#############################
#########################################################################
ttl_file_path = os.path.join(scriptDir, 'wpo_v0.5.0-alpha.ttl')
output_file_path = os.path.join(scriptDir, 'wpo_v0.5.0-alpha.json')
#########################################################################

def convert_ttl_to_json_hierarchy(ttl_file_path, output_file_path):
    g = Graph()
    g.parse(ttl_file_path, format='turtle')

    # Query for all subclass relationships
    query = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?subclass ?class
    WHERE {
      ?subclass rdfs:subClassOf ?class .
    }
    """
    results = g.query(query)

    # Function to get the suffix of a URI
    def get_suffix(uri):
        return uri.split('#')[-1] if '#' in uri else uri.split('/')[-1]

    # Building the hierarchy recursively
    def build_hierarchy(class_name, hierarchy_data):
        subclasses = [get_suffix(subclass) for subclass, parent in hierarchy_data if get_suffix(parent) == class_name]
        hierarchy = {}
        for subclass in subclasses:
            hierarchy[subclass] = build_hierarchy(subclass, hierarchy_data)
        return hierarchy

    # Convert results to a list for easier processing
    results_list = [(str(row[0]), str(row[1])) for row in results]

    # Find root classes (those not appearing as subclasses)
    all_classes = set(get_suffix(parent) for _, parent in results_list)
    all_subclasses = set(get_suffix(subclass) for subclass, _ in results_list)
    root_classes = all_classes - all_subclasses

    hierarchy = {root_class: build_hierarchy(root_class, results_list) for root_class in root_classes}

    #####################################
    # Manual because this script is buggy
    #####################################
    hierarchy["Work"] = {}

    with open(output_file_path, 'w') as outfile:
        json.dump(hierarchy, outfile, indent=4)

convert_ttl_to_json_hierarchy(ttl_file_path, output_file_path)