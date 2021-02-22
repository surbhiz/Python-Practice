from collections import Counter


def checkMagazine(magazine, note):
    return (Counter(note) - Counter(magazine)) == {}


print(checkMagazine("two times three is not four",
                    "two times thret"))
