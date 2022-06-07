# -*- coding: utf-8 -*-

import os 
import glob                         # this module helps in selecting files 
import pandas as pd                 # this module helps in processing CSV files
import xml.etree.ElementTree as ET  # this module helps in processing XML files.
from datetime import datetime
import wget
import zipfile

class Download_Files:
    def __init__(self):
        # Set files path
        self.files_path = r'./Downloaded_Files/'  
        
        # change the current directory to specified directory
        os.chdir(self.files_path)
        
        
    def download_files_S3(self):
        # files s3 url
        url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip'
        # Download files from amazon s3 storage
        wget.download(url, out=self.files_path)

    def Unzip_files(self):
        path_to_zip_file = self.files_path + 'source.zip'
        # Unzip files
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall(self.files_path)
     



if __name__ == "__main__":
    downloader = Download_Files()
    downloader.download_files_S3()
    downloader.Unzip_files()