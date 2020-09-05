
import sys

sampleBoard = {
    'topleft': '1', 'topmiddle': '2', 'topright': '3',
    'left': '4', 'middle': '5', 'right': '6',
    'botleft': '7', 'botmiddle': '8', 'botright': '9',
}

theBoard = {
    'topleft': ' ', 'topmiddle': ' ', 'topright': ' ',
    'left': ' ', 'middle': ' ', 'right': ' ',
    'botleft': ' ', 'botmiddle': ' ', 'botright': ' ',
}

def BoardPrint(**kwargs):
    print(kwargs['topleft'] + '|' + kwargs['topmiddle'] + '|' + kwargs['topright'])
    print('-+-+-')
    print(kwargs['left'] + '|' + kwargs['middle'] + '|' + kwargs['right'])
    print('-+-+-')
    print(kwargs['botleft'] + '|' + kwargs['botmiddle'] + '|' + kwargs['botright'])

def isWin(turn, **kwargs):
    if (kwargs['topleft'] == kwargs['topmiddle'] == kwargs['topright'] == turn or
        kwargs['left'] == kwargs['middle'] == kwargs['right'] == turn or
        kwargs['botleft'] == kwargs['botmiddle'] == kwargs['botright'] == turn or
        kwargs['topleft'] == kwargs['left'] == kwargs['botleft'] == turn or
        kwargs['topmiddle'] == kwargs['middle'] == kwargs['botmiddle'] == turn or
        kwargs['topright'] == kwargs['right'] == kwargs['botright'] == turn or
        kwargs['topleft'] == kwargs['middle'] == kwargs['botright'] == turn or
        kwargs['topright'] == kwargs['middle'] == kwargs['botleft'] == turn):
        return True
    else:
        return False


if __name__ == '__main__':
    BoardPrint(**sampleBoard)
    turn = 'X'
    i = 9
    while i > 0:
        print(i)
        if turn == 'X':
            print('X turn...')
        else:
            print('O turn...')
        choose = input('Move on which space? ')
        pos = choose
        for k,v in sampleBoard.items():
            if choose == v:
                pos = k
                if theBoard[pos] != ' ':
                    print('you can not take this position...')
                    break
                theBoard[pos] = turn
                if isWin(turn, **theBoard):
                    BoardPrint(**theBoard)
                    sys.exit(turn + 'Win...')
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
                i -= 1
                break
        BoardPrint(**theBoard)
    print('draw')
    exit()
