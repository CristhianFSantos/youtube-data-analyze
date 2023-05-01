import shutil
import json
import os


class JsonTools:
    
    def read_json(self, file_name):
        file_ref = open(file_name, encoding="utf8")
        data = json.load(file_ref)
        file_ref.close()
        return data
    
    def write_json(self, file_path, data):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file_ref:
            json.dump(data, file_ref, indent=4, ensure_ascii=False)
            
    def json_files_clean_directory(self, folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")