| website link --> https://eswargupta.pythonanywhere.com/TextSummerizer
 - API was not working suddenly will fix in few days
---

---
# End to end text summerization website making
---
## workflow
|1. Intial setup-->
- Template.py,setup.py,requriments.py,logging,exception_handling create the excpetion class(for this project we are using a custom exception called box.exception) , utils-->if have anything that you you use offen in many places and you no that before in hand then keep that hear

|2. EDA-->
- Do EDA of the data that you want to deal with, Then explore diffrent possible models you want to try etc.... this is in research folder(make sure you upload your data in github or aws etc... so that you can use it in future)

|3. Then start tinkring with --> config.yaml,prams.yaml
---

config.yaml-->
- Hear we need to keep our configaration that is path configaration's of diffrent datasets and many diffrent things needed
prams.yaml--> need to keep a dummy line key : value to avoid errors for this project (Note latter we will add content)
ex:-

data_ingestion_config:
  root_dir: artifacts/data_ingestion
  source_URL: https://github.com/Eswar-gupta/Text_summerizer_website_intiail/blob/main/data/samsung_data.zip
  local_data_file: artifacts/data_ingestion/data.zip
  unzip_dir: artifacts/data_ingestion

- So hear when ever you need to acces the the place when ever in future you want to load data you can use this data_ingestion_config by just importing if you decided to change the data etc... also it will become simple as just you need to give new url link that's it
 
---
4. update entity
- The entity folder is used to define and store configuration classes and data structures that represent the core entities of the project. These entities encapsulate configuration settings, parameters, and other structured data essential for the project's functionality.
ex:-
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

5. update constants inside the src
- We are going to use the config.yaml,prams.yaml etc.. mutiple time so when ever we need their path one way is hard code the path there or keep all these path that mostly won't change in a file that is the __init__.py file of constants
ex:-This is the strating phase of the constants/__init__

```bash
from pathlib import Path

config_yaml_file_path = Path("config\config.yaml")
prams_yaml_file_path = Path("params.yaml")

print(config_yaml_file_path)
print(prams_yaml_file_path)
  
```

6. update configuration manager in src config
 - Keep all the configuration manger function that you generated in the model_train.ipynb note book hear

7. update the componets - data_ingestion,data_tranformation,model_trainer,generating .pkl files there etc...
- First create a separate notebooks for data_ingestion,tranformation,training and everthing
- And then try to write all the class def's and code in block and download the data locaclly and check is everthing working if yes then convert all thi s into a single .py file

8. update pipelines 
9. update main.py
10. update app.py
---

## Comman errors
|1. sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..','..')))
- so if you add this to the grand_child2 then the above is the path to parent
or More relaible thing is 
---
# Get absolute path to project root
PROJECT_ROOT = Path(__file__).parent.parent.absolute()
sys.path.append(str(PROJECT_ROOT))
---
Now you can use
import child1,child2 -- allowed
import prarent -->not allowed 

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..','..')))
This line allows you to acces all the libries inside the the above directory so all inside parent is allowed not parent itself

parent
__init__.py
|--child1
    __init__.py
    |--grand_child1
    __init__.py
__init__.py
|--child2
    __init__.py
    |--grand_child2
    __init__.py


