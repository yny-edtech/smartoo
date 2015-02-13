"""
Utilities for SPARQL language
"""

from __future__ import unicode_literals
from rdflib.plugins.sparql import prepareQuery
from knowledge.namespaces import NAMESPACES_DICT


def prepared_query(query_string):
    """
    Returns prepared query with initialized standard namespaces bindings.
    """
    return prepareQuery(query_string, initNs=NAMESPACES_DICT)

# ---------------------------------------------------------------------------
#  preprepared queries
# ---------------------------------------------------------------------------

#LABEL_QUERY = prepared_query("""
#    SELECT ?label
#    WHERE {
#        ?uri rdfs:label ?label
#    }
#""")


#def label(uri, graph, fallback_guess=True):
#    """
#    Returns label for given uri reference stated in the given graph.

#    Args:
#        uri: URI reference to the object for which to find label
#        graph: where to search for the label
#        fallback_guess: guess the label (using URI) if label wasn't found
#    Returns:
#        label [unicode]
#    """
#    # TODO: misto SPARQL dotazu by stacilo pouzit graph.value(), reps. dokonce
#    # existuje Graph.label() nebo Graph.preferredLabel()
#    result = graph.query(LABEL_QUERY, initBindings={'uri': uri})
#    try:
#        return unicode(next(iter(result))[0])
#    except StopIteration:
#        # no result found
#        if fallback_guess:
#            return uri_to_name(uri)
#        else:
#            return None


#ALL_TERMS_QUERY = prepared_query("""
#    SELECT ?term
#    WHERE {
#        ?term a smartoo:term .
#    }
#""")


# neni potreba: staci pouzit Graph.objecs()
#TYPES_QUERY = prepared_query("""
#    SELECT ?type
#    WHERE {
#        ?term a ?type .
#    }
#""")

# TODO: def discover_types(uri:URIRef)
