groceries = {"chicken": 8, "apples": 6, "cucumbers": 3,
             "milk": 2, "oranges": 4}
x = groceries.pop("oranges")

print(groceries)

speakers = {"Sir Rafael": 54, "Ms. Joan": 33, "Ms. Dana": 67}

y = speakers.keys()

print(y)

swimming_team_tryout = {"Carl": "passed", "Quentine": "failed", "John Y.": "passed",
                        "Peter": "failed", "Max T.": "passed", "Joseph": "passed",
                        "Jone": "failed", "Jorge": "failed", "George": "passed",
                        "Ben": "passed", "Jerome": "passed", "Rick": "failed",
                        "Max G.": "failed", "john P.": "failed", "Vince": "passed"}

stt = swimming_team_tryout.get("Jorge")

print(stt)
