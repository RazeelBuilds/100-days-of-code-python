#You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:
true_str = "true"
love_str = "love"

def calculate_love_score(name1,name2):
    true_count = 0
    love_count = 0
    name_add = (name1 + name2).lower()
    for char in true_str:
        true_count += name_add.count(char)
    for char in love_str:
        love_count += name_add.count(char)
    love_score = str(true_count) + str(love_count)
    print(love_score)
calculate_love_score(name1="Kanye West",name2="Kim Kardashian")
