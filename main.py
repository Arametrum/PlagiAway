import DataReader as dr
import Fingerprints as fp
import Comparison as cp
import Testing
import Analysis as an
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class WindowManager(ScreenManager):
    pass

class MainWindow(Screen):
    pass

class ModeSelectWindow(Screen):
    pass

#Paragraph-stuctured file reading
class ParFileWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_dropfile = self.onFileDrop)

    def onFileDrop(self, window, file_path):
        self.ids["parSusFile"].text = file_path
    pass

#Plain file reading
class PlainFileWindow(Screen):
    def plainSelect(self):
        tmp = self.ids.plainSusFile.text

    pass

#Results for entire par.-struct. file
class ParFileResultsWindow(Screen):
    pass

class PlainResultsWindow(Screen):
    pass

#List of results for each paragraph
class ParSingleResultsWindow(Screen):
    pass

#List of matched strings for chosen paragraph
class ParMatchedStringsWindow(Screen):
    pass

#List of matched strings for entire plain file
class PlainMatchedStringsWindow(Screen):
    pass

kv = Builder.load_file("gui.kv")

class RunningApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    RunningApp().run()