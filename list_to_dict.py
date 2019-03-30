person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

answer = {i[0]:i[1] for i in person}

# Alternative:
# answer = dict(person)

print(answer)