from tkinter import *
master = Tk()
import pandas as pd

triangle_size  = 0.1
cell_score_min = -10
cell_score_max = 10
Width   = 50
( x , y ) = ( 12 , 12 )
actions   = [ "up" , "down" , "left" , "right" ]

board       = Canvas ( master, width = x * Width , height = y * Width )
player      = ( 1 , y - 2 )
score       = 0
restart     = False
data        = pd.read_csv ( "DataTugasML3.txt" , delimiter = '\t' )
totalReward = []
hasilReward = []
asd         = []
for i in range ( data.shape [ 0 ] ):
    reward  = []
    rewardd = []
    for j in range(data.shape[1]):
        reward.append  ( float ( data [ str ( i ) ][ j : j + 1 ] ) / 100000 )
        rewardd.append ( float ( data [ str ( i ) ][ j : j + 1 ] ) )
    totalReward.append ( reward )
    hasilReward.append ( rewardd )

def walkReward ( totalReward , x , y ):
    if ( x >= 0 and x <= 9 ) and ( y >= 0 and y <= 9 ):
        return totalReward [ x ] [ y ]
    else:
        return -999
walls       = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(11,1),(11,2),(11,3),(11,4),(11,5),(11,7),(11,6),(11,8),(11,9),(11,10),(11,11),(10,11),(9,11),(8,11),(7,11),(6,11),(5,11),(4,11),(3,11),(2,11),(1,11)]
specials    = [ ( 10 , 1 , "green" , 100 ) ]
cell_scores = {}



def create_triangle ( i , j , action ):
    if action == actions [ 0 ]:
        return board.create_polygon ( ( i + 0.5 - triangle_size ) * Width , ( j + triangle_size ) * Width ,
                                    ( i + 0.5 + triangle_size ) * Width , ( j + triangle_size ) * Width ,
                                    ( i + 0.5 ) * Width , j * Width,
                                    fill = "white" , width=1)
    elif action == actions [ 1 ]:
        return board.create_polygon ( ( i + 0.5 - triangle_size ) * Width , ( j + 1 - triangle_size ) * Width ,
                                    ( i + 0.5 + triangle_size ) * Width , ( j + 1 - triangle_size ) * Width ,
                                    ( i + 0.5 ) * Width , ( j + 1 ) * Width ,
                                    fill = "white" , width = 1 )
    elif action == actions [ 2 ]:
        return board.create_polygon ( ( i + triangle_size ) * Width , ( j + 0.5 - triangle_size ) * Width ,
                                    ( i + triangle_size ) * Width , ( j + 0.5 + triangle_size ) * Width ,
                                    i * Width , ( j + 0.5 ) * Width ,
                                    fill = "white" , width = 1 )
    elif action == actions [ 3 ]:
        return board.create_polygon ( ( i + 1 - triangle_size ) * Width , ( j + 0.5 - triangle_size ) * Width ,
                                    ( i + 1 - triangle_size ) * Width , ( j + 0.5 + triangle_size ) * Width ,
                                    ( i + 1 ) * Width , ( j + 0.5 ) * Width ,
                                    fill = "white" , width = 1 )

def render_grid():
    global specials , walls , Width , x , y , player
    for i in range ( x ):
        for j in range ( y ):
            board.create_rectangle ( i * Width , j * Width , ( i + 1 ) * Width , ( j + 1 ) * Width , fill = "white" , width = 1 )
            temp = {}
            for action in actions:
                temp [ action ] = create_triangle ( i , j , action )
            cell_scores [ ( i , j ) ] = temp
    for ( i , j , c , w ) in specials:
        board.create_rectangle ( i * Width , j * Width , ( i + 1 ) * Width , ( j + 1 ) * Width , fill = c , width = 1 )
    for ( i , j ) in walls:
        board.create_rectangle ( i * Width , j * Width , ( i + 1 ) * Width , ( j + 1 ) * Width , fill = "black" , width = 1 )

render_grid()


def set_cell_score ( state , action , val ):
    global cell_score_min , cell_score_max
    triangle = cell_scores [ state ] [ action ]
    green_dec = int ( min ( 255 , max ( 0 , ( val - cell_score_min ) * 255.0 / ( cell_score_max - cell_score_min ) ) ) )
    green = hex ( green_dec ) [ 2 : ]
    red = hex ( 255 - green_dec ) [ 2 : ]
    if len ( red ) == 1:
        red += "0"
    if len ( green ) == 1:
        green += "0"
    color = "#" + red + green + "00"
    board.itemconfigure ( triangle , fill = color )


def findScore ( data , hasilReward ):
    sum = 0
    for i in range ( len ( data ) ):
        if ( data [ i ] [ 0 ] >= 0 and data [ i ] [ 0 ] <= 9 ) and ( data [ i ] [ 1 ] >= 0 and data [ i ] [ 1 ] <= 9 ):
            sum += hasilReward [ data [ i ] [ 0 ] ] [ data [ i ] [ 1 ] ]
    return sum

def try_move ( dx , dy ):
    global player , x , y , score , totalReward , me, restart , asd , hasilReward
    if restart == True:
        restart_game()
    if ( player [ 0 ] + dx != -1 or player [ 0 ] + dx != 10 or player [ 1 ] + dy != -1 or player [ 1 ] + dy != -1 ):
        new_x = player [ 0 ] + dx
        new_y = player [ 1 ] + dy
        asd.append ( [ new_x - 1 , new_y - 1 ] )
        if ( new_x == 9 and new_y == 8 ):
            score += -0.03
        score += walkReward ( totalReward , new_x -1 , new_y -1 )
        if ( new_x > -1 ) and ( new_x < x ) and ( new_y > -1 ) and ( new_y < y ) and not ( ( new_x , new_y ) in walls ):
            board.coords ( me , new_x * Width + Width * 2 / 10 , new_y * Width + Width * 2 / 10, new_x * Width + Width * 8 / 10 , new_y * Width + Width * 8 / 10 )
            player = ( new_x , new_y )
        for ( i , j , c , w ) in specials:
            if new_x == i and new_y == j:
                score += walkReward ( totalReward , i - 1 , j - 1 ) #find score nya do pake index dijumlahin
                print ("Success! score: ", findScore( asd , hasilReward ) )
                restart = True
                asd     = []
                return
        #print "score: ", score


def call_up  ( event  ):
    try_move ( 0 , -1 )


def call_down ( event ):
    try_move  ( 0 , 1 )


def call_left ( event  ):
    try_move  ( -1 , 0 )


def call_right ( event ):
    try_move   ( 1 , 0 )


def restart_game():
    global player , score , me , restart
    player  = ( 1 , y - 2 )
    score   = 1
    restart = False
    board.coords ( me , player [ 0 ] * Width + Width * 2 / 10 , player [ 1 ] * Width + Width * 2 / 10 , player [ 0 ] * Width + Width * 8 / 10 , player [ 1 ] * Width + Width * 8 / 10 )

def has_restarted():
    return restart

master.bind ( "<Up>"    , call_up   )
master.bind ( "<Down>"  , call_down )
master.bind ( "<Right>" , call_right)
master.bind ( "<Left>"  , call_left )

me = board.create_rectangle ( player [ 0 ] * Width + Width * 2 / 10 , player [ 1 ] * Width + Width * 2 / 10 ,
                            player [ 0 ] * Width + Width * 8 / 10 , player [ 1 ] * Width + Width * 8 / 10 , fill = "orange" , width = 1 , tag = "me" )

board.grid ( row = 0 , column = 0 )


def start_game():
    master.mainloop()