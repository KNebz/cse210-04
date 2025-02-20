import os
from pickle import FALSE
import random

from game.casting.actor import Actor
from game.casting.stone import Stone
from game.casting.cast import Cast
from game.casting.score import Score

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
#DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_STONES = 20


def main():
    
    # create the cast
    cast = Cast()
    
    # create the score score
    score = Score()
    position = Point(0, 0)
    #score.set_text("")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(position)
    cast.add_actor("score", score)
    
    # create the player
    x = int(MAX_X / 2)
    y = int(MAX_Y - (MAX_Y / 8))
    position = Point(x, y)

    player = Actor()
    player.set_text("⚒︎")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)
    characters = [42, 79]
    
    # with open(DATA_PATH) as file:
    #     data = file.read()
    #     messages = data.splitlines()

    for n in range(DEFAULT_STONES): #may not need
        text = chr(random.choice(characters))
        #message = message[n]

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, 5)
        position = position.scale(CELL_SIZE) 

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        # create the stones 
        stone = Stone()
        stone.set_text(text)
        stone.set_font_size(FONT_SIZE)
        stone.set_color(color)
        stone.set_position(position)
        #stone.set_message(message) #may not need
        cast.add_actor("stones", stone)

        
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service, COLS, ROWS, CELL_SIZE, FONT_SIZE)
    director.start_game(cast)


if __name__ == "__main__":
    main()