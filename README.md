`Python 3.8.11`

The repository consists of the [main](src/main.py) and [preprocessing](src/preprocessing.py) 
scripts to run conjugacy test. 

To run the script clone repository and run [main.py](src/main.py). By default script is running with 
[in.txt](resources/in.txt) file. To run the script with different file, run the script from command line:

```python3 -m src.main -i <input_txt_file_path>```

By default [out.txt](resources/in.txt) file will be created in [resources](resources) directory. 
You can also
specify the path to the desired directory by running the following command:

```python3 -m src.main -i <input_txt_file_path> -o <output_txt_file_path>```
