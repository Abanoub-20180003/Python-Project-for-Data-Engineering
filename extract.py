# -*- coding: utf-8 -*-

class extract:
    def __init__(self):        
        self.local_path = r'./Downloaded_Files/'
        self.tmpfile    = "temp.tmp"               # file used to store all extracted data
        self.logfile    = "logfile.txt"            # all event logs will be stored in this file
        self.targetfile = "transformed_data.csv"   # file where transformed data is stored
        
    def extract_from_csv(self, file_name):
        # get file path 
        path  = os.path.join(self.local_path, file_name)
        dataframe = pd.read_csv()
        return dataframe

    def extract_from_json(self, file_name):
        # get file path 
        path  = os.path.join(self.local_path, file_name)
        dataframe = pd.read_json(path,lines=True)
        return dataframe
    
    def extract_from_xml(self, file_name):
        # get file path 
        path  = os.path.join(self.local_path, file_name)        
        # create dataframe for the loaded file 
        dataframe = pd.DataFrame(columns=["name", "height", "weight"])       
        # parse the xml as tree 
        tree = ET.parse(path)
        root = tree.getroot()
        #loop over avry parent object 
        for person in root:
            name = person.find("name").text
            height = float(person.find("height").text)
            weight = float(person.find("weight").text)
            dataframe = dataframe.append({"name":name, "height":height, "weight":weight}, ignore_index=True)
        return dataframe
    
    
    def save_extracted_file(self, file):
        # get file path 
        path  = os.path.join(self.local_path, "extract.csv")
        os.change_dir(path)        
        # save the extracted file as csv
        pd.to_csv(file , index=False)
    
    def extract(self):
        extracted_data = pd.DataFrame(columns=['name','height','weight']) # create an empty data frame to hold extracted data        
        #process all csv files
        for csvfile in glob.glob("*.csv"):
            extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)            
        #process all json files
        for jsonfile in glob.glob("*.json"):
            extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)       
        #process all xml files
        for xmlfile in glob.glob("*.xml"):
            extracted_data = extracted_data.append(extract_from_xml(xmlfile), ignore_index=True)
        save_extracted_file(extracted_data)  
        return extracted_data