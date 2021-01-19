import os

import yaml


def get_base_url_from_settings(part):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "{}_{}.yaml".format("base_config", os.getenv("environment", "stage")))) as file:
        return yaml.load(file, Loader=yaml.FullLoader)[part]


def get_version_api_from_settings(part):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "version_api.yaml")) as file:
        return yaml.load(file, Loader=yaml.FullLoader)[part]


base_url = lambda: get_base_url_from_settings("base_url")
api_v1 = lambda: get_version_api_from_settings("api_v1")
