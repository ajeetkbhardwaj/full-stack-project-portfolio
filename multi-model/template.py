import os
from pathlib import Path
import logging # used to log into terminals

# logging stream
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    'src/__init__.py', # constructor file to consider src as local package
    'src/utils.py', # consists of all of my helping function
    ".env", # for managing openai api key after commit on github .env file will ignored.
    "requirements.txt", # keep track of dependencies of projects
    "setup.py", # to write local package
    "app.py", # application 
    "research/example.ipynb", # research

]

for filepath in list_of_files:
   # to manage left/right slash to make runnable on any os.
   # WindowsPath('test/test.py')
   filepath = Path(filepath)
   # seperate out folder and file
   filedir, filename = os.path.split(filepath)
   # check if file dir not empty
   if filedir!="":
      # make directory if empty
      os.makedirs(filedir, exist_ok= True)
      # logging to terminal for log message
      logging.info(f"Creating directory; {filedir} for the file: {filename}")

   # check if file exist and size of it if yes then replace the file else
   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      # create the file
      with open(filepath, 'w') as f:
         pass
         logging.info(f"Creating empty file: {filepath}") # file created on terminal

   else:
      logging.info(f"{filename} is already exists") # file already exits