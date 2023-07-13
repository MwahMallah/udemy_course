for i in range(1, 101):
    statement = ""
    
    if i % 3 == 0:
        statement += "Fizz"
    if i % 5 == 0:
        statement += "Buzz"
    if len(statement) == 0:
        statement = i

    print(statement)