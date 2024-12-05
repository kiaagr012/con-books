import pgzrun
from random import randint
from time import time

WIDTH =  800
HEIGHT = 600

books = []
lines = []
next_book = 0

start_time = 0
total_time = 0
end_time = 0

num_books = 8

def create_books():
    global start_time
    for count in range(0, num_books):
        book = Actor('books')
        book.pos = randint(40,WIDTH-40) , randint(40,HEIGHT-40)
        books.append(books)
    start_time = time()


def draw():
    global total_time
    screen.blit('home', (0,0))
    number = 1
    for book in books:  
        screen.draw.text(str(number), (book.pos[0], book.pos[1]+20))
        book.draw()
        number = number +1
    
    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_book< num_books:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)

def update():
    pass

def on_mouse_down(pos):
    global next_book, lines
    if next_book<num_books:
        if books[next_book].collidepoint(pos):
            if next_book:
                lines.append(books[next_book-1].pos, books[next_book].pos)
            next_book = next_book+1
        else:
            lines = []
            next_book = 0

create_books()

pgzrun.go()