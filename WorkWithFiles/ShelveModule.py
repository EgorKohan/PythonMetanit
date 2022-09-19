import shelve

FILENAME = "states2"

with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"

with shelve.open(FILENAME) as states:
    print("London is capital of", states["London"])
    for state in states:
        print(states[state])

with shelve.open(FILENAME) as states:
    key = "Brussels"
    if key in states:
        print(states[key])
    else:
        print(key, "not found")

with shelve.open(FILENAME) as states:
    states["London"] = "United Kingdom"
    states["Brussels"] = "Belgium"
    for key in states:
        print(key, "-", states[key])

with shelve.open(FILENAME) as states:
    popped_elem = states.pop("London", "Not Found")
    print(popped_elem)

    del states["Madrid"]
    print("Madrid" in states.keys())
    