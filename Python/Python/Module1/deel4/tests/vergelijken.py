def vergelijken(nr1, nr2):
    if nr1 > nr2:
        maximum, minimum = nr1, nr2
    elif nr1 < nr2:
        maximum, minimum = nr1, nr2
    else:
        print('Beide getallen zijn even groot')
        return nr1, nr2

    print(f'Maximum: {maximum} en minimum: {minimum}')
    return maximum, minimum