import cc_dat_utils
import json
import test_json_utils


#Part 1
#Use cc_data_utils.make_cc_data_from_dat() to load pfgd_test.dat
path = "data/pfgd_test.dat"
data = cc_dat_utils.make_cc_data_from_dat(path)
#print the resulting data
print(data)



#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
with open(input_json_file, "r") as jsFile:
    #Use the json module to load the data from the file
    jsData = json.load(jsFile)
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
gmLibrary = test_json_utils.make_game_library_from_json(jsData)
#Print out the resulting GameLibrary data using print_game_library(game_library_data) in test_data.py
print(gmLibrary)
### End Add Code Here ###


#Part 3
import  cc_json_utils
#Load your custom JSON file
inputJsonFile = "data/ley1_cc1.json"
exportDatFile = "data/ley1_cc1.dat"
with open(inputJsonFile, "r") as jsFile:
    #Use the json module to load the data from the file
    jsData = json.load(jsFile)
#Convert JSON data to cc_data
ccData = cc_json_utils.makeDataFile(jsData)
#Save converted data to DAT file
cc_dat_utils.write_cc_data_to_dat(ccData,exportDatFile)
print("done!")
