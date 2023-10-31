import random
import json

def generate_readable_word(length):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    if length == 0:
        return ""

    word = ""
    if random.choice([True, False]):
        word += random.choice(consonants)
    else:
        word += random.choice(vowels)

    for _ in range(length - 1):
        if word[-1] in vowels:
            word += random.choice(consonants)
        else:
            word += random.choice(vowels)

    return word

def random_collection_collateral():
    collection_columns = []
    number_of_columns = random.randint(1, 10)
    if number_of_columns == 10:
        number_of_columns = random.randint(42, 99)

    data = {}
    for i in range(number_of_columns):
        column_name = generate_readable_word(random.randint(5, 12))
        collection_columns.append(column_name)
        data[column_name] = generate_readable_word(random.randint(10, 20))
        print(column_name + " added.")

    json_data = json.dumps(data)
    print(json_data)
    return json_data