import pygame
import sys
import pygame.font
from random import randint
pygame.init()
pygame.font.init()
pygame.mixer.init()
WIDTH = 1200
HEIGHT = 650
WHITE = (255, 255, 255)
FPS = 60
IMAGE_WIDTH, IMAGE_HEIGHT = 500, 250
BUTTON_WIDTH, BUTTON_HEIGHT = 180, 60
# images
# human
PAPER_IMAGE = pygame.image.load("image\imgpaperpp.png")
PAPER = pygame.transform.scale(PAPER_IMAGE, (IMAGE_WIDTH, IMAGE_HEIGHT))
SCISSORS_IMAGE = pygame.image.load("image\imgscissorspp.png")
SCISSORS = pygame.transform.scale(SCISSORS_IMAGE, (IMAGE_WIDTH, IMAGE_HEIGHT))
ROCK_IMAGE = pygame.image.load("image\imgrockpp.png")
ROCK = pygame.transform.scale(ROCK_IMAGE, (IMAGE_WIDTH, IMAGE_HEIGHT))
# user 1
PAPER_IMAGE1 = pygame.image.load("image\imgpaper1.png")
PAPER1 = pygame.transform.scale(PAPER_IMAGE1, (IMAGE_WIDTH, IMAGE_HEIGHT))
SCISSORS_IMAGE1 = pygame.image.load("image\imgscissors1.png")
SCISSORS1 = pygame.transform.scale(SCISSORS_IMAGE1, (IMAGE_WIDTH, IMAGE_HEIGHT))
ROCK_IMAGE1 = pygame.image.load("image\imgrock1.png")
ROCK1 = pygame.transform.scale(ROCK_IMAGE1, (IMAGE_WIDTH, IMAGE_HEIGHT))

# user 2
PAPER_IMAGE2 = pygame.image.load("image\imgpaper2.png")
PAPER2 = pygame.transform.scale(PAPER_IMAGE2, (IMAGE_WIDTH, IMAGE_HEIGHT))
SCISSORS_IMAGE2 = pygame.image.load("image\imgscissors2.png")
SCISSORS2 = pygame.transform.scale(SCISSORS_IMAGE2, (IMAGE_WIDTH, IMAGE_HEIGHT))
ROCK_IMAGE2 = pygame.image.load("image\imgrock2.png")
ROCK2 = pygame.transform.scale(ROCK_IMAGE2, (IMAGE_WIDTH, IMAGE_HEIGHT))

# robot
PAPER_IMAGE_BOT = pygame.image.load("image\imgpaperbot.png")
PAPER_BOT = pygame.transform.scale(PAPER_IMAGE_BOT, (IMAGE_WIDTH, IMAGE_HEIGHT))
SCISSORS_IMAGE_BOT = pygame.image.load("image\imgscissorsbot.png")
SCISSORS_BOT = pygame.transform.scale(SCISSORS_IMAGE_BOT, (IMAGE_WIDTH, IMAGE_HEIGHT))
ROCK_IMAGE_BOT = pygame.image.load("image\imgrockbot.png")
ROCK_BOT = pygame.transform.scale(ROCK_IMAGE_BOT, (IMAGE_WIDTH, IMAGE_HEIGHT))

HUMAN_IMAGE = pygame.image.load("image\imghuman.png")
HUMAN = pygame.transform.scale(HUMAN_IMAGE, (IMAGE_WIDTH - 180, IMAGE_HEIGHT - 170))
ROBOT_IMAGE = pygame.image.load("image\imgrobot.png")
ROBOT = pygame.transform.scale(ROBOT_IMAGE, (IMAGE_WIDTH - 180, IMAGE_HEIGHT - 170))
HUMAN_IMAGE1 = pygame.image.load("image\imguser1.png")
HUMAN1 = pygame.transform.scale(HUMAN_IMAGE1, (IMAGE_WIDTH - 180, IMAGE_HEIGHT - 170))
HUMAN_IMAGE2 = pygame.image.load("image\imguser2.png")
HUMAN2 = pygame.transform.scale(HUMAN_IMAGE2, (IMAGE_WIDTH - 180, IMAGE_HEIGHT - 170))

SCORE_IMAGE = pygame.image.load("image\score.png")
SCORE = pygame.transform.scale(SCORE_IMAGE, (IMAGE_WIDTH - 220, IMAGE_HEIGHT - 100))

WINNER_IMAGE = pygame.image.load("image\Winner.png")
WINNER = pygame.transform.scale(WINNER_IMAGE, (WIDTH//3, HEIGHT//2+ 150))

INSTRUCTION_IMAGE_WITH_ROBOT = pygame.image.load("image\instruction-with-robot.png")
INSTRUCTION_ROBOT = pygame.transform.scale(INSTRUCTION_IMAGE_WITH_ROBOT, (WIDTH, HEIGHT))

INSTRUCTION_IMAGE_WITH_HUMAN = pygame.image.load("image\instruction-2users.png")
INSTRUCTION_HUMAN = pygame.transform.scale(INSTRUCTION_IMAGE_WITH_HUMAN, (WIDTH, HEIGHT))

BACKGROUND_IMAGE = pygame.image.load("image\start-game.png")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))
END_BACKGROUND_IMAGE = pygame.image.load("image\end-game.png")
END_BACKGROUND = pygame.transform.scale(END_BACKGROUND_IMAGE, (WIDTH, HEIGHT))
MENU_IMAGE = pygame.image.load("image\menu.png")
MENU = pygame.transform.scale(MENU_IMAGE, (WIDTH, HEIGHT))

COMPUTER_MOVE = randint(1, 3)
COMPUTER_NAME = "ROBOT"
USER_NAME = "USER"
USER_1_NAME = 'USER1'
USER_2_NAME = 'USER2'

count_for_computer = 0
count_for_user = 0
count_for_player1 = 0
count_for_player2 = 0
MAX_HEALTH = 10
# sound
BACKGROUND_SOUND = pygame.mixer.music.load('sound\Background music.mp3')
# BACKGROUND_SOUND.set_volume(0.2)
CLICK_SOUND = pygame.mixer.Sound("sound\Button click sound.mp3")
# CLICK_SOUND.set_volume(1.0)

WINNER_SOUND = pygame.mixer.Sound('sound\Winner sound.mp3')
# WINNER_SOUND.set_volume(1.0)
# font
HEALTH_FONT = pygame.font.Font("font\Anzeigen Grotesk D Regular.otf", 100)
NAME_FONT = pygame.font.Font("font\Anzeigen Grotesk D Regular.otf", 40)
WINNER_FONT = pygame.font.Font("font\Anzeigen Grotesk D Regular.otf", 90)

# position
POSITION_LEFT = [-70, (HEIGHT // 2 - 150)]
POSITION_RIGHT = [(WIDTH - WIDTH//3 - 40), (HEIGHT // 2 - 150)]
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.music.play(-1)

class Button():
    def __init__(self, image, x_pos, y_pos):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
     
    def update(self):
        WIN.blit(self.image, self.rect)
        # WIN.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        else:
            return False
def draw_window():
    WIN.blit(BACKGROUND, (0,0))
    pygame.display.update()
# people turn
def print_paper():
    WIN.blit(PAPER, POSITION_LEFT)
    pygame.display.update()
def print_rock():
    WIN.blit(ROCK, POSITION_LEFT)
    pygame.display.update()
def print_scissors():
    WIN.blit(SCISSORS, POSITION_LEFT)
    pygame.display.update()
# bot turn
def print_paper_bot():
    WIN.blit(PAPER_BOT, POSITION_RIGHT)
    pygame.display.update()
def print_rock_bot():
    WIN.blit(ROCK_BOT, POSITION_RIGHT)
    pygame.display.update()
def print_scissors_bot():
    WIN.blit(SCISSORS_BOT, POSITION_RIGHT)
    pygame.display.update()
# user 1 turn
def print_paper_1():
    WIN.blit(PAPER1, POSITION_LEFT)
    pygame.display.update()
def print_rock_1():
    WIN.blit(ROCK1, POSITION_LEFT)
    pygame.display.update()
def print_scissors_1():
    WIN.blit(SCISSORS1, POSITION_LEFT)
    pygame.display.update()
# user 2 turn
def print_paper_2():
    WIN.blit(PAPER2, POSITION_RIGHT)
    pygame.display.update()
def print_rock_2():
    WIN.blit(ROCK2, POSITION_RIGHT)
    pygame.display.update()
def print_scissors_2():
    WIN.blit(SCISSORS2, POSITION_RIGHT)
    pygame.display.update()

# play again
def play():
    #GIAO DIỆN KHI ĐÃ CHƠI XONG 1 MÀN VÀ CÓ NGƯỜI CHIẾN THẮNG
    while True:
        # PLAY AGAIN
        load_back_button = pygame.image.load("image\play-again.png")
        load_back_button = pygame.transform.scale(load_back_button, (BUTTON_WIDTH +100, BUTTON_HEIGHT))
        back_button = Button(load_back_button, WIDTH//2, 2*HEIGHT//3 - BUTTON_HEIGHT// 2 + 15)

        # QUIT BUTTON
        load_exit_button = pygame.image.load("image\exit.png")
        load_exit_button = pygame.transform.scale(load_exit_button, (BUTTON_WIDTH, BUTTON_HEIGHT))
        exit_button = Button(load_exit_button, WIDTH//2, 2*HEIGHT//3 + BUTTON_HEIGHT)
        back_button.update()
        exit_button.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(pygame.mouse.get_pos()):
                    #NẾU ẤN VÀO BACK BUTTON SẼ QUAY TRỞ LẠI MENU CHÍNH ĐỂ NGƯỜI DÙNG CHỌN XEM CHƠI LẠI HAY QUIT
                    CLICK_SOUND.play()
                    option_screen()
                if exit_button.checkForInput(pygame.mouse.get_pos()):
                    #NẾU ẤN VÀO QUIT THÌ OUT TRÒ CHƠI
                    CLICK_SOUND.play()
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

# Option
def option_screen():
    while True:
        #HUMAN VS HUMAN BUTTON
        WIN.blit(MENU, (0, 0))
        button_surface = pygame.image.load("image\withfriend.png")
        button_surface = pygame.transform.scale(button_surface, (2*BUTTON_WIDTH, BUTTON_HEIGHT))
        button = Button(button_surface, WIDTH//2, HEIGHT//2+ 100)

        #HUMAN VS BOT BUTTON
        button_surface_2 = pygame.image.load("image\pp-comp.png")
        button_surface_2 = pygame.transform.scale(button_surface_2, (2*BUTTON_WIDTH, BUTTON_HEIGHT))
        button_2 = Button(button_surface_2, WIDTH//2, 3*HEIGHT//4 + BUTTON_HEIGHT//2)
        button.update()
        button_2.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_2.checkForInput(pygame.mouse.get_pos()):
                    CLICK_SOUND.play()
                    show_instruction_robot()
                    # main_button_2()
                if button.checkForInput(pygame.mouse.get_pos()):
                    CLICK_SOUND.play()
                    # main_button_1()
                    show_instruction_2users()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
# instruction of 2 user mode
def show_instruction_2users():
    while True:
        # OPTION BUTTON
        button_surface = pygame.image.load("image\start.png")
        button_surface = pygame.transform.scale(button_surface, (BUTTON_WIDTH, BUTTON_HEIGHT))
        button = Button(button_surface, WIDTH//2, HEIGHT- 65)
       
        WIN.blit(INSTRUCTION_HUMAN, (0, 0))
        button.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.checkForInput(pygame.mouse.get_pos()):
                    CLICK_SOUND.play()
                    main_button_1()
        pygame.display.update()

# instruction of robot mode
def show_instruction_robot():
    while True:
        # OPTION BUTTON
        button_surface = pygame.image.load("image\start.png")
        button_surface = pygame.transform.scale(button_surface, (BUTTON_WIDTH, BUTTON_HEIGHT))
        button = Button(button_surface, WIDTH//2, HEIGHT- 65)
       
        WIN.blit(INSTRUCTION_ROBOT, (0, 0))
        button.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.checkForInput(pygame.mouse.get_pos()):
                    CLICK_SOUND.play()
                    main_button_2()
        pygame.display.update()

def display_point(count_for_computer, count_for_user):
    WIN.blit(SCORE, (WIDTH//2 - IMAGE_WIDTH//2 + 110, HEIGHT - 170))
    computer_health = HEALTH_FONT.render(str(count_for_computer), 1, WHITE)
    user_health = HEALTH_FONT.render(str(count_for_user), 1, WHITE)
    WIN.blit(user_health, (WIDTH//2 - 110, HEIGHT - 140))
    WIN.blit(computer_health, (WIDTH//2 + 65, HEIGHT - 140))
    pygame.display.update()

    # Draw the names
    computer_name = NAME_FONT.render(COMPUTER_NAME, 1, WHITE)
    user_name = NAME_FONT.render(USER_NAME, 1, WHITE)
    WIN.blit(HUMAN, (30, HEIGHT - 100))
    WIN.blit(ROBOT, (WIDTH//2+250, HEIGHT - 100))
    WIN.blit(user_name, (155, HEIGHT - 80))
    WIN.blit(computer_name, (WIDTH//2+370, HEIGHT - 80))

def compare_to_print(user_input, computer_move):
    display_point(count_for_computer, count_for_user)
    draw_window()
    # computer move:
    if computer_move == 1:
        print_rock_bot()
    if computer_move == 2:
        print_paper_bot()
    if computer_move == 3:
        print_scissors_bot()

    # User move:
    if user_input[pygame.K_r]:
        print_rock()
    elif user_input[pygame.K_p]:
        print_paper()
    elif user_input[pygame.K_s]:
        print_scissors()
    pygame.display.update()

# 1 la rock, 2 la paper, 3 la scissor
def decide_winner(user_input, computer_move):
    global count_for_computer, count_for_user
    # user wins
    if user_input[pygame.K_r] and computer_move == 3 or \
        user_input[pygame.K_s] and computer_move == 2 or \
        user_input[pygame.K_p] and computer_move == 1:
        count_for_user += 1
    # computer wins
    elif computer_move == 1 and user_input[pygame.K_s] or \
        computer_move == 3 and user_input[pygame.K_p] or \
        computer_move == 2 and user_input[pygame.K_r]:
        count_for_computer += 1
    # tie
    elif user_input[pygame.K_r] and computer_move == 1 or \
        user_input[pygame.K_p] and computer_move == 2 or \
        user_input[pygame.K_s] and computer_move == 3  :
        pass
    else:
        display_instruction_with_robot()
        main_button_2()

def display_winner(winner_name):
    WINNER_SOUND.play()
    WIN.blit(END_BACKGROUND, (0, 0))
    WIN.blit(WINNER, (WIDTH//3, HEIGHT//6))
    text = NAME_FONT.render('The winner', 1, WHITE)
    WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT//3 - 50))
    # Draw the winner's name
    winner_text = WINNER_FONT.render(winner_name, 1, (100, 184, 212))
    WIN.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT//3))
    play()
    
    pygame.display.update()
    pygame.time.delay(1000)  # Wait for 1 second before closing the game
def main_button_2():
    global count_for_user, count_for_computer
    run = True
    draw_window()
    clock = pygame.time.Clock()
    user_input = None
    print_rock()
    print_rock_bot()
    while run:
        clock.tick(FPS)
        computer_move = randint(1, 3)
        for event in pygame.event.get():
            for i in range(10):
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if user_input is None:
                        user_input = pygame.key.get_pressed()
                        pygame.display.update()

            if user_input is not None:
                # print player's input out
                compare_to_print(user_input, computer_move)
                # counting the number of wining rounds of each player
                decide_winner(user_input, computer_move)
                display_point(count_for_computer, count_for_user)
                # print(f"count for user: {count_for_user}")
                # print(f"count for computer: {count_for_computer}")

                pygame.display.update()
                user_input = None
                pygame.display.update()

                if count_for_user == 10 or count_for_computer == 10:
                    if count_for_user == 10:
                        count_for_user = 0
                        count_for_computer = 0
                        display_winner(USER_NAME)
                    else:
                        count_for_user = 0
                        count_for_computer = 0
                        display_winner(COMPUTER_NAME)
                    # run = False
                pygame.display.update()

#FUNCTION IN RA ĐIỂM CỦA TỪNG NGƯỜI CHƠI
def display_point_option_2(count_for_player1, count_for_player2):
    WIN.blit(SCORE, (WIDTH//2 - IMAGE_WIDTH//2 + 110, HEIGHT - 170))
    user_1_health = HEALTH_FONT.render(str(count_for_player1), 1, WHITE)
    user_2_health = HEALTH_FONT.render(str(count_for_player2), 1, WHITE)
    WIN.blit(user_1_health, (WIDTH//2 - 110, HEIGHT - 140))
    WIN.blit(user_2_health, (WIDTH//2 + 65, HEIGHT - 140))
    pygame.display.update()

    # Draw the names
    user_1_name = NAME_FONT.render(USER_1_NAME, 1, WHITE)
    user_2_name = NAME_FONT.render(USER_2_NAME, 1, WHITE)
    WIN.blit(HUMAN1, (30, HEIGHT - 100))
    WIN.blit(HUMAN2, (WIDTH//2+250, HEIGHT - 100))
    WIN.blit(user_1_name, (155, HEIGHT - 80))
    WIN.blit(user_2_name, (WIDTH//2+370, HEIGHT - 80))
# 2: rock, 4: paper, 6: scissors
def compare_to_print_option_2(first_input, second_input):
    #FUNCTION IN RA MÀN HÌNH LỰA CHỌN MÀ NGƯỜI DÙNG NHẬP VÀO LÀ KÉO, BÚA HAY BAO (OPTION NGƯỜI VỚI NGƯỜI)
    display_point_option_2(count_for_player1, count_for_player2)
    draw_window()

    if first_input[pygame.K_r]:
        print_rock_1()
    if first_input[pygame.K_p]:
        print_paper_1()
    if first_input[pygame.K_s]:
        print_scissors_1()

    if second_input[pygame.K_2]:
        print_rock_2()
    if second_input[pygame.K_4]:
        print_paper_2()
    if second_input[pygame.K_6]:
        print_scissors_2()
    pygame.display.update()
# fUNCTION SO SÁNH INPUT CỦA NGƯỜI DÙNG XEM XEM AI LÀ NGƯỜI THẮNG
# ĐỒNG THỜI CỘNG 1 ĐIỂM CHO NGƯỜI THẮNG (OPTION NGƯỜI VỚI NGƯỜI)
def decide_winner_option_2(first_input, second_input):
    global count_for_player1, count_for_player2
    # player 1 wins
    if first_input[pygame.K_r] and second_input[pygame.K_6] or \
        first_input[pygame.K_p] and second_input[pygame.K_2] or \
        first_input[pygame.K_s] and second_input[pygame.K_4]:
        count_for_player1 += 1
    # tie
    elif first_input[pygame.K_r] and second_input[pygame.K_2] or \
        first_input[pygame.K_p] and second_input[pygame.K_4] or \
        first_input[pygame.K_s] and second_input[pygame.K_6]:
        pass
    # player 2 wins
    elif first_input[pygame.K_r] and second_input[pygame.K_4] or \
        first_input[pygame.K_p] and second_input[pygame.K_6] or \
        first_input[pygame.K_s] and second_input[pygame.K_2]   :
        count_for_player2 += 1
    # wrong input
    else:
        display_instruction_human()
        main_button_1()
#FUNCTION NẾU NGƯỜI DÙNG NHẬP SAI KÝ TỰ
def display_instruction_human():
    WIN.blit(INSTRUCTION_HUMAN, (0,0))
    
    pygame.display.update()
    pygame.time.delay(1000)
def display_instruction_with_robot():
    WIN.blit(INSTRUCTION_ROBOT, (0,0))
    
    pygame.display.update()
    pygame.time.delay(1000)
# GIAO DIỆN NGƯỜI CHƠI VỚI NGƯỜI
def main_button_1():
    global count_for_player1, count_for_player2
    run = True
    draw_window()
    clock = pygame.time.Clock()
    first_input = None
    second_input = None
    print_rock_1()
    print_rock_2()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if first_input is None:
                    first_input = pygame.key.get_pressed()
                elif second_input is None:
                    second_input = pygame.key.get_pressed()
                    pygame.display.update()
            if first_input is not None and second_input is not None:
                # print player's input out
                compare_to_print_option_2(first_input, second_input)
                # counting the number of wining rounds of each player
                decide_winner_option_2(first_input, second_input)
                display_point_option_2(count_for_player1, count_for_player2)
                # print(f"count for player 1: {count_for_player1}")
                # print(f"count for player 2: {count_for_player2}")
                pygame.display.update()
                first_input = None
                second_input = None
                pygame.display.update()

                if count_for_player1 == 10 or count_for_player2 == 10:
                    if count_for_player1 == 10:  
                        count_for_player1 = 0
                        count_for_player2 = 0
                        display_winner(USER_1_NAME)
                    if count_for_player2 == 10:
                        count_for_player1 = 0
                        count_for_player2 = 0
                        display_winner(USER_2_NAME)

                pygame.display.update()
    # pygame.quit()
if __name__ == "__main__":
    # main_menu()
    option_screen()
