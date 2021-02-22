heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

print(len(heros))
heros.append("black panther")
heros.remove("black panther")
heros.append("hulk")
print(heros)
for hero in heros:
    if hero == "thor":
        heros.remove("thor")
        heros.insert(1, "doctor strange")
    if hero == "hulk":
        heros.remove("hulk")
heros.insert(2, "doctor strange")
heros.insert(5, "doctor strange")
print(heros)
heros.sort()
print(heros)
