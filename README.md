# GElasticsearch
A simple python lib for Elasticsearch 5

Example:

```python
es=GElasticsearch()
es.setURL("http://127.0.0.1:9200")

es.createIndex("test")
es.indexSingle("test", "test", {'id': '1', 'email': 'me@domain.com'})
dataDict=[
        {'id': '1', 'email': 'person1@domain.com'},
        {'id': '2', 'email': 'person2@domain.com'},
        ]
es.indexBulk("test", "test", dataDict)
es.deleteSingle("test", "test", "1")
es.deleteIndex("test")
```
