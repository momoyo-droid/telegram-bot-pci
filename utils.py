import random as rd

MAX_MSG_FWD = 300  # FWD channel has less than X messages

API_TOKEN = None
TOKEN_GROUP = None

with open("apitoken.txt") as f:
    API_TOKEN = f.read().strip()


with open("tokengroup.txt") as f:
    TOKEN_GROUP = f.read().strip()


def getRandomQuestion():
    questionFile = open("questions.txt", "r")
    content = questionFile.readlines()
    return content[rd.randint(0, len(content)-1)]
