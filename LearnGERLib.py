#unused example classes; functionality not implemented yet
from __future__ import annotations
from LearnBotLib import LanguageProfile

class VocabGER:
    def __init__(self):
        pass
    
class GrammarGER:
    def __init__(self):
        pass
    
      
class GermanProfile(LanguageProfile):
    def __init__(self, learningscore, grade, solvedVocabGER : list[VocabGER], solvedGrammarGER : list[GrammarGER], learnedVocabGER : list[VocabGER], learnedGrammarGER : list[GrammarGER]):
        #parent class __init__
        super().__init__("ger", learningscore, grade)
        
        #loaded from file
        self.solvedVocabGER : list[VocabGER] = solvedVocabGER
        self.solvedGrammarGER : list[GrammarGER] = solvedGrammarGER
        
        self.learnedVocabGER : list[VocabGER] = learnedVocabGER
        self.learnedGrammarGER : list[GrammarGER] = learnedGrammarGER