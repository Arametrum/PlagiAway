import DataReader as dr
import Fingerprints as fp
import Comparison as cp
import Testing
import Analysis as an
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class InputData:
    plainSusPath = ""
    plainCompPath = ""

    parSusPath = ""
    parCompPath = ""

class WindowManager(ScreenManager):
    pass

class MainWindow(Screen):
    pass

class ModeSelectWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_dropfile = self.dropfile)

    def plain(self):
        self.manager.get_screen("plainSus").ids["plainSusFile"].text = ""

    def par(self):
        self.manager.get_screen("parSus").ids["parSusFile"].text = ""

    def dropfile(self, window, path):
        self.manager.get_screen("plainSus").ids["plainSusFile"].text = path
        self.manager.get_screen("parSus").ids["parSusFile"].text = path
        self.manager.get_screen("plainComp").ids["plainCompFile"].text = path
        self.manager.get_screen("parComp").ids["parCompFile"].text = path
    pass

#Paragraph-stuctured file reading
class ParSusWindow(Screen):
    def select(self):
        self.manager.get_screen("parComp").ids["parCompFile"].text = ""
        InputData.parSusPath = self.ids["parSusFile"].text
    pass

#Paragraph-stuctured file reading
class ParCompWindow(Screen):
    def select(self):
        InputData.parCompPath = self.ids["parCompFile"].text
    pass

#Plain file reading
class PlainSusWindow(Screen):
    def select(self):
        self.manager.get_screen("plainComp").ids["plainCompFile"].text = ""
        InputData.plainSusPath = self.ids["plainSusFile"].text

    pass

#Plain file reading
class PlainCompWindow(Screen):
    def select(self):
        InputData.test.plainCompPath = self.ids["plainCompFile"].text

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