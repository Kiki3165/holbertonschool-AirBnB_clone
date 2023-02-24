# Airbnb Clone Console [![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)]
This is a console application that simulates some of the basic functionality of the Airbnb website. With this console, you can create, view, and book accommodations, as well as manage user accounts.

##Installation
To install this application, simply clone the repository to your local machine:

```bash
git clone https://github.com/Kiki3165/holbertonschool-AirBnB_clone.git
```

Then, navigate to the root directory of the project and install the required dependencies:

```bash
cd holbertonschool-AirBnB_clone
```

## Usage
To start the console, run the following command from the root directory of the project:

```bash
python console.py
```

You will be presented with a command prompt, where you can enter commands to interact with the application. The available commands are:

### create

Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.

Usage: create <class name>

Ex: $ create BaseModel

If the class name is missing, print ** class name missing ** (ex: $ create)

If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)

### show

Prints the string representation of an instance based on the class name and id.

Usage: show <class name> <id>

Ex: $ show BaseModel 1234-1234-1234

If the class name is missing, print ** class name missing ** (ex: $ show)

If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)

If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)

If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)

### destroy

Deletes an instance based on the class name and id (save the change into the JSON file).

Usage: destroy <class name> <id>

Ex: $ destroy BaseModel 1234-1234-1234

If the class name is missing, print ** class name missing ** (ex: $ destroy)

If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ destroy MyModel)

If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)

If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)

### all

Prints all string representation of all instances based or not on the class name.

Usage: all [<class name>]

Ex: $ all BaseModel or $ all

The printed result must be a list of strings (like the example below)

If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)

### update

Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

Usage: update <class name> <id> <attribute name> "<attribute value>"

Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"

Only one attribute can be updated at a time. You can assume the attribute name is valid (exists for this model). The attribute value must be casted to the attribute type.

If the class name is missing, print ** class name missing ** (ex: $ update)

If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ update MyModel)

If the id is missing, print ** instance id missing ** (ex: $ update BaseModel)

If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ update BaseModel 121212)

If the attribute name is missing, print ** attribute name missing ** (ex: $ update BaseModel existing-id)

If the value for the attribute name doesn’t exist, print ** value missing ** (ex: $ update BaseModel existing-id first_name)

## Data Persistence

This console application uses a simple file-based database to store user accounts and accommodation listings in a file.json file.

## Contributing

Contributions to this project are welcome! If you find a bug or have an idea for a new feature, please create a GitHub issue or pull request.

## Authors 

Camille Favriel : https://github.com/CamilleFavriel

Kyllian Terrasson : https://github.com/Kiki3165
