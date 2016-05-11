These are many parameters for this program:
1. add_data: adding data from JSON file to couchDB, before using this parameter, Please
	make sure that the path of the JSON file is correct. This parameter has to be 
	follow by a city name.
2. query_data: query data stored in couchDB.
3. train_data: training model, If you want to run this program, please change IP addresses

How to run:
python run.py add_data melborne
python run.py query_data
python train_data