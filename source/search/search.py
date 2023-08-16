import elasticsearch
from elasticsearch_dsl import Search



ELASTIC_HOST = "http://localhost:9200/"

client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST])


INDEXES = ['products']


def lookup(query, index=INDEXES, fields=['title', 'description'], ):
    if not query:
        return
    
    results = Search(index=index).using(client).query("multi_match", fields=fields, fuzziness="AUTO", query=query)
    
    query_results = []

    for hit in results:
        
        print(hit.title)
        print(hit.description)

        data = {
            'id': hit.id,
            'title': hit.title,
            'description': hit.description,
            'url': hit.url,
        }
        query_results.append(data)
    
    return query_results


