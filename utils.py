from constants import *

# Print function that mergers all lines into a single one

def pm(lines: list):
    output = ""
    for line in lines:
        output += line
    print(output)


# Print function that prints all lines seperatly

def pl(lines: list):
    for line in lines:
        print(line)

# Text function to format a text in the proper colorized way

def ct(text, color, endColor=END_COLOR): return f"{color}{text}{endColor}"
def RED(text): return ct(text,COLOR_RED)
def PURPLE(text): return ct(text,COLOR_PURPLE)
def GREEN(text): return ct(text,COLOR_GREEN)
def BLUE(text): return ct(text,COLOR_BLUE)
def CYAN(text): return ct(text,COLOR_CYAN)