import shutil
import json
import os


class JsonTools:
    
    def read_json(self, file_name):
        file_ref = open(file_name, encoding="utf8")
        data = json.load(file_ref)
        file_ref.close()
        return data