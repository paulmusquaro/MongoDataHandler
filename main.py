from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from environs import Env

env = Env()
env.read_env()

client = MongoClient(f"mongodb+srv://{env('DB_USERNAME')}:{env('DB_PASSWORD')}@clusterhw3.cq1kk.mongodb.net/")

db = client.cats


def get_all_cats():
    try:
        cats = db.cats.find()
        for cat in cats:
            print(cat)
    except ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")


def get_cat_by_name(name: str):
    try:
        cat = db.cats.find_one({"name": name})
        if cat is None:
            print('No such cat in the database')
        else:
            print(cat)
    except ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")


def update_cat_age(name: str, new_age):
    try:
        if db.cats.count_documents({"name": name}) == 0:
            print(f"No such cat {name}")
        else:
            result = db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
            if result.modified_count > 0:
                print(f"The cat {name} is now {new_age} years old")
            else:
                print(f"Nothing changed as the cat {name} is already {new_age} years old")
    except ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")


def update_cat_features(name: str, feature: str):
    try:
        if db.cats.count_documents({"name": name}) == 0:
            print(f"No such cat {name}")
        else:
            cat = db.cats.find_one({"name": name, "features": feature})
            if cat:
                print(f"The cat {name} already has the feature {feature}")
            else:
                result = db.cats.update_one({"name": name}, {"$push": {"features": feature}})
                if result.modified_count > 0:
                    print(f"The cat {name} now has a new feature {feature}")
                else:
                    print(f"Nothing changed due to an unknown error.")
    except ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")


def delete_cat(name: str):
    try:
        if db.cats.count_documents({"name": name}) == 0:
            print(f"No such cat {name}")
        else:
            db.cats.delete_one({"name": name})
            print(f"Deleted cat {name}")
    except ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")


def delete_cats():
    try:
        if db.cats.count_documents({}) == 0:
            print("The database is empty")
        else:
            db.cats.delete_many({})
            print("Deleted all cats")
    except ConnectionFailure as e:
        print(f"Error connecting to MongoDB: {e}")


if __name__ == "__main__":
    get_all_cats()
    get_cat_by_name('barsik')
    update_cat_age('Lama', 6)
    update_cat_features('barsik', 'smokes')
    delete_cat('Lama')
    delete_cats()
