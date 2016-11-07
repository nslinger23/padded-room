import random

from flask import Flask
app = Flask(__name__)

class Quotes(object):
    def __init__(self,name,gender,words):
        self._name = name
        self._gender = gender
        self._words = words

    @property
    def name(self):
        return self._name

    @property
    def gender(self):
        return self._gender

    @property
    def words(self):
        return self._words

male_quotes = [
    Quotes("Eddard", "male", "THE MAN WHO PASSES THE SENTENCE SHOULD SWING THE SWORD."),
    Quotes("Eddard", "male", "WINTER IS COMING."),
    Quotes("Jaime", "male", "THE THINGS I DO FOR LOVE." ),
]


female_quotes = [
    Quotes("Khaleesi", "female", "THE NEXT TIME YOU RAISE A HAND TO ME WILL BE THE LAST TIME YOU HAVE HANDS!"),
    Quotes("Cersei", "female", "WHEN YOU PLAY THE GAME OF THRONES, YOU WIN OR YOU DIE"),

]

random_quotes = male_quotes + female_quotes
@app.route("/api/v1/random/")
def get_random():
    return random.choice(random_quotes).words

@app.route("/api/v1/random/gender/<gender>")
def get_quote_gender(gender):
    data = None
    if gender == "male":
        data = male_quotes
    if gender == "female":
        data = female_quotes
    if data == None:
        return "Error"
    return random.choice(data).words

@app.route("/api/v1/random/name/<name>")
def get_quote_by_name(name):
    data = []
    for x in random_quotes:
        if x.name == name:
            data.append(x.words)
    if data == []:
        return "Error"
    return random.choice(data)



if __name__ == "__main__":
    app.run()
