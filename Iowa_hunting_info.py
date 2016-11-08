import random

from flask import Flask
app = Flask(__name__)

class Dates(object):
    def __init__(self,prey,open,close):
        self._prey = prey
        self._open = open
        self._close = close

    @property
    def prey(self):
        return self._prey

    @property
    def open(self):
        return self._open

    @property
    def close(self):
        return self._close

shotgun_dates = [
    dates("teal", "Sept 3rd", "Sept 11th"),
    dates("duck1", "Sept 24", "Oct 2"),
    dates("duck2", "Oct 15th", "Dec 4th"),
    dates("goose1", "Sept 24", "Oct 9th"),
    dates("goose2", "Oct 15th", "Jan 4th")
    dates("pheasant", "Oct 29th", "Jan 10th"),
    dates("deer1", "Dec 3rd", "Dec 7th"),
    dates("deer2", "Dec 10th", "Dec 18th"),
    dates("turkey", "Oct 10th", "Dec 2nd"),
]

bow_dates = [
    dates("deer1", "Oct 1st", "Dec 2nd"),
    dates("deer2", "Dec 19th", "Jan 10th"),
    dates("turkey1", "Oct 1st", "Dec 2nd"),
    dates("turkey2", "Dec 19th", "Jan 10th"),
]

muzzle_loader_dates = [
    dates("deer1", "Oct 15th", "Oct 23rd"),
    dates("deer2", "Dec 19th", "Jan 10th"),
    dates("turkey", "Oct 10th", "Dec 2nd"),
]

class Limits(object):
    def __init__(self,prey,bag,possesion):
        self._prey = prey
        self._bag = bag
        self._possesion = possesion

    @property
    def prey(self):
        return self._prey

    @property
    def bag(self):
        return self._bag

    @property
    def possesion(self):
        return self._possesion

prey_limit = [
    limits("teal", "Daily limit 6", "3 times the daily limit"),
    limits("duck", "Daily limit 6; no more than 4 mallards, 3 wood ducks", "3 times the daily limit"),
    limits("goose", "Daily limit 3", "3 times the daily limit"),
    limits("pheasant", "bag limit 3", "possesion limit 12"),
    limits("deer", "depends on #tags", "depends on #tags"),
    limits("turkey", "depends on #tags", "depends on #tags"),
]

class Notes(object):
    def __init__(self,info):
        self._prey = prey
        self._info = info

    @property
    def prey(self):
        return self._prey

    @property
    def info(self):
        return self._info

prey_info = [
    info("teal", "Must have plug, No lead shot"),
    info("duck", "Must have plug, No lead shot"),
    info("goose", "Must have plug, No lead shot"),
    info("pheasant", "Must wear Blaze orange Hat AND/OR Vest. No Plug needed"),
    info("deer", "Must wear Blaze orange Hat AND/OR Vest. No Plug needed"),
    info("turkey", "Requires permit, no orange required"),
]

class shooting_hours(object):
    def __init__(self,open,close):
        self._prey = prey
        self._open = open
        self._close = close

    @property
    def prey(self):
        return self._prey

    @property
    def open(self):
        return self._open

    @property
    def close(self):
        return self._close

shooting_hours = [
    times("teal", "30 minutes before sunrise", "30 minutes before sunset"),
    times("duck", "30 minutes before sunrise", "30 minutes before sunset"),
    times("goose", "30 minutes before sunrise", "30 minutes before sunset"),
    times("pheasant", "8 AM", "4:30 PM"),
    times("deer", "30 minutes before sunrise", "30 minutes before sunset"),
    times("turkey", "30 minutes before sunrise", "30 minutes before sunset"),
]

@app.route("/api/v1/prey/")
def prey_list():
    return (?).?

@app.route("/api/v1/prey/teal")
def teal_info():
    prey = None
    data = None
    if prey == "teal":
        data = [shotgun_dates, prey_limit,shooting_hours,prey_info]
    if prey == None:
        return "Error"
    return data



@app.route("/api/v1/prey/duck)
def duck_info(duck):
    prey = None
    data = None
    if prey == "duck":
        data = [shotgun_dates, prey_limit,shooting_hours,prey_info]
    if prey == None:
        return "Error"
    return data

@app.route("/api/v1/prey/goose")
def teal_info(goose):
    prey = None
    data = None
    if prey == "goose":
        data = [shotgun_dates, prey_limit,shooting_hours,prey_info]
    if prey == None:
        return "Error"
    return data

@app.route("/api/v1/prey/pheasant")
def teal_info(pheasant):
    prey = None
    data = None
    if prey == "pheasant":
        data = [shotgun_dates, prey_limit,shooting_hours,prey_info]
    if prey == None:
        return "Error"
    return data

@app.route("/api/v1/prey/deer1")
def teal_info(deer):
    prey = None
    data = None
    if prey == "deer1":
        data = [shotgun_dates, bow_dates, muzzle_loader_dates,  prey_limit,shooting_hours,prey_info]
    if prey == None:
        return "Error"
    return data

@app.route("/api/v1/prey/deer2")
def teal_info(deer):
    prey = None
    data = None
    if prey == "deer2":
        data = [shotgun_dates, bow_dates, muzzle_loader_dates, prey_limit,shooting_hours,prey_info]
    if prey == None:
        return "Error"
    return data

@app.route("/api/v1/prey/turkey1")
def teal_info(turkey):
    prey = None
    data = None
    if prey == "turkey1":
        data = [shotgun_dates, bow_dates, muzzle_loader_dates, prey_limit,shooting_hours,prey_info]
    if prey == None:
        return "Error"
    return data

app.route("/api/v1/prey/turkey2")
def teal_info(turkey):
    prey = None
    data = None
    if prey == "turkey2":
        data = [shotgun_dates, bow_dates, muzzle_loader_dates, prey_limit,shooting_hours,prey_info]
    if prey == None:
        return "Error"
    return data

if __name__ == "__main__":
    app.run()
