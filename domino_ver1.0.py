import random
from operator import itemgetter

domino_snake = []

def dealing():
    for no1 in range (0, 7):
        for no2 in range(0 + no1, 7):
            piece = [no1, no2]
            stock_pieces.append(piece)

    for deal in range(0, 14):
        piece = (random.choice(stock_pieces))
        stock_pieces.remove(piece)
        if deal %2 == 0:
            computer_pieces.append(piece)
        else:
            player_pieces.append(piece)


def first_move():

    doubles = [[6,6], [5,5], [4,4], [3,3], [2,2], [1,1], [0,0]]

    for piece in doubles:
        if piece not in stock_pieces:
            domino_snake.append(piece)
            if piece in computer_pieces:
                computer_pieces.remove(piece)
                global status
                status = "player"
                break
            else:
                player_pieces.remove(piece)
                status = "computer"
                break
            print("rozdajemy ponownie")


def playing_field():
    
    print("=" * 70)
    print(f"Stock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(computer_pieces)}\n")
    if len(domino_snake) > 6:
        print(f"{domino_snake[0]}{domino_snake[1]}{domino_snake[2]}...{domino_snake[-3]}{domino_snake[-2]}{domino_snake[-1]}")
    else:
        for i in domino_snake:
            print(i, end="")
        
    print("\n\nYour pieces:")
    for count, piece in enumerate(player_pieces):
        print(f"{count + 1}: {piece}")


def weighting_CP():
    
    list_to_count = []
    pieces_to_count = []
    
    list_to_count = domino_snake + computer_pieces
    
    for pieces in list_to_count:
        for piece in pieces:
            pieces_to_count.append(piece)
    
    zero = pieces_to_count.count(0)
    one = pieces_to_count.count(1)
    two = pieces_to_count.count(2)
    three = pieces_to_count.count(3)
    four = pieces_to_count.count(4)
    five = pieces_to_count.count(5)
    six = pieces_to_count.count(6)

    for piece in computer_pieces:
        weight = 0
        for number in piece:
            if number == 0:
                weight += zero
            elif number == 1:
                weight += one
            elif number == 2:
                weight += two
            elif number == 3:
                weight += three
            elif number == 4:
                weight += four
            elif number == 5:
                weight += five
            elif number == 6:
                weight += six
        piece.append(weight)

    computer_pieces.sort(key=itemgetter(2), reverse = True)
    
    for elem in computer_pieces:
        elem.remove(elem[2])


def computer_AI():

    global status
    global piece
    
    for piece in computer_pieces:
        if (piece[0] == domino_snake[0][0]) or (piece[1] == domino_snake[0][0]):
            if piece[1] != domino_snake[0][0]:
                change()
                domino_snake.insert(0, piece)
            else:
                domino_snake.insert(0, piece)
            computer_pieces.remove(piece)
            status = "player"
            break
        elif (piece[0] == domino_snake[-1][-1]) or (piece[1] == domino_snake[-1][-1]):
            if piece[0] != domino_snake[-1][-1]:
                change()
                domino_snake.append(piece)
            else:
                domino_snake.append(piece)
            computer_pieces.remove(piece)
            status = "player"
            break
        
    while status == "computer":
        if len(stock_pieces) > 0:
            piece = random.choice(stock_pieces)
            stock_pieces.remove(piece)
            computer_pieces.append(piece)
        status = "player"


def change():

    end = piece[0]
    piece[0] = piece[1]
    piece[1] = end


def taking_turns():

    global status
    global piece

    if status == "player":
        print("\nStatus: It's your turn to make a move. Enter your command.")
        order = input()
        try:
            int(order)
            if abs(int(order)) > len(player_pieces):
                print("Invalid input. Please try again.")
            elif int(order) == 0:
                if len(stock_pieces) > 0:
                    piece = random.choice(stock_pieces)
                    stock_pieces.remove(piece)
                    player_pieces.append(piece)
                status = "computer"
            else:
                piece = player_pieces[abs(int(order))-1]
                if int(order)< 0:
                    if (piece[0] == domino_snake[0][0]) or (piece[1] == domino_snake[0][0]):
                        if piece[1] != domino_snake[0][0]:
                            change()
                            domino_snake.insert(0, piece)
                        else:
                            domino_snake.insert(0, piece)
                        status = "computer"
                        player_pieces.remove(piece)
                    else:
                        print("Illegal move. Please try again.")
                elif (int(order) > 0):
                    if (piece[0] == domino_snake[-1][-1]) or (piece[1] == domino_snake[-1][-1]):
                        if piece[0] != domino_snake[-1][-1]:
                            change()
                            domino_snake.append(piece)
                        else:
                            domino_snake.append(piece)
                        status = "computer"
                        player_pieces.remove(piece)
                    else:
                        print("Illegal move. Please try again.")
                
        except ValueError:
            print("Invalid input. Please try again.")
    
    elif status == "computer":
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
        input()
        weighting_CP()
        computer_AI()


def end_game():
    global game
    
    if len(computer_pieces) == 0:
        playing_field()
        print("Status: The game is over. The computer won!")
        game = False
    elif len(player_pieces) == 0:
        playing_field()
        print("Status: The game is over. You won!")
        game = False
    elif domino_snake[0][0] == domino_snake[-1][-1]:
        global count
        count = 0
        for stone in domino_snake:
            for element in stone:
                if element == domino_snake[0][0]:
                    count += 1
        if count == 8:
            playing_field()
            print("Status: The game is over. It's a draw!")
            game = False


while len(domino_snake) == 0:
    stock_pieces = []
    computer_pieces = []
    player_pieces = []
    dealing()
    first_move()


game = True
while game:
    playing_field()
    taking_turns()
    end_game()
