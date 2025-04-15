#unused example classes; functionality not implemented yet
from __future__ import annotations
from LearnBotLib import LearnProfile

class VocabGER:
    def __init__(self):
        pass
    
class GrammarGER:
    def __init__(self):
        pass
    
      
class GermanProfile(LearnProfile):
    def __init__(self, user, lerningscore, grade, solvedVocabGER : list[VocabGER], solvedGrammarGER : list[GrammarGER], learnedVocabGER : list[VocabGER], learnedGrammarGER : list[GrammarGER]):
        #parent class __init__
        super().__init__(user, "ger", lerningscore, grade)
        
        #loaded from file
        self.solvedVocabGER : list[VocabGER] = solvedVocabGER
        self.solvedGrammarGER : list[GrammarGER] = solvedGrammarGER
        
        self.learnedVocabGER : list[VocabGER] = learnedVocabGER
        self.learnedGrammarGER : list[GrammarGER] = learnedGrammarGER