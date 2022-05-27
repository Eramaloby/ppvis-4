import json


with open("D:\\Ucheba\\2_курс_2_семестр\\ППВиС\\lab_1\\src\\utility\\config.json", "r") as configfile:
    data = json.load(configfile)


class config():
    @staticmethod
    def get(key: str):
        return data[key]
