import requests
import json

BASE_URL = "https://civitai.com/"


class Resource:
    def __init__(self, data, strength=1.0):
        data['strength'] = strength
        self.data = data

    def setStrength(self, strength):
        self.data['strength'] = strength


class Civitai:
    def __init__(self, cookie):
        self.cookie = cookie
        self.__session = requests.Session()
        self.__headers = self.getHeaders()
        self.__session.post(url=BASE_URL, headers=self.__headers)

    def getHeaders(self):
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Connection': 'keep-alive',
            'Referer': 'https://civitai.com/',
            'Cookie': f'{self.cookie}'
        }
        return headers

    def createRequestJson(self, resources, params):
        data = {
            "json": {
                "resources": [e.data for e in resources],
                "params": params,
                "authed": True
            },
            "meta": {
               "values": {
                  "params.baseModel": ["undefined"]
               }
            }
        }
        url = BASE_URL + "api/trpc/generation.createRequest"
        return self.__session.post(url=url, headers=self.__headers, json=data).json()['result']['data']['json']

    def getRequests(self):
        url = BASE_URL + "api/trpc/generation.getRequests?input=%7B%22json%22%3A%7B%22cursor%22%3Anull%2C%22authed%22%3Atrue%7D%2C%22meta%22%3A%7B%22values%22%3A%7B%22cursor%22%3A%5B%22undefined%22%5D%7D%7D%7D"
        return self.__session.get(url=url, headers=self.__headers).json()['result']['data']['json']

    def getCheckpoints(self, query=""):
        url = BASE_URL + f"api/trpc/generation.getResources?input=%7B%22json%22%3A%7B%22types%22%3A%5B%22Checkpoint%22%5D%2C%22query%22%3A%22{query}%22%2C%22baseModel%22%3Anull%2C%22supported%22%3Atrue%2C%22authed%22%3Atrue%7D%2C%22meta%22%3A%7B%22values%22%3A%7B%22baseModel%22%3A%5B%22undefined%22%5D%7D%7D%7D"
        req = self.__session.get(url=url, headers=self.__headers).json()
        result = []
        for i in req['result']['data']['json']:
            result.append(Resource(i))
        return result

    def getAdditionalResources(self, query=""):
        url = BASE_URL + f"api/trpc/generation.getResources?input=%7B%22json%22%3A%7B%22types%22%3A%5B%22LORA%22%2C%22TextualInversion%22%2C%22LoCon%22%5D%2C%22query%22%3A%22{query}%22%2C%22baseModel%22%3Anull%2C%22supported%22%3Atrue%2C%22authed%22%3Atrue%7D%2C%22meta%22%3A%7B%22values%22%3A%7B%22baseModel%22%3A%5B%22undefined%22%5D%7D%7D%7D"
        req = self.__session.get(url=url, headers=self.__headers).json()
        result = []
        for i in req['result']['data']['json']:
            result.append(Resource(i))
        return result



















'''

https://civitai.com/api/trpc/generation.getRequests?input=%7B%22json%22%3A%7B%22cursor%22%3Anull%2C%22authed%22%3Atrue%7D%2C%22meta%22%3A%7B%22values%22%3A%7B%22cursor%22%3A%5B%22undefined%22%5D%7D%7D%7D


params = {
          "json": {
            "resources": [
              {
                "id": 127490,
                "name": "MK V1",
                "trainedWords": [],
                "modelId": 117617,
                "modelName": "MeinaKizuki - Hentai",
                "modelType": "Checkpoint",
                "strength": 1,
                "baseModel": "SD 1.5"
              }
            ],
            "params": {
              "prompt": "1girl",
              "negativePrompt": "EasyNegative,sketch,duplicate,ugly,huge eyes",
              "cfgScale": 5.5,
              "sampler": "DPM++ 2M Karras",
              "seed": 3722448200,
              "steps": 27,
              "clipSkip": 1,
              "quantity": 4,
              "nsfw": True,
              "aspectRatio": "0",
              "baseModel": None
            },
            "authed": True
          },
          "meta": {
            "values": {
              "params.baseModel": [
                "undefined"
              ]
            }
          }
        }'''