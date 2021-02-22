voted = {}


def check_voters(name):
    if voted.get(name):
        print("Kick them out")
    else:
        voted[name] = True
        print("Let them vote")


check_voters("tom")
check_voters("Ajay")
check_voters("tom")
