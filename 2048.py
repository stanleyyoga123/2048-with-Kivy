from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.modules import keybinding
from kivy.core.window import Window

import random
from random import randint
from random import choice

matrix_2048=[[0 for x in range(4)] for y in range(4)]
matrix_before = [[0 for x in range(4)] for y in range(4)]
queue = [0 for x in range(4)]

class MyGrid(GridLayout):
    matrix=[[0 for x in range(4)] for y in range(4)]
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        
        self.cols = 4
        count = 0

        for i in range(4):
            for j in range(4):
                k = random.randrange(1,50)
                if(k > 25 and count < 4):
                    count+=1
                    matrix_2048[i][j] = 2
                m = matrix_2048[i][j]
                if(m == 0):
                    text_in = ''
                else:
                    text_in = '2'
                if(matrix_2048[i][j] == 0):
                    color = (0,0,0,1)
                else:
                    color = (248/255,196/255,20/255,1)
                self.matrix[i][j] = Button(text = text_in, background_color = color)

        for i in range(4):
            for j in range(4):
                self.add_widget(self.matrix[i][j])
        
        self.print_matrix_2048()

    def change_matrix(self):
        k = randint(0, 3)
        l = randint(0, 3)
        print(str(k))
        print(str(l))
        while(matrix_2048[k][l] != 0):
            k = randint(0,3)
            l = randint(0,3)
        inner = choice([2,4])
        print(str(inner))
        matrix_2048[k][l] = inner
        for i in range(4):
            for j in range(4):
                m = matrix_2048[i][j]
                if(m == 0):
                    text_in = ''
                else:
                    text_in = str(matrix_2048[i][j])
                if(matrix_2048[i][j] == 0):
                    color = (0,0,0,1)
                else:
                    color = (248/255,196/255,20/255,1)
                self.matrix[i][j].text = text_in
                self.matrix[i][j].background_color = color

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if(keycode[1] == 'w'):
            self.copy_matrix()
            self.command_w()
            if(self.is_change()):
                self.change_matrix()
        elif(keycode[1] == 's'):
            self.copy_matrix()
            self.command_s()
            if(self.is_change()):
                self.change_matrix()
        elif(keycode[1] == 'a'):
            self.copy_matrix()
            self.command_a()
            if(self.is_change()):
                self.change_matrix()
        elif(keycode[1] == 'd'):
            self.copy_matrix()
            self.command_d()
            if(self.is_change()):
                self.change_matrix()
        return True
    
    def is_change(self):
        for i in range(4):
            for j in range(4):
                if(matrix_2048[i][j] != matrix_before[i][j]):
                    return True
        return False
    
    def copy_matrix(self):
        for i in range(4):
            for j in range(4):
                matrix_before[i][j] = matrix_2048[i][j]

    def queue_vertical_w(self, y):
        for i in range(4):
            queue[i] = matrix_2048[i][y]

    def queue_vertical_s(self, y):
        for i in range(4):
            queue[i] = matrix_2048[3-i][y]

    def queue_horizontal_a(self, x):
        for i in range(4):
            queue[i] = matrix_2048[x][i]

    def queue_horizontal_d(self, x):
        for i in range(4):
            queue[i] = matrix_2048[x][3-i]

    def add(self, x):
        for i in range(2,-1,-1):
            queue[i+1] = queue[i]
        queue[0] = x 
    
    def delete(self):
        ret_val = queue[0]
        for i in range(1,4):
            queue[i-1] = queue[i]
        queue[3] = 0
        return ret_val

    def command_w(self):
        for i in range(4):
            self.queue_vertical_w(i)
            temp_answer = []
            for j in range(4):
                temp = self.delete()
                counter = 0
                while(temp == 0 and counter < 4):
                    temp = self.delete()
                    counter+=1
                if(counter == 4):
                    temp = 0
                temp_2 = self.delete()
                counter = 0
                while(temp_2 == 0 and counter < 4):
                    temp_2 = self.delete()
                    counter+=1
                if(counter == 4):
                    temp_2 = 0
                if(temp == temp_2):
                    temp += temp_2
                    temp_answer.append(temp)
                else:
                    temp_answer.append(temp)
                    self.add(temp_2)
            print(temp_answer)
            for j in range(4):
                matrix_2048[j][i] = temp_answer[j]
    
    def command_s(self):
        for i in range(4):
            self.queue_vertical_s(i)
            temp_answer = []
            for j in range(4):
                temp = self.delete()
                counter = 0
                while(temp == 0 and counter < 4):
                    temp = self.delete()
                    counter+=1
                if(counter == 4):
                    temp = 0
                temp_2 = self.delete()
                counter = 0
                while(temp_2 == 0 and counter < 4):
                    temp_2 = self.delete()
                    counter+=1
                if(counter == 4):
                    temp_2 = 0
                if(temp == temp_2):
                    temp += temp_2
                    temp_answer.append(temp)
                else:
                    temp_answer.append(temp)
                    self.add(temp_2)
            for j in range(4):
                matrix_2048[3-j][i] = temp_answer[j]
    
    def command_a(self):
        for i in range(4):
            self.queue_horizontal_a(i)
            print(queue)
            temp_answer = []
            for j in range(4):
                temp = self.delete()
                counter = 0
                while(temp == 0 and counter < 4):
                    temp = self.delete()
                    counter+=1
                if(counter == 4):
                    temp = 0
                temp_2 = self.delete()
                counter = 0
                while(temp_2 == 0 and counter < 4):
                    temp_2 = self.delete()
                    counter+=1
                if(counter == 4):
                    temp_2 = 0
                if(temp == temp_2):
                    temp += temp_2
                    temp_answer.append(temp)
                else:
                    temp_answer.append(temp)
                    self.add(temp_2)
            print("TEMP ANSWER")
            print(temp_answer)
            for j in range(4):
                matrix_2048[i][j] = temp_answer[j]

    def command_d(self):
        for i in range(4):
            self.queue_horizontal_d(i)
            print(queue)
            temp_answer = []
            for j in range(4):
                temp = self.delete()
                counter = 0
                while(temp == 0 and counter < 4):
                    temp = self.delete()
                    counter+=1
                if(counter == 4):
                    temp = 0
                temp_2 = self.delete()
                counter = 0
                while(temp_2 == 0 and counter < 4):
                    temp_2 = self.delete()
                    counter+=1
                if(counter == 4):
                    temp_2 = 0
                if(temp == temp_2):
                    temp += temp_2
                    temp_answer.append(temp)
                else:
                    temp_answer.append(temp)
                    self.add(temp_2)
            print("TEMP ANSWER")
            print(temp_answer)
            for j in range(4):
                matrix_2048[i][3-j] = temp_answer[j]

            

    def print_queue(self):
        for i in range(4):
            print(str(queue[i]))

    def print_matrix_2048(self):
        for i in range(4):
            for j in range(4):
                print(str(matrix_2048[i][j]), end= "")
            print()

class MyApp(App):
    def build(self):
        return MyGrid()

MyApp().run()