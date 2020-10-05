__author__ = 'hap', 'aps'

"""
Author: Herat Alkeshkumar Patel (hp9198@rit.edu) , Ashesh Piyush Sheth (as2462@rit.edu)
"""

import turtle
import random
import math

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900


def init():
    """
    :pre: pos (0,0), heading (east), up
    :post: pos (-700,0), heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH, -WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_HEIGHT)
    turtle.title('Forest')
    turtle.setheading(0)
    turtle.up()
    turtle.setx(-700)
    turtle.speed(0)
    turtle.hideturtle()


def space():
    """
    moves 100 pixels forward on the ground
    :return: None
    """
    global flag
    if flag != 1:
        turtle.down()
    turtle.forward(100)


def house(height_wall):
    """
    draws a pentagon shaped house with the height provided and a 45 degree roof
    :param height_wall: height of the walls of the house
    :return: None
    """
    global lumber
    lumber = lumber + height_wall*(2+math.sqrt(2))
    turtle.down()
    turtle.forward(height_wall)
    turtle.left(90)
    turtle.forward(height_wall)
    turtle.left(45)
    turtle.forward((height_wall/2)*math.sqrt(2))
    turtle.left(90)
    turtle.forward((height_wall/2)*math.sqrt(2))
    turtle.left(45)
    turtle.forward(height_wall)

    turtle.left(90)
    turtle.up()
    turtle.forward(height_wall)
    space()


def trees():
    """
    Selects the type of tree and position of house(if wanted by user) randomly. Draws the trees and calls
    the house function.
    Also calls the star function once the trees and house are drawn
    :return: None
    """
    total_trees = int(num_tree)
    house_position = random.randint(0, total_trees-2)
    global lumber
    global max_height

    for tree in range(0, total_trees):
        turtle.down()
        turtle.left(90)
        turtle.forward(50)
        this_tree = random.randint(1, 3)

        if this_tree == 1:
            height_pine = random.randint(50, 200)
            lumber = lumber + height_pine
            if height_pine + ((math.sqrt(3) / 2)*60) > max_height:
                max_height = height_pine + ((math.sqrt(3) / 2)*60)
            turtle.forward(height_pine - 50)
            turtle.left(90)
            turtle.forward(30)
            for x in range(0, 2):
                turtle.right(120)
                turtle.forward(60)
            turtle.right(120)
            turtle.forward(30)
            turtle.sety(0)
            turtle.right(180)
            turtle.up()
            if tree != total_trees-1:
                space()
                if want_house.lower() == 'y' and tree == house_position:
                    house(100)

        elif this_tree == 2:
            height_maple = random.randint(50, 150)
            lumber = lumber + height_maple
            if height_maple + 60 > max_height:
                max_height = height_maple + 60
            turtle.forward(height_maple - 50)
            turtle.right(90)
            turtle.circle(30)
            turtle.sety(0)
            turtle.up()
            if tree != total_trees-1:
                space()
                if want_house.lower() == 'y' and tree == house_position:
                    house(100)

        else:
            height_apple = random.randint(50, 200)
            lumber = lumber + height_apple
            if height_apple + (math.sqrt(2)*60) > max_height:
                max_height = height_apple + (math.sqrt(2) * 60)
            turtle.forward(height_apple - 50)
            turtle.left(45)
            for x in range(0, 4):
                turtle.forward(60)
                turtle.right(90)
            turtle.sety(0)
            turtle.right(135)
            turtle.up()
            if tree != total_trees-1:
                space()
                if want_house.lower() == 'y' and tree == house_position:
                    house(100)

    star()


def star():
    """
    Draws a star above the last tree with its bottom 10 pixels higher than the highest tree
    :return: None
    """
    turtle.up()
    turtle.left(90)
    turtle.forward(max_height + 30)
    turtle.down()
    for i in range(0, 8):
        turtle.forward(10)
        turtle.backward(10)
        turtle.right(45)
    turtle.up()
    turtle.setx(0)


def day():
    """
    Prints the total lumber and height of the walls for new house. Calls house function with new height
    and also calls the sun function
    :return: None
    """
    print("We have " + str(lumber) + " units of lumber for building.")
    print("We will build a house with walls " + str(lumber/(2 + math.sqrt(2))) + " tall.")
    house(lumber / (2 + math.sqrt(2)))
    sun()


def sun():
    """
    Creates a sun beside and above the house
    :return: None
    """
    turtle.left(90)
    turtle.up()
    turtle.forward((lumber / (2 + math.sqrt(2))))
    turtle.down()
    turtle.circle(45)


def main():
    """
    calls the tree function to start drawing the night scene and when the user prompts,
    calls the day function
    :return:
    """
    init()
    trees()
    night_done = input("Night is done, press enter for day")
    global flag
    flag = 1
    if night_done == "":
        turtle.reset()
        turtle.hideturtle()
        day()

    m = input("Day is done, house is built, press enter to quit")
    if m == "":
        exit()


if __name__ == '__main__':
    num_tree = input("How many trees in your forest? ")
    want_house = input("Is there a house in the forest (y/n)? ")
    lumber = 0
    max_height = 0
    flag = 0
    main()
