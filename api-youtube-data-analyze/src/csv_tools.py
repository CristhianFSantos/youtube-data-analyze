import pandas as pd
import os

class CsvTools:
    
    def write_data_frame_to_csv(self, list, file_name):
        data_frame = pd.DataFrame(list)
        data_frame.to_csv(file_name, index=False, encoding='utf-8-sig', sep=';')
        
    def check_file_exists(self, file_name):
        try:
            os.remove(file_name)
        except OSError:
            pass
                