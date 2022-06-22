import pandas as pd
import os
from time import time


class Data:
    def __init__(self,
                 path: str = None,
                 save_path: str = None,
                 file_name: str = None):
        self.path = path
        self.save_path = save_path
        self.file_name = file_name
    
    def get_data(self, path: str = None):
        if self.path:
            path = self.path
        if not path:
            raise "No path!"

        print('downloading data...')
        data = pd.read_csv(path)

        if self.save_path:
            print('saving data...')
            if self.file_name:
                data.to_pickle(os.path.join(self.save_path, self.file_name))
            else:
                data.to_pickle(os.path.join(self.save_path, f'data_{round(time())}.pkl'))
        return data
