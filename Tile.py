#Tile class. Contains information for each tile in the game

import urllib.request #used in display images
import ssl
from PIL import Image
from fuzzywuzzy import fuzz   #string matching library
import random

class tile:
    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.year = dictionary["year"]

        self.picture = dictionary["picture"]
        #self.filename = self.name.replace(" ", "_") + "." + self.picture.split(".")[len(self.picture.split(".")) - 1].lower()

        self.gender = dictionary["gender"]

        self.race = ""
        race_keys = ["American Indian or Alaska Native", "Asian", "Black or African American", "Hispanic or Latino", "Middle Eastern", "Native Hawaiian or Other Pacific Islander", "White", "Other"]
        # iterate through race objects, only add non-blank elements
        for race in race_keys:
            if dictionary[race] != "":
                self.race += dictionary[race] + ", "

        self.major = dictionary["major"]
        self.minor = dictionary["minor"]
        self.modification = dictionary["modification"]

        self.birthday = dictionary["birthday"]
        #create age and astroglocical sign

        self.role = dictionary["role"]
        self.home = dictionary["home"] #turn this into country, US or outside US
        #omit quote
        self.favoriteArtist = dictionary["favoriteArtist"]
        self.favoriteColor = dictionary["favoriteColor"]
        self.phoneType = dictionary["phoneType"]

    def get_image(self, width, height):
        return self.resize_image(self.convert_URL_to_Image(), width, height)

    #purpose: helper function, convert URL to Img
    def convert_URL_to_Image(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        img = Image.open(urllib.request.urlretrieve(self.picture)[0]) #save images to image folder
        return img

    #purpose: helper function, resize Img
    def resize_image(self, img, width, height):
        resized = img.resize((width, height), Image.ANTIALIAS)
        return resized

    def does_not_contains_element(self, key, value):
        if key.lower() == "year" and self.year.lower() != value.lower(): return True
        if key.lower() == "gender" and self.gender.lower() != value.lower(): return True
        if key.lower() == "race" and self.race.lower() != value.lower(): return True
        if key.lower() == "major" and self.major.lower() != value.lower(): return True
        if key.lower() == "minor" and self.minor.lower() != value.lower(): return True
        if key.lower() == "modification" and self.modification.lower() != value.lower(): return True
        if key.lower() == "birthday" and self.birthday.lower() != value.lower(): return True
        if key.lower() == "role" and self.role.lower() != value.lower(): return True
        if key.lower() == "home" and self.home.lower() != value.lower(): return True
        if key.lower() == "favoriteArtist" and self.favoriteArtist.lower() != value.lower(): return True
        if key.lower() == "favoriteColor" and self.favoriteColor.lower() != value.lower(): return True
        if key.lower() == "phoneType" and self.phoneType.lower() != value.lower(): return True
        return False

    def contains_element(self, key, value):

        if key.lower() == "year" and self.year.lower() == value.lower(): return True
        if key.lower() == "gender" and self.gender.lower() == value.lower(): return True
        if key.lower() == "race" and self.race.lower() == value.lower(): return True
        if key.lower() == "major" and self.major.lower() == value.lower(): return True
        if key.lower() == "minor" and self.minor.lower() == value.lower(): return True
        if key.lower() == "modification" and self.modification.lower() == value.lower(): return True
        if key.lower() == "birthday" and self.birthday.lower() == value.lower(): return True
        if key.lower() == "role" and self.role.lower() == value.lower(): return True
        if key.lower() == "home" and self.home.lower() == value.lower(): return True
        if key.lower() == "favoriteArtist" and self.favoriteArtist.lower() == value.lower(): return True
        if key.lower() == "favoriteColor" and self.favoriteColor.lower() == value.lower(): return True
        if key.lower() == "phoneType" and self.phoneType.lower() == value.lower(): return True
        return False