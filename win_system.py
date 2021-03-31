import json


def getConfig(configName: str):
    config = open("config.json", "r").read()
    config = json.loads(config)
    if configName in config:
        return config[configName]
    else:
        return None


def saveConfig(data: dict = {}):
    print(data)