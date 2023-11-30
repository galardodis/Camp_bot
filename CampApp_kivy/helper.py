screen_helper = """
ScreenManager:
    MainScreen:
    BookmarksScreen:
    SettingsScreen

<MainScreen>:
    start: root.start()
    name: 'menu'
    Screen:
        NavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: str(app.filt[1])
                            left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                            elevation: 10
                        ScrollView:
                            MDList:
                                id: container    
                        MDTextField:
                            hint_text: 'Найти'
                            size_hint_x: .8
                            pos_hint: {'center_x': .5, 'center_y': 1}
                           
                           
            MDNavigationDrawer:
                id: nav_drawer

                ContentNavigationDrawer:
                    orientation: 'vertical'
                    padding: "8dp"
                    spacing: "8dp"

                    ScrollView:
                        DrawerList:
                            id: md_list

                            MDList:
                                OneLineIconListItem:
                                    text: "Закладки"
                                    on_release: print('Закладки')

                                    IconLeftWidget:
                                        icon: "bookmark"
                                        on_release: root.manager.current = 'bookmarks'

                                OneLineIconListItem:
                                    text: "Что-то"
                                    on_release: print('Что-то')

                                    IconLeftWidget:
                                        icon: "upload"
                                        on_release: print('Что-то')


                                OneLineIconListItem:
                                    text: "Настройки"
                                    on_release: print('Настройки')

                                    IconLeftWidget:
                                        icon: "settings"
                                        on_release: print('Настройки')

<BookmarksScreen>:
    
    name: 'bookmarks'
    Screen:
        NavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'

                        MDToolbar:
                            title: 'BookmarksScreen'
                            left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                            elevation: 10
                        ScrollView:
                            MDList:
                                id: container
                        MDTextField:
                            hint_text: 'Найти'
                            size_hint_x: .8
                            pos_hint: {'center_x': .5, 'center_y': 1}

            MDNavigationDrawer:
                id: nav_drawer

                ContentNavigationDrawer:
                    orientation: 'vertical'
                    padding: "8dp"
                    spacing: "8dp"

                    ScrollView:
                        DrawerList:
                            id: md_list

                            MDList:
                                OneLineIconListItem:
                                    text: "Закладки"
                                    on_release: print('Закладки')

                                    IconLeftWidget:
                                        icon: "bookmark"
                                        on_release: root.manager.current = 'menu'

                                OneLineIconListItem:
                                    text: "Что-то"
                                    on_release: print('Что-то')

                                    IconLeftWidget:
                                        icon: "upload"
                                        on_release: print('Что-то')


                                OneLineIconListItem:
                                    text: "Настройки"
                                    on_release: print('Настройки')

                                    IconLeftWidget:
                                        icon: "settings"
                                        on_release: print('Настройки')

"""
toolbar_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    
                    MDToolbar:
                        title: 'Количество игр'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 10
                    ScrollView:
                        MDList:
                            id: container
                    MDToolbar:
                        title: 'Поиск по имени'
                        
        MDNavigationDrawer:
            id: nav_drawer
            
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"

                ScrollView:
                    DrawerList:
                        id: md_list
                        
                        MDList:
                            OneLineIconListItem:
                                text: "Закладки"
                                on_press: print('Закладки')
                                
                                IconLeftWidget:
                                    icon: "bookmark"
                                    on_press: root.manager.current = 'profile'
                                      
                            OneLineIconListItem:
                                text: "Что-то"
                                on_press: print('Что-то')
                            
                                IconLeftWidget:
                                    icon: "upload"
                                    on_press: print('Что-то')
                                    
                           
                            OneLineIconListItem:
                                text: "Настройки"
                                on_press: print('Настройки')
                            
                                IconLeftWidget:
                                    icon: "settings"
                                    on_press: print('Настройки')
"""

