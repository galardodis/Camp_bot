from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from datetime import datetime
import json
from kivy.lang import Builder


# импорт базы игр
with open('list_of_game.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


# Создание и восстановление заклодок
bookmarks = set()
with open('bookmarks.txt', 'r', encoding='utf-8') as b:
    for line in b.readlines():
        bookmarks.add(line.strip())

chosen_game = {'gname': 'gname', 'gtag': ['gtag'], 'gdescription': 'gdescription'}
print(data)


def app_filter(alf, *pattern):
    game_name = []
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
                    game_name.append(i['name'])
            else:
                game_name.append(i['name'])
        game_name = sorted(game_name)
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
                    game_name.append(i['name'])
            else:
                game_name.append(i['name'])
        game_name = sorted(game_name, reverse=True)
        print(len(game_name))
        return game_name


class MainScreen(Screen):
    def __init__(self, **kw):
        super(MainScreen, self).__init__(**kw)
        # создание слоев
        main_layout = BoxLayout(orientation='vertical', padding=0)
        layout_1 = BoxLayout(orientation='horizontal', padding=0, size_hint_y=0.05)
        layout_2 = GridLayout(cols=1, spacing=5, size_hint=(1, None))

        btn2 = Button(text='...', size_hint=(0.05, 1))
        btn1 = Button(text='Закладки', size_hint=(0.9, 1), on_release=button_pressed_bookmark)
        print(Window.height)
        print(Window.width)
        layout_2.bind(minimum_height=(layout_2.setter('height')))

        for i in app_filter('z-A', 'Командные игры'):
            btn = Button(text=i.strip(), size_hint_y=None,
                         height=30, on_release=self.button_pressed_game)
            layout_2.add_widget(btn)

        scroll = ScrollView(do_scroll_y=True)
        layout_1.add_widget(btn2)
        layout_1.add_widget(btn1)
        scroll.add_widget(layout_2)
        main_layout.add_widget(layout_1)
        main_layout.add_widget(scroll)

        self.add_widget(main_layout)

    # нажатие кнопки
    def button_pressed_game(self, instance):
        global NewGameWindow
        for i in data:
            if str(i['name']).upper().strip() == str(instance.text).upper().strip():
                chosen_game.clear()
                chosen_game['gname'] = i['name']
                chosen_game['gtag'] = i['tag']
                chosen_game['gdescription'] = i['description']
                sm.remove_widget(NewGameWindow)
                NewGameWindow = GameScreen(name='game_description')
                sm.add_widget(NewGameWindow)
                break
        set_screen('game_description')


class BookmarkScreen(Screen):
    def __init__(self, **kw):
        super(BookmarkScreen, self).__init__(**kw)
        # создание стиля
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))

        # заполнение кнопками
        btn1 = Button(text='Назад', size_hint_y=None,
                      height=30, on_release=lambda x: set_screen('main'))
        layout.add_widget(btn1)
        for i in bookmarks:
            btn = Button(text=i.strip(), size_hint_y=None,
                         height=30, on_release=self.bp_game)
            layout.add_widget(btn)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)
        self.add_widget(root)

    # нажатие кнопки
    def bp_game(self, instance):
        global NewGameWindow_FB
        for i in data:
            if str(i['name']).upper().strip() == str(instance.text).upper().strip():
                chosen_game['gname'] = i['name']
                chosen_game['gtag'] = i['tag']
                chosen_game['gdescription'] = i['description']
                sm.remove_widget(NewGameWindow_FB)
                NewGameWindow_FB = GameScreenFromBookmarks(name='gg')
                sm.add_widget(NewGameWindow_FB)
                break
        set_screen('gg')


    # нажатие кнопки закладка

def button_pressed_bookmark(instance):
    global NewBookmarkWindow
    sm.remove_widget(NewBookmarkWindow)
    NewBookmarkWindow = BookmarkScreen(name='game_bookmarks')
    sm.add_widget(NewBookmarkWindow)
    set_screen('game_bookmarks')


# экран с описанием игры
class GameScreen(Screen):
    def __init__(self, **kw):
        super(GameScreen, self).__init__(**kw)
        layout = BoxLayout(orientation='vertical', padding=0)
        layout_text = GridLayout(cols=1)
        layout.bind(minimum_height=layout.setter('height'))
        # 3 лэйбла
        btn1 = Button(text='Назад', size_hint_y=None,
                      height=30, on_release=lambda x: set_screen('main'))
        btn2 = Button(text='В закладки', size_hint_y=None,
                      height=30, on_release=self.add_bookmark)
        lb1 = Label(text=chosen_game['gname'], size_hint=(1, 0.1))
        # a = sorted(chosen_game['gtag'])
        lb2 = Label(text=', '.join(sorted(chosen_game['gtag'])), size_hint=(1, 0.1),
                    halign='center', valign='center', text_size=(Window.width, None))
        tex = Label(text=chosen_game['gdescription'], halign='center', valign='center',
                    text_size=(Window.width, None))
        # root = ScrollView(size_hint=(1, 0.8))
        # layout_text.add_widget(tex)
        # root.add_widget(tex)
        layout.add_widget(btn1)
        layout.add_widget(lb1)
        layout.add_widget(lb2)
        layout.add_widget(tex)
        layout.add_widget(btn2)
        self.add_widget(layout)

    def add_bookmark(self, *args):
        global bookmarks
        bookmarks.add(chosen_game['gname'])
        refresh_bookmarks_list()
        print(bookmarks)


# экран с описанием игры переход из закладок
class GameScreenFromBookmarks(Screen):
    def __init__(self, **kw):
        super(GameScreenFromBookmarks, self).__init__(**kw)
        layout = BoxLayout(orientation='vertical', padding=0)
        layout.bind(minimum_height=layout.setter('height'))
        # 3 лэйбла
        btn1 = Button(text='Назад', size_hint_y=None,
                      height=30, on_release=button_pressed_bookmark)
        btn2 = Button(text='Удалить из закладок', size_hint_y=None,
                      height=30, on_release=self.del_from_bookmarks)
        lb1 = Label(text=chosen_game['gname'], size_hint=(1, 0.1))
        lb2 = Label(text=', '.join(sorted(chosen_game['gtag'])), size_hint=(1, 0.1),
                    halign='center', valign='center', text_size=(Window.width, None))
        tex = Label(text=chosen_game['gdescription'], halign='center', valign='center',
                    text_size=(Window.width, None))
        # root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        layout.add_widget(btn1)
        layout.add_widget(lb1)
        layout.add_widget(lb2)
        layout.add_widget(tex)
        layout.add_widget(btn2)
        # root.add_widget(layout)
        self.add_widget(layout)

    def del_from_bookmarks(self, instance):
        print(bookmarks)
        # print(instance.text)
        bookmarks.discard(chosen_game['gname'])
        refresh_bookmarks_list()
        print(bookmarks)





def refresh_bookmarks_list():
    with open('bookmarks.txt', 'w', encoding='utf-8') as f:
        for i in bookmarks:
            f.write(i + '\n')

# Создание экранов
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
NewGameWindow = GameScreen(name='game_description')
NewBookmarkWindow = BookmarkScreen(name='game_bookmark')
NewGameWindow_FB = GameScreenFromBookmarks(name='gg')

def set_screen(name_screen):
    sm.current = name_screen


class MyApp(App):
    def __init__(self, **kvargs):
        super(MyApp, self).__init__(**kvargs)
        self.config = ConfigParser()

    # def build_config(self, config):
    #     config.adddefaultsection('General')
    #     config.setdefault('General', 'user_data', '{}')

    # def set_value_from_config(self):
    #     self.config.read(os.path.join(self.directory, '%(appname)s.ini'))
    #     self.user_data = ast.literal_eval(self.config.get(
    #         'General', 'user_data'))

    def get_application_config(self):
        return super(MyApp, self).get_application_config(
            '{}/%(appname)s.ini'.format(self.directory))

    def build(self):
        return sm


if __name__ == '__main__':
    MyApp().run()
    #
    # spin = Spinner(
    #     # default value shown
    #     text='Фильтр',
    #     # available values
    #     values=('Индивидуальные задания', 'Игры на улице', 'Игры в помещении',
    #             'Игры для 2-х игроков', 'Эстафеты', 'Общелагерные игры', 'Командные игры',
    #             'Библейские уроки', 'Игры с залом', 'Когда ничего нет под рукой',
    #             'Игры на знакомство', 'Конкурсы'),
    #     # just for positioning in our example
    #     size_hint=(None, None),
    #     size=(100, 44),
    #     pos_hint={'center_x': .5, 'center_y': .5})
