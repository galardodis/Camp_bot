from kivy.app import App
from kivymd.uix.navigationdrawer import NavigationLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList, OneLineIconListItem
from kivymd.uix.button import MDTextButton
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from helper import screen_helper, toolbar_helper

import json

Window.size = (300, 500)

# импорт базы игр
with open('list_of_game.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

class DemoApp(App):

    def app_filter(alf, *pattern):
        filtered_game = []
        if alf == 'A-z':
            for i in data:
                if pattern:
                    for pat in pattern:
                        if pat in i['tag']:
                            add = True
                        else:
                            add = False
                        if not add:
                            break
                    if add:
                        filtered_game.append(i['name'])
                else:
                    filtered_game.append(i['name'])
            filtered_game = sorted(filtered_game)
        if alf == 'z-A':
            for i in data:
                if pattern:
                    for pat in pattern:
                        if pat in i['tag']:
                            add = True
                        else:
                            add = False
                        if not add:
                            break
                    if add:
                        filtered_game.append(i['name'])
                else:
                    filtered_game.append(i['name'])
            filtered_game = sorted(filtered_game, reverse=True)
            num_game = len(filtered_game)
            print(len(filtered_game))
            return [filtered_game, num_game]
    filt = app_filter('z-A')

    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass


    def on_start(self):
        print('on_start work!')
        for i in self.filt[0]:
            item = OneLineIconListItem(text=i.strip())
            self.root.ids.container.add_widget(item)

DemoApp().run()
