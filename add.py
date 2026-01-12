def score_calcuator():
    """Calculate and return the score"""

    
    Maths = int(input("Enter your Maths score: "))
    Science = int(input("Enter your Science score: "))
    English = int(input("Enter your English score: "))

    length = 3

    average_score = (Maths + Science + English) / length
    return print(average_score)


    
score_calcuator()