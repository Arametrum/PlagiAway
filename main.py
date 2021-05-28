import DataReader as dr
import Fingerprints as fp
import Comparison as cp
import Testing
import Analysis as an
import os.path
import random
from datetime import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
import re

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


    def computePar():
        InputData.parSusFile = dr.readByParagraphs(InputData.parSusPath)
        InputData.parCompFile = dr.readByParagraphs(InputData.parCompPath)

        InputData.parRes = an.analyseParagraphComp(Testing.multFprintParagraph(InputData.parSusFile, InputData.parCompFile))
        InputData.parResOffset = an.analyseParagraphComp(Testing.offsetFprintParagraph(InputData.parSusFile, InputData.parCompFile))

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
            self.manager.get_screen("parFileRes").ids["par4FileAver"].text = str(InputData.parRes[0][1])
            self.manager.get_screen("parFileRes").ids["par4FileHigh"].text = str(InputData.parRes[0][2])
            self.manager.get_screen("parFileRes").ids["par5FileAver"].text = str(InputData.parRes[1][1])
            self.manager.get_screen("parFileRes").ids["par5FileHigh"].text = str(InputData.parRes[1][2])

            self.manager.get_screen("parOffset").ids["par4OffAver"].text = str(InputData.parResOffset[0][1])
            self.manager.get_screen("parOffset").ids["par4OffHigh"].text = str(InputData.parResOffset[0][2])
            self.manager.get_screen("parOffset").ids["par5OffAver"].text = str(InputData.parResOffset[1][1])
            self.manager.get_screen("parOffset").ids["par5OffHigh"].text = str(InputData.parResOffset[1][2])

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

            self.manager.get_screen("plainOffset").ids["plain4OffAver"].text = str(InputData.plainResOffset[0][0])
            self.manager.get_screen("plainOffset").ids["plain4OffHigh"].text = str(InputData.plainResOffset[0][1])
            self.manager.get_screen("plainOffset").ids["plain5OffAver"].text = str(InputData.plainResOffset[1][0])
            self.manager.get_screen("plainOffset").ids["plain5OffHigh"].text = str(InputData.plainResOffset[1][1])

            self.manager.current = "plainRes"
            

    def ret(self):
        self.manager.get_screen("plainSus").ids["plainSusFile"].text = ""
    pass

#Results for entire par.-struct. file
class ParFileResultsWindow(Screen):
    def details(self):
        self.manager.get_screen("parSingleRes").ids["parSinRes"].clear_widgets()

        for index, parAver in enumerate(InputData.parRes[0][0][0]):
            parText = "Paragraph " + str(index + 1)

            text4 = "4 word substrings\nAverage overlap: " + str(parAver)[:4]
            text4 += "\nHighest overlap:" + str(InputData.parRes[0][0][1][index])[:4]

            text5 = "5 word substrings\nAverage overlap: " + str(InputData.parRes[1][0][0][index])[:4]
            text5 += "\nHighest overlaps" + str(InputData.parRes[1][0][1][index])[:4]

            self.manager.get_screen("parSingleRes").ids["parSinRes"].add_widget(Label(size_hint_y = None, text = parText))
            self.manager.get_screen("parSingleRes").ids["parSinRes"].add_widget(Label(size_hint_y = None, text = text4))
            self.manager.get_screen("parSingleRes").ids["parSinRes"].add_widget(Label(size_hint_y = None, text = text5))
            self.manager.get_screen("parSingleRes").ids["parSinRes"].add_widget(Button(text = "PARAGRAPH " + str(index + 1) + " \nDETAILS", size_hint_y = None, on_release = self.parDetails))
            


    def parDetails(self, instance):
        parNum = int(re.match("\D*(?P<num>\d*)\D*", instance.text).group("num")) - 1
        tmp = ""

        for string in InputData.parRes[0][0][2][parNum]:
            tmp += string + "\n"

        for string in InputData.parRes[1][0][2][parNum]:
            tmp += string + "\n"

        self.manager.get_screen("parString").ids["parStrings"].text = tmp
        self.manager.current = "parString"
    pass

class ParOffsetWindow(Screen):
    def details(self):
        self.manager.get_screen("parSingleOff").ids["parSinOff"].clear_widgets()

        for index, parAver in enumerate(InputData.parResOffset[0][0][0]):
            parText = "Paragraph " + str(index + 1)

            text4 = "4 word substrings\nAverage overlap: " + str(parAver)[:4]
            text4 += "\nHighest overlap:" + str(InputData.parResOffset[0][0][1][index])[:4]

            text5 = "5 word substrings\nAverage overlap: " + str(InputData.parResOffset[1][0][0][index])[:4]
            text5 += "\nHighest overlaps" + str(InputData.parResOffset[1][0][1][index])[:4]

            self.manager.get_screen("parSingleOff").ids["parSinOff"].add_widget(Label(size_hint_y = None, text = parText))
            self.manager.get_screen("parSingleOff").ids["parSinOff"].add_widget(Label(size_hint_y = None, text = text4))
            self.manager.get_screen("parSingleOff").ids["parSinOff"].add_widget(Label(size_hint_y = None, text = text5))
            self.manager.get_screen("parSingleOff").ids["parSinOff"].add_widget(Button(size_hint_y = None, id = index, text = "PARAGRAPH\nDETAILS"))

    pass

class PlainResultsWindow(Screen):
    def details(self):
        #self.manager.get_screen("plainString").ids["plainBox"].clear_widgets()

        numOfElements = len(InputData.plainRes[0][2]) + len(InputData.plainRes[1][2])
        tmp = ""

        for string in InputData.plainRes[0][2]:
            tmp += string + "\n"

        for string in InputData.plainRes[1][2]:
            tmp += string + "\n"

        #lab = Label(text = tmp)

        self.manager.get_screen("plainString").ids["plainBox"].text = tmp
    pass

class PlainOffsetWindow(Screen):
    def details(self):
        #self.manager.get_screen("plainStringOff").ids["plainBoxOff"].clear_widgets()

        numOfElements = len(InputData.plainRes[0][2]) + len(InputData.plainRes[1][2])
        tmp = ""

        for string in InputData.plainResOffset[0][2]:
            tmp += string + "\n"

        for string in InputData.plainResOffset[1][2]:
            tmp += string + "\n"

        #lab = Label(text = tmp)

        self.manager.get_screen("plainStringOff").ids["plainBoxOff"].text = tmp
    pass

#List of results for each paragraph
class ParSingleResultsWindow(Screen):
    pass

class ParSingleOffsetWindow(Screen):
    pass

#List of matched strings for chosen paragraph
class ParMatchedStringsWindow(Screen):
    pass

class ParMatchedOffsetWindow(Screen):
    pass

#List of matched strings for entire plain file
class PlainMatchedStringsWindow(Screen):
    pass

class PlainMatchedOffsetWindow(Screen):
    pass

kv = Builder.load_file("gui.kv")

class RunningApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    random.seed(datetime.now())
    RunningApp().run()