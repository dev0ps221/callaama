#!/usr/bin/env python3
from flet import app,Page,Text,ElevatedButton,Row,Column
app_title = 'Callaama'
app_version = '0.1'

class StartPage:
    starttext_container = None
    startbutton_container = None
    starttext = Text(value=f'{app_title} V{app_version}')
    startbutton = ElevatedButton(text='COMMENCER')

    def configureControls(self):
        self.starttext_container.controls.append(self.starttext)
        self.startbutton_container.controls.append(self.startbutton)

    def showControls(self):
        self.container.controls.append(self.starttext_container)
        self.container.controls.append(self.startbutton_container)
    
    def addOnPage(self,page):
        page.add(self.container)
        page.update()
 
    def createControls(self):
        self.starttext_container = Column()
        self.startbutton_container = Column()

    def __init__(self,app):
        self.app = app
        self.container = Column()
        self.createControls()
        self.configureControls()
        self.showControls()
 

class Game :

    def main(self,page:Page):
        self.page = page
        self.actualview = 'start_menu'
        self.start_menu = StartPage(self)
        self.views = {
            'start_menu' : self.start_menu 
        }
        self.refreshView()

    def start_game(self):

    def end_game(self):
        

    def showView(self):
        self.views[self.actualview].addOnPage(self.page)

    def refreshView(self):
        for view in self.views:
            self.page.remove(self.views[view]) if self.views[view] in self.page._controls else None
        self.showView()

    def start(self):
        self.game = app(target=self.main)
        

game = Game()
game.start()