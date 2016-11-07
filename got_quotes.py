import random

from flask import Flask
app = Flask(__name__)

class Quotes(object):
    def __init__(self,fname,lname,gender,words):
        self._fname = fname
        self._lname = lname
        self._gender = gender
        self._words = words

    @property
    def fname(self):
        return self._fname

    @property
    def lname(self):
        return self._lname

    @property
    def gender(self):
        return self._gender

    @property
    def words(self):
        return self._words

male_quotes = [
    Quotes("Eddard", "Stark", "male", "THE MAN WHO PASSES THE SENTENCE SHOULD SWING THE SWORD"),
    Quotes("Eddard", "Stark", "male", "WINTER IS COMING."),
    Quotes("Jaime", "Lannister", "male", "THE THINGS I DO FOR LOVE."),
    Quotes("Tywin", "Lannister", "male", "IT'S THE FAMILY NAME THAT LIVES ON. IT'S ALL THAT LIVES ON."),
    Quotes("Jeor", "Mormont", "male", "WHEN DEAD MEN AND WORSE COME HUNTING … YOU THINK IT MATTERS WHO SITS ON THE IRON THRONE?"),
    Quotes("Tyrion", "Lannister", "male", "THE MAD KING DID AS HE LIKED. HAS YOUR UNCLE JAIME EVER TOLD YOU WHAT HAPPENED TO HIM?"),
]


female_quotes = [
    Quotes("Daenerys", "Targaryen", "female", "THE NEXT TIME YOU RAISE A HAND TO ME WILL BE THE LAST TIME YOU HAVE HANDS!"),
    Quotes("Daenerys", "Targaryen", "female", "TURN US AWAY, AND WE WILL BURN YOU FIRST."),
    Quotes("Cersei", "Lannister", "female", "WHEN YOU PLAY THE GAME OF THRONES, YOU WIN OR YOU DIE"),
    Quotes("Catelyn", "Stark", "female", "I PRAYED TO THE GODS 'TAKE HIM AWAY, MAKE HIM DIE"),
    Quotes("Cersei", "Lannister", "female", "IF YOU EVER CALL ME SISTER AGAIN, I'LL HAVE YOU STRANGLED IN YOUR SLEEP")
    Quotes("Arya", "Stark", "female", "Nothing isn't better or worse than anything. Nothing is just nothing"),

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

@app.route("/api/v1/random/fname/<fname>")
def get_quote_by_fname(fname):
    data = []
    for x in random_quotes:
        if x.fname == fname:
            data.append(x.words)
    if data == []:
        return "Error"
    return random.choice(data)

@app.route("/api/v1/random/lname/<lname>")
def get_quote_by_lname(lname):
    data = []
    for x in random_quotes:
        if x.lname == lname:
            data.append(x.words)
    if data == []:
        return "Error"
    return random.choice(data)



if __name__ == "__main__":
    app.run()
