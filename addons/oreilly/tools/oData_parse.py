import json 

def change_id_to_ident(oDataDict):
    """ jsonData with a field name 'id' gets changed to 'ident' """
    oDataDict['ident'] = oDataDict['id']
    del oDataDict['id']
    return oDataDict

def json_to_dict(jsonString):
    return json.loads(jsonString.text)

def oreilly_raw_object_to_dict(raw_object):
    for key,value in raw_object:
        json.loads(raw_object[key].text)

def getOVehicles():
    """ returns a storable recent Vehicle List """

def getOrders():
    """ returns a storable recent order list """

