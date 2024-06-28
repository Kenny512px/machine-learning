import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
hangman_status = 0
words = ["DEVELOPER", "PYTHON", "PROGRAMMING", "HANGMAN", "PYGAME"]
word = random.choice(words)
guessed = []

# Setup button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
   x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
   y = starty + ((i // 13) * (GAP + RADIUS * 2))
   letters.append([x, y, chr(A + i), True])

# Drawing hangman function
def draw_hangman(status):
   if status >= 1:
       pygame.draw.line(win, BLACK, (150, 500), (400, 500), 10)  # Base
   if status >= 2:
       pygame.draw.line(win, BLACK, (275, 500), (275, 150), 10)  # Pole
   if status >= 3:
       pygame.draw.line(win, BLACK, (275, 150), (400, 150), 10)  # Top bar
   if status >= 4:
       pygame.draw.line(win, BLACK, (400, 150), (400, 200), 10)  # Rope
   if status >= 5:
       pygame.draw.circle(win, BLACK, (400, 250), 50, 10)  # Head
   if status >= 6:
       pygame.draw.line(win, BLACK, (400, 300), (400, 400), 10)  # Body
   if status >= 7:
       pygame.draw.line(win, BLACK, (400, 400), (350, 450), 10)  # Left leg
   if status >= 8:
       pygame.draw.line(win, BLACK, (400, 400), (450, 450), 10)  # Right leg
   if status >= 9:
       pygame.draw.line(win, BLACK, (400, 350), (350, 300), 10)  # Left arm
   if status >= 10:
       pygame.draw.line(win, BLACK, (400, 350), (450, 300), 10)  # Right arm

# Load game images
def draw():
   win.fill(WHITE)
   text = TITLE_FONT.render("HANGMAN", 1, BLACK)
   win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

   # Draw word
   display_word = ""
   for letter in word:
       if letter in guessed:
           display_word += letter + " "
       else:
           display_word += "_ "
   text = WORD_FONT.render(display_word, 1, BLACK)
   win.blit(text, (400, 200))

   # Draw buttons
   for letter in letters:
       x, y, ltr, visible = letter
       if visible:
           pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
           text = LETTER_FONT.render(ltr, 1, BLACK)
           win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

   # Draw hangman
   draw_hangman(hangman_status)

   pygame.display.update()

def display_message(message):
   pygame.time.delay(1000)
   win.fill(WHITE)
   text = WORD_FONT.render(message, 1, BLACK)
   win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
   pygame.display.update()
   pygame.time.delay(3000)

def main():
   global hangman_status

   clock = pygame.time.Clock()
   run = True

   while run:
       clock.tick(60)

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False
           if event.type == pygame.MOUSEBUTTONDOWN:
               m_x, m_y = pygame.mouse.get_pos()
               for letter in letters:
                   x, y, ltr, visible = letter
                   if visible:
                       dis = ((x - m_x) ** 2 + (y - m_y) ** 2) ** 0.5
                       if dis < RADIUS:
                           letter[3] = False
                           guessed.append(ltr)
                           if ltr not in word:
                               hangman_status += 1

       draw()

       won = True
       for letter in word:
           if letter not in guessed:
               won = False
               break

       if won:
           display_message("YOU WON!")
           break

       if hangman_status == 10:
           display_message("YOU LOST!")
           break

while True:
   main()

pygame.quit()
