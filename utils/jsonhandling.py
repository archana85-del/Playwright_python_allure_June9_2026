import json


# filePathJson = "testData/credentials.json"


def jsonhandling(filePathJson):
    with open(filePathJson) as data:
        details = json.load(data)
        return details
    