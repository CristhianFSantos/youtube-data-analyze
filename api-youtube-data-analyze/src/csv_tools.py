import pandas as pd

class CsvTools:
    
    def write_data_frame_to_csv(self, list, file_name):
        data_frame = pd.DataFrame(list)
        data_frame.to_csv(file_name, index=False, encoding='utf-8-sig', sep=';')