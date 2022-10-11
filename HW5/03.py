# # Создайте программу для игры в ""Крестики-нолики""

# import pygame

# # size = (600,400)
# # pygame.display.set_mode(size)

# pygame.display.set_mode((600,400)) # размер дисплея
# pygame.display.set_caption('TIC TAC TOE') # название
# # img = pygame.image.load('photo.png')
# # pygame.display.set_icon(img)            изменить иконку

# # while True:       # запустить прогу просто для наглядности изменений
# #    pass           # (не будет отвечать т.к. нет игрововго алгоритма)

# # можно так, тогда с окном можно взаимодействовать

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             quit()

import sys
import pygame

# функция поиска выигрыша
def check_win(mas,sign): # массив и знак
    zeroes = 0
    for row in mas:
        zeroes+=row.count(0) # для ничьей,проверка на пустые клетки
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col]==sign and mas[1][col]==sign and mas[2][col]==sign:
            return sign
    if mas[0][0]==sign and mas[1][1]==sign and mas[2][2]==sign:
        return sign
    if mas[0][2]==sign and mas[1][1]==sign and mas[2][0]==sign: # диагональ справа верх налева вниз
        return sign
    if zeroes==0:
        return 'Piece'
    return False

# отрисовка деталей цветами (пока что)
pygame.init()
size_block = 250 # блок
margin = 35 # отступ
width = height = size_block*3 + margin*4 # формула высчитывания дисплея

size_window = (width,height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('TIC TAC TOE')

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
mas = [[0]*3 for i in range (3)] # массив заполненный нулями, обозначающими то, что клетка пустая
query = 0   # целочисленные переменные, множество целых чисел (будем постепенно увеличивать на 1)
            # проверкой четность и нечетность можно задать чередование ходов игроков
game_over = False # для того, чтобы после окончания нельзя было тыкать на тоже поле (+69 +81 строки)

while True:  # цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
####        elif event.type == pygame.MOUSEBUTTONDOWN: # если событие - это нажатие кнопки
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over: # реагируем на нажатие мыши,пока игра не закончена
            x_mouse, y_mouse = pygame.mouse.get_pos() # координаты мышки
            col = x_mouse // (size_block+margin) # находим строчку в которой находится мышка
            row = y_mouse // (size_block+margin) # находим столбец
            # проверка на то, пустая ли ячейка (т.е. 0 ли в ней)
            if mas[row][col] == 0:
####            mas[row][col] = 'x' # пока будем заносить крестик в массив с такими координатами
                if query%2 == 0: # проверка на четность и нечетность для определения игрока
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query+=1 # увеличить переменную для цикла

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # рестарт игры при нажатии пробела
            game_over = False
            mas = [[0]*3 for i in range(3)]
            query=0
            screen.fill(black)

    if not game_over: # отрисовка блоков пока игра не закончен
        for row in range(3): # цикл, который обходит кол-во строк и столбцов
            for col in range(3): # три столбца, три строки
                # делаем проверку положения маус для изменения цвета
                if mas[row][col] == 'x':
                    color = red
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white

                x = col*size_block + (col+1)*margin # поиск координаты для верхнего левого угла квадрата
                y = row*size_block + (row+1)*margin
    ####            pygame.draw.rect(screen,white, (x,y,size_block,size_block)) # нарисовать на экране белым цветом (координаты первого, размеры правого нижнего угла(второго)) (противоположные квадраты)
                pygame.draw.rect(screen,color,(x,y,size_block,size_block)) # поменяли white на переменную color
        if (query-1)%2==0: # так как в 78 строке увеличивали
            game_over = check_win(mas,'x') # прописываем, что возвращаем
        else:
            game_over = check_win(mas,'o')

        if game_over: # непустая строка
            screen.fill(black) # закраска экрана
            font = pygame.font.SysFont('stxingkai', 80) # шрифт
            text1 = font.render(game_over,True, white) # текст будет содержать GO белым цветом
            text_rect = text1.get_rect() # задаем координаты
            # две строчки, которые находят центр экрана
            text_x = screen.get_width() /2 - text_rect.width/2
            text_y = screen.get_height() /2 - text_rect.height/2
            # строка, прикрепляющая текст к заданным координатам
            screen.blit(text1,[text_x, text_y])
        
        pygame.display.update() # чтобы на экране отобразились изменения