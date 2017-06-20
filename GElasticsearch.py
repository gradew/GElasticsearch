#!/usr/bin/env python

import os, sys
import requests, json

class GElasticsearch:
    baseURL=None

    def __init__(self):
        pass

    def setURL(self, bUrl):
        self.baseURL=bUrl

    def _sendData(self, op, url, payload, bulk=False):
        r=None

        fURL=self.baseURL+"/"+url
        if bulk==False:
            headers={'Content-Type': 'application/json'}
            fData=json.dumps(payload)
        else:
            headers={'Content-Type': 'application/ndjson'}
            fData=payload

        try:
            if op=="POST":
                r=requests.post(fURL, headers=headers, data=fData)
            elif op=="PUT":
                r=requests.put(fURL, headers=headers, data=fData)
        except:
            pass
        return r

    def deleteIndex(self, index):
        return requests.delete(self.baseURL+"/"+index)

    def createIndex(self, index):
        return requests.put(self.baseURL+"/"+index)

    def indexSingle(self, index, _type, _data):
        _id=_data['id']
        del _data['id']
        return requests.put(self.baseURL+"/"+index+"/"+_type+"/"+_id, data=json.dumps(_data))

    def indexBulk(self, index, _type, _data):
        rendered=""
        for element in _data:
            _id=element['id']
            del element['id']
            opDict={'index': {'_index': index, '_type': _type, '_id': _id}}
            rendered=rendered+json.dumps(opDict)+"\n"
            rendered=rendered+json.dumps(element)+"\n\n"
        return self._sendData("POST", index+"/"+_type+"/_bulk", rendered, True)

    def deleteSingle(self, index, _type, _id):
        return requests.delete(self.baseURL+"/"+index+"/"+_type+"/"+_id)
