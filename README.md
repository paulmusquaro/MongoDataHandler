# MongoDataHandler

This project demonstrates some operations (Read, Update, Delete) on a MongoDB database using PyMongo, with an example of managing a collection of cats. The code is designed to interact with a remote MongoDB instance hosted on MongoDB Atlas.

## Requirements

- Python 3.7+
- MongoDB Atlas account
- Poetry for dependency management

## Features

- Retrieve all cats from the database
- Retrieve a specific cat by name
- Update a cat's age
- Add new features to a cat
- Delete a specific cat by name
- Delete all cats from the database

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/paulmusquaro/MongoDataHandler.git
```

### 2. Set up the Virtual Environment

Create and activate a virtual environment using Poetry:

```bash
poetry install
```
This will automatically create the virtual environment and install the required dependencies listed in the pyproject.toml.

### 4. Set Up Environment Variables

Create a .env file in the project root directory and add the following:

```
DB_USERNAME=your_mongodb_username
DB_PASSWORD=your_mongodb_password
```
Replace your_mongodb_username and your_mongodb_password with your actual MongoDB credentials.

### 5. Activate the Virtual Environment

Once the dependencies are installed, activate the virtual environment:

```bash
poetry shell
```

### 6. Run the Project

You can run the Python script with:

```bash
python main.py
```

## Available Functions

+ `get_all_cats()`: Fetches and prints all cats in the database.
+ `get_cat_by_name(name)`: Fetches and prints a cat by its name.
+ `update_cat_age(name, new_age)`: Updates the age of a cat by name.
+ `update_cat_features(name, feature)`: Adds a new feature to a cat if not already present.
+ `delete_cat(name)`: Deletes a cat by name.
+ `delete_cats()`: Deletes all cats in the collection.

## License

This project is licensed under the MIT License. See the LICENSE file for details.