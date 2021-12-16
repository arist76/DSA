def domino_piler():
    dimensions = input('Enter you\'re dimensions:').split(' 5 ')
    M = int(dimensions[0])
    N = int(dimensions[1])
    square_area = M*N
    number_of_dominos = square_area//2
    print(number_of_dominos)


domino_piler()