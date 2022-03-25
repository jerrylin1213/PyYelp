import requests
from pprint import pprint
import config
# we need to store the api_key and maybe other important vars to the config.py
# file to prevent others to pretend us. Then put config.py into .gitignore
# so that when we use git, it won't be uploaded

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}

term = input("Enter what you are looking for: ")
location = input(f"Your are looking for {term} near: ")
rating = input("The rating shuold be (between 1 to 5): ")

params = {
    "term": term,
    "location": location,
    "rating": float(rating)
}

response = requests.get(url, headers=headers, params=params)
# print out response.text so that you can know what you're missing
businesses = response.json()["businesses"]
# print(businesses)
# for business in businesses:
#     print(business["name"])
rating_over_45 = [
    business["name"] for business in businesses if business["rating"] > params["rating"]]
pprint(rating_over_45)
