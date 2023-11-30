from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList, OneLineIconListItem, OneLineListItem
from kivymd.uix.button import MDTextButton
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from helper import screen_helper, toolbar_helper

import json

Window.size = (300, 500)

# импорт базы игр
with open('list_of_game.json', 'r', encoding='utf-8') as f:
    data = json.load(f)





# def on_start(self):
#     print('on_start work!')
#     for i in self.filt[0]:
#         item = OneLineIconListItem(text=i.strip())
#         self.root.ids.container.add_widget(item)

class MainScreen(Screen):


    def start(self):
        print('on_start work!')
        for i in DemoApp.filt[0]:
            item = OneLineListItem(text=i.strip())
            self.ids.container.add_widget(item)


class BookmarksScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen(name='menu'))
sm.add_widget(BookmarksScreen(name='bookmarks'))


class DemoApp(MDApp):

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

    def build(self):
        self.theme_cls.theme_style = 'Light'
        screen = Builder.load_string(screen_helper)
        return screen

    # def on_start(self):
    #     print('on_start work!')
    #     for i in self.filt[0]:
    #         item = OneLineIconListItem(text=i.strip())
    #         self.root.ids.container.add_widget(item)

DemoApp().run()
