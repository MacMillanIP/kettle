from kivy.core.window import Window
from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from ins import * 
from ruffier import*
from kivy.core.window import Window
from seconds import Seconds


age = None
name = None
p1,p2,p3 = None , None , None

ruf_index = 0
window_color = (0, 0.20, 0.20, 1)
Window.clearcolor = window_color 
btn_color = (0, 0.6, 0.9, 1)
Window.size = (300, 600)


def get_num(num):
    try:
        num = int(num)
        if num > 7 :
            return num 
        else :
            return False
    except:
        return False

class MainScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs) # имя экрана должно передаваться конструктору класса Screen
        txt = Label(text=txt_ins)
        self.user_name = TextInput(multiline=False)
        self.user_age = TextInput(multiline=False)
        txt_name = Label(text = "Name:")
        txt_age = Label(text = "Age")
        self.btn = Button(text = "Next")
        self.btn.background_color = btn_color
        self.btn.on_press = self.next


        
        main_bl = BoxLayout(orientation="vertical")
        bl1 = BoxLayout(orientation="vertical" , size_hint=(1,.70))
        bl2 = BoxLayout(size_hint=(1,.10))
        bl3 = BoxLayout(size_hint=(1,.10))
        bl4 = BoxLayout(size_hint=(1,.10))
        
        bl1.add_widget(txt)
        bl2.add_widget(txt_name)
        bl2.add_widget(self.user_name)
        bl3.add_widget(txt_age)
        bl3.add_widget(self.user_age)
        bl4.add_widget(self.btn)

        main_bl.add_widget(bl1)
        main_bl.add_widget(bl2)
        main_bl.add_widget(bl3)
        main_bl.add_widget(bl4)
        self.add_widget(main_bl)
    
    def next(self):
        global name
        global age 
        name = self.user_name.text
        age = get_num(self.user_age.text)        
        if age == False :
            self.user_age.text = ""
        else :
            self.manager.transition.direction = 'left'
            self.manager.current = '2'



class Color(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        txt = Label(text = "Выберите цветовую схему: ")
        self.btn1 = Button(text = "Черная тема")
        self.btn2 = Button(text = "Белая тема")
        self.btn1.on_press = self.next1
        self.btn2.on_press = self.next2

        main_bl = BoxLayout(orientation="vertical")
        bl = BoxLayout(size_hint=(1,.08))
        bl2 = BoxLayout(size_hint=(1,.08))


        bl.add_widget(self.btn1)
        bl2.add_widget(self.btn2)

        main_bl.add_widget(bl)
        main_bl.add_widget(bl2)
        self.add_widget(main_bl)


    def next1(self):
        global window_color
        global btn_color
        window_color = (0, 0, 0, 0)
        btn_color = (255, 255, 255, 0)


        self.manager.transition.direction = 'left'
        self.manager.current = 'main'



    def next2(self):
        global window_color
        global btn_color
        window_color = (255, 255, 255, 0)
        btn_color = (0, 0, 0, 0)
        self.manager.transition.direction = 'left'
        self.manager.current = 'main'
        



class Scr2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs) # имя экрана должно передаваться конструктору класса Screen
        txt = Label(text=ins_test1)
        self.pulse = TextInput(multiline=False)
        txt_pulse = Label(text = "Pulse")
        self.btn = Button(text = "Start")
        self.btn.on_press = self.next
        self.lbl_sec = Seconds(15)
        
        main_bl = BoxLayout(orientation="vertical")
        bl1 = BoxLayout(orientation="vertical" , size_hint=(1,.56))
        bl2 = BoxLayout(size_hint=(1,.08))
        bl3 = BoxLayout(size_hint=(1,.08))
        bl4 = BoxLayout(size_hint=(1,.08))
        self.btn.background_color = btn_color
        bl1.add_widget(txt)
        bl2.add_widget(txt_pulse)
        bl2.add_widget(self.pulse)
        bl3.add_widget(self.btn)    
        bl4.add_widget(self.lbl_sec)
        

        main_bl.add_widget(bl1)
        main_bl.add_widget(bl4)
        main_bl.add_widget(bl2)
        main_bl.add_widget(bl3)
        

        self.add_widget(main_bl)

    def next(self):
        global p1
        if self.btn.text == "Start" :
            self.lbl_sec.start()
            self.btn.text = "Next"
        else :
            p1 = get_num(self.pulse.text)
            if p1 == False:
                self.pulse.text=""
            else:
                self.manager.transition.direction = 'left'
                self.manager.current = '3'
    def clean(self):
        self.user_


class Scr3(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs) # имя экрана должно передаваться конструктору класса Screen
        txt = Label(text=ins_test2)
        self.btn = Button(text = "Start")
        self.btn.on_press = self.next
        self.btn.background_color = btn_color
        self.lbl_sec = Seconds(15)
        main_bl = BoxLayout(orientation="vertical")
        bl1 = BoxLayout(orientation="vertical" , size_hint=(1,.60))
        bl2 = BoxLayout(size_hint=(1,.10))
        bl4 = BoxLayout(size_hint=(1,.08))
        bl1.add_widget(txt)
        bl2.add_widget(self.btn)
        bl4.add_widget(self.lbl_sec)
  
        main_bl.add_widget(bl1)
        main_bl.add_widget(bl4)
        main_bl.add_widget(bl2)

        self.add_widget(main_bl)

    def next(self):
        if self.btn.text == "Start" :
            self.lbl_sec.start()
            self.btn.text = "Next"
        else :
            self.manager.transition.direction = 'left'
            self.manager.current = '4'

class Scr4(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs) # имя экрана должно передаваться конструктору класса Screen
        txt = Label(text=txt_test3)
        self.pulse2 = TextInput(multiline=False)
        self.pulse3 = TextInput(multiline=False)
        txt_name = Label(text = "Pulse_1")
        txt_age = Label(text = "Pulse_2")
        self.btn = Button(text = "Next")
        self.btn.on_press = self.next
        self.btn.background_color = btn_color
        
        
        main_bl = BoxLayout(orientation="vertical")
        bl1 = BoxLayout(orientation="vertical" , size_hint=(1,.70))
        bl2 = BoxLayout(size_hint=(1,.10))
        bl3 = BoxLayout(size_hint=(1,.10))
        bl4 = BoxLayout(size_hint=(1,.10))
        bl1.add_widget(txt)
        bl2.add_widget(txt_name)
        bl2.add_widget(self.pulse2)
        bl3.add_widget(txt_age)
        bl3.add_widget(self.pulse3)
        bl4.add_widget(self.btn)
 
        main_bl.add_widget(bl1)
        main_bl.add_widget(bl2)
        main_bl.add_widget(bl3)
        main_bl.add_widget(bl4)
        self.add_widget(main_bl)
    def next(self):
        global p2 
        global p3 
        if self.btn.text == "Start" :
            self.lbl_sec.start()
            self.btn.text = "Next"
        else :
            p2 = get_num(self.pulse2.text)
            p3 = get_num(self.pulse3.text)
            self.manager.transition.direction = 'left'
            self.manager.current = '5'




class Scr5(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs) # имя экрана должно передаваться конструктору класса Screen
        self.txt = Label(text = "")
        self.btn = Button(text = "back")
        self.btn.on_press = self.back
        self.btn.background_color = btn_color
        main_bl = BoxLayout(orientation="vertical")
        bl1 = BoxLayout(orientation="vertical" , size_hint=(1,.90))
        bl2 = BoxLayout(size_hint=(1,.10))
        bl1.add_widget(self.txt)
        bl2.add_widget(self.btn)
        main_bl.add_widget(bl1)
        main_bl.add_widget(bl2)
        self.add_widget(main_bl)
        self.on_enter = self.index_ruffier
    def index_ruffier(self):
        ir = (4*(p1+p2+p3)-200)/10
        self.txt.text = txt_ending +str(ir)





    def back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'
        global p1 
        global p2 
        global p3






class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Color(name='color'))
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(Scr2(name='2'))
        sm.add_widget(Scr3(name="3"))
        sm.add_widget(Scr4(name='4'))
        sm.add_widget(Scr5(name='5'))
        
        return sm

app = MyApp()
app.run()