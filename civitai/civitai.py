import datetime

import requests
import json

BASE_URL = "https://civitai.com/"


class Image:
    def __init__(self, data):
        self.data = data

    @property
    def id(self):
        return self.data["id"]

    @property
    def created_at(self):
        return self.data["createdAt"]

    @property
    def estimated_completion_date(self):
        return self.data["estimatedCompletionDate"]

    @property
    def status(self):
        return self.data["status"]

    @property
    def queue_position(self):
        return self.data["queuePosition"]

    @property
    def params(self):
        return {key: value for key, value in self.data["params"].items()}

    @property
    def resources(self):
        return [Resource(resource) for resource in self.data["resources"]]


class Resource:
    def __init__(self, data, strength=1.0):
        data['strength'] = strength
        self.data = data

    def set_strength(self, strength):
        self.data['strength'] = strength

    @property
    def id(self):
        return self.data["id"]

    @property
    def name(self):
        return self.data["name"]

    @property
    def trained_words(self):
        return self.data["trainedWords"]

    @property
    def model_id(self):
        return self.data["modelId"]

    @property
    def model_name(self):
        return self.data["modelName"]

    @property
    def model_type(self):
        return self.data["modelType"]

    @property
    def base_model(self):
        return self.data["baseModel"]


class Civitai:
    def __init__(self, cookie):
        self.cookie = cookie
        self.__session = requests.Session()
        self.__headers = self.__get_headers()
        self.__session.post(url=BASE_URL, headers=self.__headers)

    def __get_headers(self):
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

    def create_request(self, resources, params):
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

    def get_requests(self):
        url = BASE_URL + "api/trpc/generation.getRequests?input=%7B%22json%22%3A%7B%22cursor%22%3Anull%2C%22authed%22%3Atrue%7D%2C%22meta%22%3A%7B%22values%22%3A%7B%22cursor%22%3A%5B%22undefined%22%5D%7D%7D%7D"
        req = self.__session.get(url=url, headers=self.__headers)
        result = []
        for i in req.json()['result']['data']['json']['items']:
            result.append(Image(i))
        return result

    def get_checkpoints(self, query=""):
        url = BASE_URL + f"api/trpc/generation.getResources?input=%7B%22json%22%3A%7B%22types%22%3A%5B%22Checkpoint%22%5D%2C%22query%22%3A%22{query}%22%2C%22baseModel%22%3Anull%2C%22supported%22%3Atrue%2C%22authed%22%3Atrue%7D%2C%22meta%22%3A%7B%22values%22%3A%7B%22baseModel%22%3A%5B%22undefined%22%5D%7D%7D%7D"
        req = self.__session.get(url=url, headers=self.__headers).json()
        result = []
        for i in req['result']['data']['json']:
            result.append(Resource(i))
        return result

    def get_additional_resources(self, query=""):
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