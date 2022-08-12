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
        self.startbutton_container.controls.append(self.starttext)

    def showControls(self):
        self.page.add(self.starttext_container)
        self.page.add(self.startbutton_container)
    
    def update(self):
        self.page.update()

    def createControls(self):
        self.starttext_container = Column()
        self.startbutton_container = Column()

    def __init__(self,page):
        self.page = page