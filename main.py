
bruno_data = {"name": "Bruno", "high": 168, "birthday": "2005-08-28", "zodiac": "virgo", "hobby": "play_VideoGames"}
sara_data = {"name": "Sara", "high": 160, "birthday": "2004-01-02", "zodiac": "capricorn", "hobby": "reed"}
anthony_data = {"name": "Anthony", "high": 193, "birthday": "2005-08-26", "zodiac": "virgo", "hobby": "play_VideoGames"}
person_dict = {"1107840789": anthony_data, "1109184020": sara_data, "1108965743": bruno_data}

print(person_dict)
print(person_dict["1107840789"])
print(person_dict["1107840789"]["hobby"])