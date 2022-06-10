# -*- coding: utf-8 -*-
import os 
import pands as pd 
def transform:
    def __init__(self):
        # set local path 
        self.local_path = r'./Downloaded_Files/'
    def load_data(self):
        # get file path 
        path  = os.path.join(self.local_path, 'extract.csv')
        # load extracted csv file 
        self.data  = pd.read_csv(path)
        
    def save_transformed_file(self, file):
        # get file path 
        path  = os.path.join(self.local_path, "transformed.csv")
        os.change_dir(path)        
        # save the extracted file as csv
        pd.to_csv(file , index=False)
        
    def transform(self):
        #Convert height which is in inches to millimeter
        #Convert the datatype of the column into float
        #data.height = data.height.astype(float)
        #Convert inches to meters and round off to two decimals(one inch is 0.0254 meters)
        self.data['height'] = round(self.data.height * 0.0254,2)
        
        #Convert weight which is in pounds to kilograms
        #Convert the datatype of the column into float
        #data.weight = data.weight.astype(float)
        #Convert pounds to kilograms and round off to two decimals(one pound is 0.45359237 kilograms)
        self.data['weight'] = round(self.data.weight * 0.45359237,2)
        # save transformed file 
        save_extracted_file(self.data)        
        return data