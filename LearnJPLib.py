from __future__ import annotations
from LearnBotLib import LearnProfile

class VocabJP:
    def __init__(self):
        pass
    
class Kanji:
    def __init__(self):
        pass
    
class Hiragana:
    def __init__(self):
        pass

class Katakana:
    def __init__(self):
        pass
    
class GrammarJP:
    def __init__(self):
        pass
    
class JapaneseProfile(LearnProfile):
    def __init__(self, user, lerningscore, grade, solvedVocabJP : list[VocabJP], solvedKanji : list[Kanji], solvedHiragana : list[Hiragana], solvedKataka : list[Katakana], solvedGrammarJP : list[GrammarJP], learnedVocabJP : list[VocabJP], learnedKanji : list[Kanji], learnedHiragana : list[Hiragana], learnedKataka : list[Katakana], learnedGrammarJP : list[GrammarJP]):
        #parent class __init__
        super().__init__(user, "jp", lerningscore, grade)
        
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