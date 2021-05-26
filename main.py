import DataReader as dr
import Fingerprints as fp
import Comparison as cp
import Testing
import Analysis as an
import os.path
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class InputData:
    plainSusPath = ""
    plainCompPath = ""

    plainSusFile = []
    plainCompFile = []

    parSusPath = ""
    parCompPath = ""

    parSusFile = []
    parCompFile = []

    plainRes = 0
    parRes = 0

    plainResOffset = 0
    parResOffset = 0

    def computePlain():
        InputData.plainSusFile = dr.readFile(InputData.plainSusPath)
        InputData.plainCompFile = dr.readFile(InputData.plainCompPath)

        InputData.plainRes = an.analyseFileComp(Testing.multFingerprints(InputData.plainSusFile, InputData.plainCompFile))
        InputData.plainResOffset = an.analyseFileComp(Testing.offsetFingerprints(InputData.plainSusFile, InputData.plainCompFile))

        print(InputData.plainRes)
        print(InputData.plainResOffset)

    def computePar():
        InputData.parSusFile = dr.readByParagraphs(InputData.parSusPath)
        InputData.parCompFile = dr.readByParagraphs(InputData.parCompPath)

        InputData.parRes = an.analyseParagraphComp(Testing.multFprintParagraph(InputData.parSusFile, InputData.parCompFile))
        InputData.parResOffset = an.analyseParagraphComp(Testing.multFprintParagraph(InputData.parSusFile, InputData.parCompFile))

        print(InputData.parRes)
        print(InputData.parResOffset)
    pass

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

        if os.path.isfile(InputData.parSusPath):
            self.manager.current = "parComp"
    pass

#Paragraph-stuctured file reading
class ParCompWindow(Screen):
    def select(self):
        InputData.parCompPath = self.ids["parCompFile"].text

        if os.path.isfile(InputData.parCompPath):
            InputData.computePar()
            self.manager.current = "parFileRes"

    def ret(self):
        self.manager.get_screen("parSus").ids["parSusFile"].text = ""
    pass

#Plain file reading
class PlainSusWindow(Screen):
    def select(self):
        self.manager.get_screen("plainComp").ids["plainCompFile"].text = ""
        InputData.plainSusPath = self.ids["plainSusFile"].text

        if os.path.isfile(InputData.plainSusPath):
            self.manager.current = "plainComp"

    pass

#Plain file reading
class PlainCompWindow(Screen):
    def select(self):
        InputData.plainCompPath = self.ids["plainCompFile"].text

        if os.path.isfile(InputData.plainCompPath):
            InputData.computePlain()
            self.manager.get_screen("plainRes").ids["plain4ResAver"].text = str(InputData.plainRes[0][0])
            self.manager.get_screen("plainRes").ids["plain4ResHigh"].text = str(InputData.plainRes[0][1])
            self.manager.get_screen("plainRes").ids["plain5ResAver"].text = str(InputData.plainRes[1][0])
            self.manager.get_screen("plainRes").ids["plain5ResHigh"].text = str(InputData.plainRes[1][1])

            self.manager.current = "plainRes"
            

    def ret(self):
        self.manager.get_screen("plainSus").ids["plainSusFile"].text = ""
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