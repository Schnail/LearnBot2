from __future__ import annotations
from LearnBotLib import LanguageProfile
from Vector import Vector2d

class VocabJP:
    def __init__(self, eng : str, vector : Vector2d):
        self.jp : str = ""
        self.eng : str = eng
        self.romaji : str = ""
        self.example : str = ""
        self.vector : Vector2d = vector   
    
class Kanji:
    def __init__(self, sym : str, vector : Vector2d):
        self.sym : str = ""
        self.meaning : str = sym
        self.on : list[str] = []
        self.kun : list[str] = []
        
        self.vector : Vector2d = vector  
    
class Hiragana:
    def __init__(self, sym : str, vector : Vector2d):
        self.sym : str = sym
        self.sound : str = ""
        self.vector : Vector2d = vector 

class Katakana:
    def __init__(self, sym : str, vector : Vector2d):
        self.sym : str = sym
        self.sound : str = ""
        self.vector : Vector2d = vector 
    
class GrammarJP:
    def __init__(self):
        pass
    
class JapaneseProfile(LanguageProfile):
    def __init__(self, learningscore, grade, solvedVocabJP : list[VocabJP], solvedKanji : list[Kanji], solvedHiragana : list[Hiragana], solvedKataka : list[Katakana], solvedGrammarJP : list[GrammarJP], learnedVocabJP : list[VocabJP], learnedKanji : list[Kanji], learnedHiragana : list[Hiragana], learnedKataka : list[Katakana], learnedGrammarJP : list[GrammarJP]):
        #parent class __init__
        super().__init__("jp", learningscore, grade)
        
        #loaded from file
        self.solvedVocabJP : list[VocabJP] = solvedVocabJP
        self.solvedKanji : list[Kanji] = solvedKanji
        self.solvedHiragana : list[Hiragana] = solvedHiragana
        self.solvedKataka : list[Katakana] = solvedKataka
        self.solvedGrammarJP : list[GrammarJP] = solvedGrammarJP
        
        self.learnedVocabJP : list[VocabJP] = learnedVocabJP
        self.learnedKanji : list[Kanji] = learnedKanji
        self.learnedHiragana : list[Hiragana] = learnedHiragana
        self.learnedKataka : list[Katakana] = learnedKataka
        self.learnedGrammarJP : list[GrammarJP] = learnedGrammarJP    