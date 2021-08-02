
from tkinter import *
import time
from copy import deepcopy
from itertools import chain
import random


class Graphics:
   def __init__(self):
       self.board = None  # יצביע לcanvas שעליו נוצרת הגרפיקה
       self.tri_array = []  # מכיל את כל המשולשים שבתוך כל הריבועים
       self.size = 4
       self.square_size = 100
       self.options()

   def options(self):  # הפעולה בונה את לוח האופציות ומציבה בחירה בין משחק של שני שחקנים לבין משחק נגד המחשב
       self.optionss = Label(root, text="OPTIONS", bg="pink", font="Comicsansms 40 bold italic")
       self.optionss.place(x=175, y=10)
       self.line1 = Label(root, bg="pink",
                          text="--------------------------------------------------------------------------------------------------------------------")
       self.line1.place(x=0, y=75)
       self.choice = Label(root, text="Click on the gamemode of your choice: ", bg="pink", font="Comicsansms 10")
       self.choice.place(x=175, y=100)
       self.two = Button(root, text="Two Players", bg="pink", font="Comicsansms 10")
       self.two.bind('<Button-1>', lambda event, choice=1: self.post_choice(event, choice))
       self.two.place(x=100, y=131)
       self.or1 = Label(root, text="OR", bg="pink", font="Comicsansms 20 bold italic")
       self.or1.place(x=270, y=131)
       self.comp = Button(root, text="Against Computer", bg="pink", font="Comicsansms 10")
       self.comp.bind('<Button-1>', lambda event, choice=2: self.post_choice(event, choice))
       self.comp.place(x=400, y=131)
       self.line2 = Label(root, bg="pink",
                          text="--------------------------------------------------------------------------------------------------------------------")
       self.line2.place(x=0, y=160)

   def post_choice(self, event, choice):  # הפעולה נותנת בחירה לגודל הלוח וקוראת לפעולה הבאה לפי הבחירה של הgamemode
       self.game_mode_choice = choice
       self.square_amount = Label(root, text="Choose the amount of squares: ", bg="pink", font="Comicsansms 10")
       self.square_amount.place(x=205, y=190)
       self.amount = Spinbox(root, bg="pink", from_=3, to=10)
       self.amount.grid(row=1, column=0)
       self.amount.place(x=200, y=221)
       self.clickk = Label(root, text="Enter", bg="pink", font="Comicsansms 16")
       self.clickk.place(x=350, y=215)
       self.two.unbind('<Button-1>')
       self.comp.unbind('<Button-1>')
       if choice == 1:
           self.two.config(bg="thistle1")
           self.clickk.bind('<Button-1>', lambda event: self.two_players(event))
       if choice == 2:
           self.comp.config(bg="thistle1")
           self.clickk.bind('<Button-1>', lambda event: self.computer(event))
       self.line3 = Label(root, bg="pink",
                          text="--------------------------------------------------------------------------------------------------------------------")
       self.line3.place(x=0, y=250)

   def two_players(self, event):  # הפעולה שומרת את הגודל של הלוח וקוראת לפעולת בחירת הצבעים
       self.size = int(self.amount.get()) + 1
       self.clickk.unbind('<Button-1>')
       self.Colors = Label(root, text="COLORS", bg="pink", font="Comicsansms 40 bold italic")
       self.Colors.place(x=175, y=270)
       root.update()
       self.select_colors()

   def computer(self, event):  # הפעולה שומרת את הגודל של הלוח ופותחת אופציות לבחירת הצבעים
       self.size = int(self.amount.get()) + 1
       self.clickk.unbind('<Button-1>')
       self.Colors = Label(root, text="COLORS", bg="pink", font="Comicsansms 40 bold italic")
       self.Colors.place(x=175, y=270)
       self.colors1 = Listbox(root, selectmode=SINGLE, bg="pink", font="Comicsansms 10", width=40)
       self.colors1.insert(0, "BROWN")
       self.colors1.insert(1, "BLUE")
       self.colors1.insert(2, "GREEN")
       self.colors1.insert(3, "YELLOW")
       self.colors1.insert(4, "PURPLE")
       self.colors1.insert(5, "WHITE")
       self.colors1.insert(6, "BLACK")
       self.colors1.insert(7, "ORANGE")
       self.colors1.insert(8, "GRAY")
       self.colors1.place(x=105, y=380)
       self.colors1.select_set(0)
       self.player_one_color = self.colors1.get(self.colors1.curselection())
       self.select1 = Button(root, text="SELECT", bg="pink",
                             command=self.selected_color_comp)
       self.select1.place(x=135, y=560)

   def selected_color_comp(self):  # הפעולה קולטת את בחירת המשתמש ובוחרת צבע למחשב
       self.player_one_color = self.colors1.get(self.colors1.curselection())
       self.player_two_color = "light blue"
       self.board1_destroy()
       self.create_board(2)

   def select_colors(self):  # בשני שחקנים- בחירת הצבע של השחקן הראשון
       self.player_one_ = Label(root, text="Player one, select a color: ", bg="pink", font="Comicsansms 10")
       self.player_one_.place(x=100, y=355)
       self.colors1 = Listbox(root, selectmode=SINGLE, bg="pink", font="Comicsansms 10")
       self.colors1.insert(0, "BROWN")
       self.colors1.insert(1, "BLUE")
       self.colors1.insert(2, "GREEN")
       self.colors1.insert(3, "YELLOW")
       self.colors1.insert(4, "PURPLE")
       self.colors1.insert(5, "WHITE")
       self.colors1.insert(6, "BLACK")
       self.colors1.insert(7, "ORANGE")
       self.colors1.insert(8, "GRAY")
       self.colors1.insert(9, "LIGHT BLUE")
       self.colors1.place(x=105, y=380)
       self.colors1.select_set(0)
       self.player_one_color = self.colors1.get(self.colors1.curselection())
       self.select1 = Button(root, text="SELECT", bg="pink",
                             command=self.select_1)
       self.select1.place(x=135, y=560)

   def select_1(self):  # הפעולה קולטת את הבחירה של השחקן הראשון ומציבה בחירה של צבע לשחק השני
       self.player_one_color = self.colors1.get(self.colors1.curselection())
       num = self.colors1.curselection()
       self.player_two_ = Label(root, text="Player two, select a color: ", bg="pink", font="Comicsansms 10")
       self.player_two_.place(x=350, y=355)
       self.colors2 = Listbox(root, selectmode=SINGLE, bg="pink", font="Comicsansms 10")
       self.colors2.insert(0, "BROWN")
       self.colors2.insert(1, "BLUE")
       self.colors2.insert(2, "GREEN")
       self.colors2.insert(3, "YELLOW")
       self.colors2.insert(4, "PURPLE")
       self.colors2.insert(5, "WHITE")
       self.colors2.insert(6, "BLACK")
       self.colors2.insert(7, "ORANGE")
       self.colors2.insert(8, "GRAY")
       self.colors2.insert(9, "LIGHT BLUE")
       self.colors2.delete(num)
       self.colors2.place(x=355, y=380)
       self.colors2.select_set(0)
       self.select2 = Button(root, text="SELECT", bg="pink",
                             command=self.select_2)
       self.select2.place(x=400, y=560)

   def select_2(self):  # הפעולה קולטת את הבחירה של השחקן השני ומתחילה את השמדת לוח האופציות
       self.player_two_color = self.colors2.get(self.colors2.curselection())
       print(self.player_one_color)
       print(self.player_two_color)
       self.board1_destroy()
       self.player_one_.destroy()
       self.player_two_.destroy()
       self.colors2.destroy()
       self.select2.destroy()
       self.create_board(1)

   def board1_destroy(self):  # הפעולה מנקה את כל הדף של האופציות
       self.optionss.destroy()
       self.line1.destroy()
       self.choice.destroy()
       self.two.destroy()
       self.or1.destroy()
       self.comp.destroy()
       self.line2.destroy()
       self.square_amount.destroy()
       self.line3.destroy()
       self.colors1.destroy()
       self.select1.destroy()
       self.amount.destroy()
       self.clickk.destroy()
       self.Colors.destroy()

   def create_board(self, mode):  # הפעולה בונה את הלוח בתוך canvas. הלוח בנוי ממשולשים
       if self.size > 6:
           self.square_size = 70
       else:
           self.square_size = 100
       self.xsize = 250 + (self.square_size * ((self.size) - 3))
       self.ysize = 250 + (self.square_size * ((self.size) - 3))
       root.geometry(str(self.xsize) + "x" + str(self.ysize))
       root.resizable(0, 0)
       self.board = Canvas(root, bg="Pink", width=self.xsize, height=self.ysize)
       ########### יצירת המשולשים- אחר כך ישמשו שמקום הלחיצה ##############
       x1 = 25
       y1 = 25
       x2 = x1 + (self.square_size // 2)
       y2 = y1 + (self.square_size // 2)
       x3 = (x1 + self.square_size)
       y3 = y1
       # כל ארבעה משולשים יוצרים ריבוע, שהיתר של כל אחד מהם הוא אחד הקירות שלו, לכן הtri_array הוא מטריצה דו מימדית
       # מימד אחד זה המימד הריבוע, והוא מכיל ארבעה משולשים.
       for i in range(self.size - 1):
           self.tri_array.append([])
           for j in range(self.size - 1):
               tri1 = self.board.create_polygon(x1, y1, x2, y2, x3, y3, fill="pink", outline="pink")
               self.board.tag_bind(tri1, "<Button-1>",
                                   lambda event, modee=mode, xx1=x1, yy1=y1, xx2=x3, yy2=y3: self.clicked(modee, xx1,
                                                                                                          yy1,
                                                                                                          xx2, yy2))
               # הכניסה והיציאה זה ריחוף מעל המשלולש
               self.board.tag_bind(tri1, "<Enter>",
                                   lambda event, xx1=x1, yy1=y1, xx2=x3, yy2=y3: self.on_enter(xx1,
                                                                                               yy1,
                                                                                               xx2,
                                                                                               yy2))
               self.board.tag_bind(tri1, "<Leave>",
                                   lambda event, xx1=x1, yy1=y1, xx2=x3, yy2=y3: self.on_leave(xx1,
                                                                                               yy1,
                                                                                               xx2,
                                                                                               yy2))
               self.tri_array[i].append(tri1)
               tri2 = self.board.create_polygon(x1, y1, x2, y2, x3 - self.square_size, y3 + self.square_size,
                                                fill="pink", outline="pink")
               self.board.tag_bind(tri2, "<Button-1>",
                                   lambda event, modee=mode, xx1=x1, yy1=y1, xx2=x3 - self.square_size,
                                          yy2=y3 + self.square_size: self.clicked(mode,
                                                                                  xx1, yy1,
                                                                                  xx2, yy2))
               # הכניסה והיציאה זה ריחוף מעל המשלולש
               self.board.tag_bind(tri2, "<Enter>",
                                   lambda event, xx1=x1, yy1=y1, xx2=x3 - self.square_size,
                                          yy2=y3 + self.square_size: self.on_enter(
                                       xx1,
                                       yy1,
                                       xx2,
                                       yy2))
               self.board.tag_bind(tri2, "<Leave>",
                                   lambda event, xx1=x1, yy1=y1, xx2=x3 - self.square_size,
                                          yy2=y3 + self.square_size: self.on_leave(
                                       xx1,
                                       yy1,
                                       xx2,
                                       yy2))
               self.tri_array[i].append(tri2)
               tri3 = self.board.create_polygon(x1 + self.square_size, y1, x2, y2, x3, y3 + self.square_size,
                                                fill="pink", outline="pink")
               self.board.tag_bind(tri3, "<Button-1>",
                                   lambda event, modee=mode, xx1=x1 + self.square_size, yy1=y1, xx2=x3,
                                          yy2=y3 + self.square_size: self.clicked(modee,
                                                                                  xx1,
                                                                                  yy1,
                                                                                  xx2,
                                                                                  yy2))
               # הכניסה והיציאה זה ריחוף מעל המשלולש
               self.board.tag_bind(tri3, "<Enter>",
                                   lambda event, ii=i, jj=j, xx1=x1 + self.square_size, yy1=y1, xx2=x3,
                                          yy2=y3 + self.square_size: self.on_enter(
                                       xx1,
                                       yy1,
                                       xx2,
                                       yy2))
               self.board.tag_bind(tri3, "<Leave>",
                                   lambda event, xx1=x1 + self.square_size, yy1=y1, xx2=x3,
                                          yy2=y3 + self.square_size: self.on_leave(
                                       xx1,
                                       yy1,
                                       xx2,
                                       yy2))
               self.tri_array[i].append(tri3)
               tri4 = self.board.create_polygon(x1, y1 + self.square_size, x2, y2, x3, y3 + self.square_size,
                                                fill="pink", outline="pink")
               self.board.tag_bind(tri4, "<Button-1>",
                                   lambda event, modee=mode, xx1=x1, yy1=y1 + self.square_size, xx2=x3,
                                          yy2=y3 + self.square_size: self.clicked(modee,
                                                                                  xx1,
                                                                                  yy1,
                                                                                  xx2,
                                                                                  yy2))
               # הכניסה והיציאה זה ריחוף מעל המשלולש
               self.board.tag_bind(tri4, "<Enter>",
                                   lambda event, ii=i, jj=j, xx1=x1, yy1=y1 + self.square_size, xx2=x3,
                                          yy2=y3 + self.square_size: self.on_enter(
                                       xx1,
                                       yy1,
                                       xx2,
                                       yy2))
               self.board.tag_bind(tri4, "<Leave>",
                                   lambda event, xx1=x1, yy1=y1 + self.square_size, xx2=x3,
                                          yy2=y3 + self.square_size: self.on_leave(
                                       xx1,
                                       yy1,
                                       xx2,
                                       yy2))
               self.tri_array[i].append(tri4)
               x1 += self.square_size
               x2 += self.square_size
               x3 += self.square_size
           x1 = 25
           x2 = x1 + (self.square_size // 2)
           x3 = (x1 + self.square_size)
           y1 += self.square_size
           y2 += self.square_size
           y3 += self.square_size
       ############### העיגולים###################
       self.circles()
       self.board.pack()
       self.model = Model(self.player_one_color, self.player_two_color, self.size, self.square_size)

   def on_enter(self, x1, y1, x2,
                y2):  # אם העכבר מרחף מעל משולש כלשהו, כאשר הוא נכנס יווצר קו אדום (רק אם הקיר אינו צבוע)
       if not self.model.was_clicked(self.model.clicked_arr, [x1, y1, x2, y2]):
           self.board.create_line(x1, y1, x2, y2, fill="red", width=6)
           self.circles()

   def circles(self):# מצייר את העיגולים שאותם הקירות מחברים
       if self.size < 7:
           default1 = 15
           default2 = 35
       else:
           default1 = 18
           default2 = 32
       circx1 = default1
       circy1 = default1
       circx2 = default2
       circy2 = default2
       for i in range(self.size):
           for j in range(self.size):
               self.board.create_oval(circx1, circy1, circx2, circy2, fill="Black")
               circx1 += self.square_size
               circx2 += self.square_size
           circx1 = default1
           circx2 = default2
           circy1 += self.square_size
           circy2 += self.square_size

   def on_leave(self, x1, y1, x2,
                y2):  # אם העכבר מרחף מעל משולש כלשהו, כאשר הוא יוצא הוא מוחק את הקו אדום (רק אם הקיר אינו צבוע)
       if not Model.was_clicked(self.model.clicked_arr, [x1, y1, x2, y2]):
           self.board.create_line(x1, y1, x2, y2, fill="pink", width=6)
           self.circles()

   def clicked(self, mode, x1, y1, x2, y2):  # הפעולה עושה את התור של השחקן שלחץ על קיר מסויים. אם הקיר ממלא ריבוע,
       # השחק יקבל תור נוסף, # אחרת אם הסוג משחק הוא שני שחקנים, התור יעבור לשחקן הבא,
       # ואם הסוג הוא נגד המחשב אז תיקרא הפעולה של תור מחשב
       if not Model.was_clicked(self.model.clicked_arr, [x1, y1, x2, y2]):
           self.model.clicked_arr.append([x1, y1, x2, y2])
           self.board.create_line(x1, y1, x2, y2, fill=self.model.turn, width=6)

           self.circles()
           close_sq = self.model.in_square(x1, y1, x2, y2, "user")
           print("c " + str(close_sq))
           for i in self.model.square_drawing:
               if i is not None:
                   self.paint_square(i[0], i[1])
           if self.model.all_full(self.model.s):
               self.finish(self.model.win(self.model.s, self.player_one_color, self.player_two_color))
           if mode == 2 and close_sq == 0:
               self.model.change_turns()
               self.computer_turn()
               print("i")
           elif mode == 1 and close_sq == 0:
               self.model.change_turns()
           else:
               return

   def update_grafics(self):  # הפעולה מעדכנת את הגרפיקה אחרי שהתור של המחשב קורה ומחזירהה את הקו שעודכן.
       line = []
       for s_line in self.model.s:
           for sq in s_line:
               for side in sq.walls:
                   if sq.walls[side] == True:
                       line = sq.ret_line(side)
                       if line != None and not self.model.was_clicked(self.model.clicked_arr, line):
                           self.model.clicked_arr.append(line)
                           self.board.create_line(line, fill=self.model.turn, width=6)

       return line

   def computer_turn(
           self):  # הפעולה קוראת למינמקס כדי לעשות את תור המחשב, ולאחר מכן מעדכנת את הגרפיקה ובודקת אם יש ניצחון
       game_state = self.model.minmax(self.model.s, 3, self.model.turn, self.player_one_color,
                                      self.player_two_color, self.size)
       if game_state != None:
           self.model.s = game_state
       self.update_grafics()
       self.circles()
       self.model.draw_full()
       for i in self.model.square_drawing:
           if i is not None:
               self.paint_square(i[0], i[1])
       root.update()
       if self.model.all_full(self.model.s):
           self.finish(self.model.win(self.model.s, self.player_one_color, self.player_two_color))
       self.model.change_turns()

   def paint_square(self, i, j):  # הפעולה כותבת את הצבע של הריבוע הנתון, באמצע הריבוע.
       self.win_labels = []
       self.model.list_full.append([i, j])
       if self.size < 6:
           x1 = self.model.s[i][j].lines[0][0] + 20
           y1 = self.model.s[i][j].lines[0][1] + 20
           label = Label(root, text=self.model.s[i][j].color, width=6, height=3, bg="pink", font="Comicsansms 10")
       else:
           x1 = self.model.s[i][j].lines[0][0] + 20
           y1 = self.model.s[i][j].lines[0][1] + 20
           label = Label(root, text=self.model.s[i][j].color, width=6, height=3, bg="pink", font="Comicsansms 10")
       self.win_labels.append(label)
       label.place(x=x1, y=y1)

   def finish(self, winner):  # הפעולה כותבת איזה שחקן ניצח ופותחת אופציה של משחק חוזר.
       self.end_frame = Tk()
       self.end_frame.geometry("250x200")
       self.end_frame.config(bg= "pink")
       self.end = Label(self.end_frame, text='GAME OVER!', bg="pink", font="Comicsansms 20 bold italic")
       self.end.place(x= 20, y=0)
       self.winner = Label(self.end_frame, text='THE WINNER IS: ', bg="pink", font="Comicsansms 10 bold italic")
       self.winner.place(x=20, y=50)
       self.sign = Label(self.end_frame, text=winner, bg="pink", font="Comicsansms 10 bold italic")
       self.sign.place(x=120, y=50)
       self.start_again_button = Button(self.end_frame, text='restart', bg="pink", font="Comicsansms 20 bold italic",
                                        command=self.start_again)
       self.start_again_button.place(x=20, y=100)
       root.update()


   def start_again(self):  # הפעולה קוראת לפעולה החיצונית שמתחילה את המשחק מחדש.
       root.destroy()
       self.end_frame.destroy()
       start()


class Square:
   def __init__(self, i, j, square_size,
                size):  # הפעולה הבונה של המחלקה. הפעולה בונה את הריבוע, i ו-j הן המקום של הריבוע במערך של כל הריבועים, ו-square size הוא הגודל של כל ריבוע. הפעולה גם יוצרת את dictionary של צדדי הריבוע ומאתחלת את כל הפירושים כFalse.
       self.i = i
       self.j = j
       self.num_of_lines = 0
       self.color = None
       self.walls = {'up':False, 'down':False,'right':False,'left':False}
       '''self.walls['up'] = False
       self.walls['down'] = False
       self.walls['right'] = False
       self.walls['left'] = False'''
       self.lines = []
       self.size = size
       self.square_size = square_size

   def add_lines(self, x1, y1):  # הפעולה יוצרת מערך של כל הקירות בריבוע לפי הקורדינטות ההתחלתיות וself.square_size.
       #נחוץ להצגת הגרפיקה. החלק הגרפי של הריבוע.
       self.lines.append([x1, y1, x1 + self.square_size, y1])  # up
       self.lines.append([x1, y1, x1, y1 + self.square_size])  # left
       self.lines.append([x1 + self.square_size, y1, x1 + self.square_size, y1 + self.square_size])  # right
       self.lines.append([x1, y1 + self.square_size, x1 + self.square_size, y1 + self.square_size])  # down
       print(self.lines)

   def choose_wall(self,
                   game_state):  # הפעולה בוחרת בצורה רנדומלית קיר למלא ובודקת שהוא מתאים לפי מצב המשחק- כל עוד הוא לא יוצר ריבוע עם שלוש קירות או מלא.
       list_side = ["up", "left", "right", "down"]
       for i in reversed(range(4)):
           x = random.randint(0, i)
           if self.walls[list_side[x]] == False:
               num = Model.check_neighbor(game_state, self, list_side[x], self.size)
               if not (self.num_of_lines <= 2 and num > 2):
                   self.walls[list_side[x]] = True
                   return list_side[x]
           list_side.remove(list_side[x])
       return None

   def is_line(self, x1, y1, x2, y2):  # בודקת לאיזה צד משתייכים הקורדינטות של הקיר ומחזירה אותו.
       for i in range(4):
           if self.lines[i] == [x1, y1, x2, y2]:
               if i == 0:
                   return "up"
               if i == 1:
                   return "left"
               if i == 2:
                   return "right"
               if i == 3:
                   return "down"

   def update_wall(self, wall):  # הפעולה משנה את הפירוש במילון self.walls לקיר הנתון לTrue.
       self.walls[wall] = True

   def ret_line(self, wall):  # הפעולה מחזירה את הקורדינטות של הקיר.
       if wall == "up":
           return self.lines[0]
       if wall == "down":
           return self.lines[3]
       if wall == "left":
           return self.lines[1]
       if wall == "right":
           return self.lines[2]


class Model:
   # 3 ריבועים- למלא, 2- לא, 0 ואז 1
   def __init__(self, color1, color2, size,
                square_size):  # הפעולה הבונה של המחלקה, מכניסה לתוך תכונות המחלקה את משתני המחלקה ויוצרת את המטריצה של הריבועים.
       self.size = size
       self.s = []
       self.list_full = []
       self.clicked_arr = []
       x1 = 25
       y1 = 25
       for i in range(self.size - 1):
           self.s.append([])
           for j in range(self.size - 1):
               self.s[i].append(Square(i, j, square_size, self.size))
               self.s[i][j].add_lines(x1, y1)
               x1 += square_size
           x1 = 25
           y1 += square_size
       self.player_one_color = color1
       self.player_two_color = color2
       self.turn = self.player_one_color

   @staticmethod
   def was_clicked(clicked_arr, a):  # הפעולה מחזירה אמת אם a הוא בתוך clicked_arr ושקר אם אחרת.
       for i in clicked_arr:
           if i == a:
               return True
       return False

   def in_square(self, x1, y1, x2, y2,
                 mode='computer'):  # הפעולה בודקת אם הקורדינטות הנתונות הן קיר של ריבוע ומעדכן אותו.
       ret = 0
       self.square_drawing = []
       for i in range(self.size - 1):  # בדיקה של כל הריבועים
           for j in range(self.size - 1):
               if not self.s[i][j].num_of_lines == 4:
                   if self.s[i][j].num_of_lines == 3:
                       print("aaaa")
                   if self.s[i][j].is_line(x1, y1, x2, y2) is not None:
                       if mode == "user":
                           self.s[i][j].num_of_lines += 1
                       side = self.s[i][j].is_line(x1, y1, x2, y2)
                       self.s[i][j].update_wall(side)
                       print(self.s[i][j].num_of_lines)
                       if self.s[i][j].num_of_lines == 4:  # אם הריבוע מלא מוסיפים אותו למערך שאומר מה לצבוע
                           print("closed sq", self.turn)
                           self.s[i][j].color = self.turn
                           self.square_drawing.append([i, j])
                           ret += 1
       return ret

   def draw_full(self):  # הפעולה שמה בתוך המשתנה square_drawings את כל הריבועים המלאים החדשים שצריך לצבוע.
       self.square_drawing = []
       for i in range(len(self.s)):
           for j in range(len(self.s)):
               if self.s[i][j].num_of_lines == 4:
                   self.square_drawing.append([i, j])

   def in_list_full(self, s):  # הפעולה בודקת אם הריבוע כבר מלא.
       for i in self.list_full:
           if i == s:
               return true

   @staticmethod
   def all_full(game_state):  # הפעולה בודקת אם כל הריבועים מלאים ומחזירה אמת או שקר בהתאם
       for i in range(len(game_state)):
           for j in range(len(game_state)):
               if not game_state[i][j].num_of_lines == 4:
                   return False
       return True

   @staticmethod
   def win(game_state, player_one_color,
           player_two_color):  # הפעולה נקראת רק כאשר הלוח מלא. היא בודקת לאיזה שחקן יש יותר ריבועים ומחזיקה את הצבע שלו. אם יש תיקו אז היא מחזירה "tie"
       color1 = 0
       color2 = 0
       for i in range(len(game_state)):
           for j in range(len(game_state)):
               if game_state[i][j].color == player_one_color:
                   color1 += 1
               if game_state[i][j].color == player_two_color:
                   color2 += 1
       if color1 > color2:
           return player_one_color
       if color1 < color2:
           return player_two_color
       if color1 == color2:
           return "tie"

   def change_turns(self):  # מחליפה את התור הנוכחי.
       if self.turn == self.player_two_color:
           self.turn = self.player_one_color
       else:
           self.turn = self.player_two_color

   @staticmethod
   def count_boxes(game_state, player_one_color, player_two_color):
       #פעולת עזר לפעולה nikud, סופרת כמה קופסאות יש לכל שחקן ומחזירה את ההפרש ביניהם,
       # כאשר כשההפרש חיובי הוא לטובת המחשב ושלילי- השחקן האנושי
       player = 0
       comp = 0
       for i in range(len(game_state)):
           for j in range(len(game_state)):
               if game_state[i][j].color == player_one_color:
                   player += 1
               if game_state[i][j].color == player_two_color:
                   comp += 1
       return comp - player



   @staticmethod
   def check_neighbor(all_squares, square, wall, size): #הפעולה בודקת על איזה שכן של הריבוע- מעל, מתחת, משמאל, או מימין, משפיע הקיר שנבחר, ומחזירה את מספר הקירות הצבועים של השכן.
                                                       #היא מקבלת: all_squares- מערך של כל הריבועים
                                                       #square- הריבוע שרוצים לבדוק את השכנים שלו
                                                       #wall- הצד שלחצו עליו
                                                       #size- מספר הריבועים
       if wall == "up" and square.i > 0 and all_squares[square.i - 1][square.j].walls['down'] == False:
           return all_squares[square.i - 1][square.j].num_of_lines
       if wall == "down" and square.i < (size - 2) and all_squares[square.i + 1][square.j].walls['up'] == False:
           return all_squares[square.i + 1][square.j].num_of_lines
       if wall == "left" and square.j > 0 and all_squares[square.i][square.j - 1].walls['right'] == False:
           return all_squares[square.i][square.j - 1].num_of_lines
       if wall == "right" and square.j < (size - 2) and all_squares[square.i][square.j + 1].walls['left'] == False:
           return all_squares[square.i][square.j + 1].num_of_lines
       return 0

   @staticmethod
   def update_neighbor(all_squares, square, wall, size): #הפעולה בודקת על איזה שכן של הריבוע- מעל, מתחת, משמאל, או מימין, משפיע הקיר שנבחר, מעדכנת אותו ומחזירה מחדש את המשתנה all_squares
       # הפעולה מקבלת: all_squares- מערך של כל הריבועים
       # square- הריבוע שרוצים לבדוק את השכנים שלו
       # wall- הצד שלחצו עליו
       # size- מספר הריבועים
       if wall == "up" and square.i > 0 and all_squares[square.i - 1][square.j].walls['down'] == False:
           all_squares[square.i - 1][square.j].walls['down'] = True
           all_squares[square.i - 1][square.j].num_of_lines += 1
       if wall == "down" and square.i < (size - 2) and all_squares[square.i + 1][square.j].walls['up'] == False:
           all_squares[square.i + 1][square.j].walls['up'] = True
           all_squares[square.i + 1][square.j].num_of_lines += 1
       if wall == "left" and square.j > 0 and all_squares[square.i][square.j - 1].walls['right'] == False:
           all_squares[square.i][square.j - 1].walls['right'] = True
           all_squares[square.i][square.j - 1].num_of_lines += 1
       if wall == "right" and square.j < (size - 2) and all_squares[square.i][square.j + 1].walls['left'] == False:
           all_squares[square.i][square.j + 1].walls['left'] = True
           all_squares[square.i][square.j + 1].num_of_lines += 1
       return all_squares

   @staticmethod
   def sort_boxes(game_state): #הפעולה ממיינת את כל הריבועים לתוך ארבע רשימות לפי מספר הקירות הצבועים בו
       # (ללא ריבועים שיש בהם 4 קירות צבועים), ומחזירה chain של כל הרשימות.
       # בנוסף היא גם בודקת אם אין שום ריבוע שבו 3 קירות צבועים ויש ריבוע אחר עם 0 קירות צבועים
       # ואם מצב זה קיים היא בוחרת את הריבוע עם ה0 ומחזירה אותו ומקצרת את הפעולה.
       list_0 = []
       list_1 = []
       list_2 = []
       list_3 = []
       for i in range(len(game_state)):
           for j in range(len(game_state)):
               if game_state[i][j].num_of_lines != 4:
                   eval(f'list_{game_state[i][j].num_of_lines}').append(game_state[i][j])
       if len(list_3) == 0 and len(list_0) != 0:
           i = random.randint(0, len(list_0) - 1)
           return [list_0[i]]
       return list(chain(list_3, list_0, list_1, list_2))

   @staticmethod
   def nextBoards(game_state, comp_color, size):  # פעולה רקורסיבית המחפשת את כל הלוחות האפשריים בשביל המינמקס.
       # הפעולה היא רקורסיבית במצב שהמחשב ממלא ריבוע ויש לו תור נוסף, ואז צריך למצוא את המהלך הבא הטוב ביותר,
       # אחרת היא עוברת על הרשימה של הריבועים מהפעולה sort_boxes ומעדכנת את כל אחד מהם והשכנים שלהם ושמה במערך חדש
       # את הלוח עם העדכון. כאשר היא מסיימת לעבור על כל המערך היא מחזירה את הרשימה של הלוחות.
       list_all_next_boards = []
       list_sorted_boxes = Model.sort_boxes(game_state)
       if len(list_sorted_boxes) == 0:
           return [game_state]
       for s in list_sorted_boxes:
           a = deepcopy(game_state)
           i, j = s.i, s.j
           side = Square.choose_wall(a[i][j], game_state)
           a[i][j].num_of_lines += 1
           a[i][j].update_wall(side)
           a = Model.update_neighbor(a, a[i][j], side, size)
           if a[i][j].num_of_lines == 4:
               a[i][j].color = comp_color
               return Model.nextBoards(a, comp_color, size)
           list_all_next_boards.append(a)
       return list_all_next_boards

   @staticmethod
   def is_win(game_state, player, player_one_color, player_two_color): #הפעולה בודקת אם השחקן הנתון מנצח, מחזירה אמת אם כן ושקר אחרת.
       #היא מקבלת: game_state- מצב המשחק
       #player - השחקן שרוצים לבדוק אם הוא ניצח
       #Player_one_color, player_two_color -הצבעים של כל אחד מהשחקנים
       if Model.all_full(game_state):
           if Model.win(game_state, player_one_color, player_two_color) == player:
               return True
       return False

   @staticmethod
   def nikud(game_state, player_one_color, player_two_color):
       #הפעולה מחזירה 10- אם השחקן האנושי מנצח, 7 אם המחשב מנצח.
       # אם אף אחד מהם לא מנצח קוראים לפעולה count boxes, ולכל הפרש חיובי מחזירים +1 ולכל הפרש שלילי 2-.
       if Model.is_win(game_state, 1, player_one_color, player_two_color):
           return -10
       # בשביל המחשב
       if Model.is_win(game_state, 2, player_one_color, player_two_color):
           return 7
       score = 0
       difference = Model.count_boxes(game_state, player_one_color, player_two_color)
       if difference > 0:
          for i in range(difference):
               score += 1
          return score
       if difference < 0:
           for i in range(difference):
               score -= 2
           return score
       return 0

   @staticmethod
   def minmax(game_state, depth, comp_color, player_one_color, player_two_color, size):
       #הפעולה עוברת על הרשימה של הלוחות שחוזרת מהפעולה nextBoards וקוראת לפעולה min_play על כל אחד מהם,
       # בmin_play זה קורא לmax_play וההפך עד שהם מחזירים את הניקוד הגבוה ביותר. היא מחזירה את הלוח עם הניקוד הגבוה ביותר.
       #הפעולה מקבלת: game_state- מצב המשחק
       #depth- עומק המינמקס
       #comp_color: הצבע של המחשב
       #Player_one_color, player_two_color -הצבעים של כל אחד מהשחקנים
       next_boards = Model.nextBoards(game_state, comp_color, size)
       if len(next_boards) == 0:
           return game_state
       if len(next_boards) == 1:
           return next_boards[0]
       best_move = next_boards[0]
       best_score = float('-inf')
       alpha = float("-inf")
       beta = float("inf")
       for move in next_boards:
           score = Model.min_play(move, depth - 1, comp_color, player_one_color, player_two_color, alpha, beta, size)
           if score > best_score:
               best_move = move
               best_score = score
       return best_move

   @staticmethod
   def min_play(game_state, depth, comp_color, player_one_color, player_two_color, alpha, beta, size):
       #הפעולה בודקת לאיזה לוח מהרשימה שהפעולה nextBoards מחזירה יש את הניקוד הנמוך ביותר.
       # היא מקבלת: game_state- מצב המשחק
       # comp_color: הצבע של המחשב
       # Player_one_color, player_two_color -הצבעים של כל אחד מהשחקנים
       # Alpha, beta- המשתנים לאלגורתם אלפא בטא
       if depth == 0 or Model.all_full(game_state):
           return Model.nikud(game_state, player_one_color, player_two_color)
       # לשנות ללוח מלא
       moves_board = Model.nextBoards(game_state, comp_color, size)
       best_score = float('inf')
       for move in moves_board:
           score = Model.max_play(move, depth - 1, comp_color, player_one_color, player_two_color, alpha, beta, size)
           if score < best_score:
               best_score = score
           if best_score < beta:
               beta = best_score
           if beta <= alpha:
               break
       return best_score

   @staticmethod
   def max_play(game_state, depth, comp_color, player_one_color, player_two_color, alpha, beta, size):
       #הפעולה בודקת לאיזה לוח מהרשימה שהפעולה nextBoards מחזירה יש את הניקוד הנמוך ביותר.
       #היא מקבלת: game_state- מצב המשחק
       #comp_color: הצבע של המחשב
       #Player_one_color, player_two_color -הצבעים של כל אחד מהשחקנים
       #Alpha, beta- המשתנים לאלגורתם אלפא בטא

       if depth == 0 or Model.all_full(game_state):
           return Model.nikud(game_state, player_one_color, player_two_color)
       moves_board = Model.nextBoards(game_state, comp_color, size)
       best_score = float('-inf')
       for move in moves_board:
           score = Model.min_play(move, depth - 1, comp_color, player_one_color, player_two_color, alpha, beta, size)
           if score > best_score:
               best_score = score
           if best_score > alpha:
               alpha = best_score
           if beta <= alpha:
               break
       return best_score


def start():
   global root
   root = Tk()
   root.geometry("600x600")
   root.config(bg="pink")
   global gra
   gra = Graphics()
   root.mainloop()


start()





