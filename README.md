# AirBnB Clone - The Console
---
The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

[![N|Solid](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20191114%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20191114T033236Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=beed2c407ba88b28daca7260583f3625c1c138c7a799f76214012854b563e1ca)]
#### Functionalities of this command interpreter:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object
## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of use](#examples-of-use)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)
## Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)
## Installation
* Clone this repository: 'https://github.com/Liliana327/AirBnB_clone.git'
* Access AirBnb directory: cd AirBnB_clone
* Run hbnb(interactively): ./console and enter command
* Run hbnb(non-interactively): echo "<command>" | ./console.py
## File Descriptions
[console.py](console.py) - the console contains the entry point of the command interpreter.
List of commands this console current supports:
* EOF - exits console
* quit - exits console
* <emptyline> - overwrites default emptyline method and does nothing
* create - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* destroy - Deletes an instance based on the class name and id (save the change into the JSON file).
* show - Prints the string representation of an instance based on the class name and id.
* all - Prints all string representation of all instances based or not on the class name.
* update - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
#### models/ directory contains classes used for this project:

## Files
---
| File | Description |
| ---- | ------- |
| _base_model.py | The BaseModel class from which future classes will be derived |
| _def __init__ |(self, *args, **kwargs) - Initialization of the base model |
| _def __str__| (self) - String representation of the BaseModel class |
| _def save(self) | - Updates the attribute updated_at with the current datetime |
| _def to_dict(self) | - returns a dictionary containing all keys/values of the instance |

Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)
#### /models/engine directory contains File Storage class that handles JASON serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* def all(self) - returns the dictionary __objects
* def new(self, obj) - sets in __objects the obj with key <obj class name>.id
* def save(self) - serializes __objects to the JSON file (path: __file_path)
*  def reload(self) -  deserializes the JSON file to __objects

