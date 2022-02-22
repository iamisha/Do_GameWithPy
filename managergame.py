import random

def PlayGameLoop() -> (str, int):
    _name = None
    while _name is None:
        print("Enter your name:")
        _name = input().strip()
        if len(_name) <= 0: _name = None
        if _name is None: print("Invalid name, please enter again:")

    _score = 0
    while PlayRound():
        _score += 1

    print(f"Game finished. Your score is {_score}")
    return (_name, _score)

def PlayRound() -> bool:
    (_challenge, _solution) = GenQuestion()

    print(f'Challenge: {_challenge}')
    _input = GetInput()

    if _input == _solution:
        print("Correct answer!")
        return True
    else:
        print(f"Wrong answer, the correct one is {_solution}")
        return False

def GetInput():
    _result = None

    print("Input result")
    while _result is None:
        _input = input()
        try:    _result = int(_input)
        except: _result = None

        if _result is None:
            print("Input number only, please input result again")

    return _result

def GenQuestion() -> (str, int):

    _tokens = list()
    _tokens.append(str(random.randint(1, 9)))

    for i in range(1, 4):
        _tokens.append(('+', '-', '*', '/')[random.randint(0, 3)])
        _tokens.append(str(random.randint(1, 9)))
    
    _challenge = ' '.join(_tokens)
    _result = int(round(eval(_challenge)))

    return (_challenge, _result)