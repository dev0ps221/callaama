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
        self.configureControls()
        self.showControls()
        self.update()
 

 class Game :

     def main(self,page:Page)
        self.page = page
        self.
     def start(self):
        self.game = app(target=self.main)
        


     def __init__(self):