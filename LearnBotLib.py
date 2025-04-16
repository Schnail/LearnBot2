from __future__ import annotations
import discord
import os
import json
import math

#language classes objects

class LearnBotSystem:
    def __init__(self, languages : str):
        #CacheMemorie
        self.languages : list[str] = languages
        self.dictionary : dict = {}
        
        self.profiles : list[LearnProfile] = []
        self.active : list[ExerciseCard] = []
        self.inactive : list[ExerciseCard] = []
        self.pendingKill : list[KillCard] = []
        self.pendingInfo : list[InfoCard] = []
        
        self.maxProfiles : int = 10
        self.maxActive : int = 10
        self.maxInactive : int = 20
        self.maxPendingKill : int = 20
        self.maxPendingInfo : int = 40
        
    def loadDictionary(self):
        pass
        
#Exercise Classes

class Exercise:
    def __init__(self):
        pass


#Card Classes
       
class Card:
    def __init__(self, content : CardContent):
        self.message : discord.Message
        self.content : CardContent = content

       
class ExerciseCard(Card):
    def __init__(self, content, exercise):
        #parent class __init__
        super().__init__(content)
        
        self.exercise : Exercise = exercise

    
class KillCard(Card):
    def __init__(self, content):
        #parent class __init__
        super().__init__(content)

    
class InfoCard(Card):
    def __init__(self, content):
        #parent class __init__
        super().__init__(content)

    
class CardContent:
    def __init__(self):
        pass
    
    def embed(self) -> discord.Embed:
        pass

class LearnProfile:
    def __init__(self, user : discord.User):
        self.user : discord.User = user
        self.userID : int = user.id
        self.languageProfiles : list[LanguageProfile] = []
        
    def loadLanguageProfile(self, language : str) -> LanguageProfile:
        pass
        
        

#used to derive language specific objects; This object shouldn't be created
class LanguageProfile:
    def __init__(self, language : str, parent : LearnProfile,  learningscore : float, grade : int):
        self.LANGUAGE : str = language
        self.learnprofile: LearnProfile = parent
        
        #loaded from file
        self.learningscore : float
        self.grade : int
        
        #only stored in cache, never loaded from file
        self.pendingExercise : list[ExerciseCard] = []
        self.pendingKill : list[KillCard] = []
        self.pendingInfo : list[InfoCard] = []


#testing area     
if __name__ == "__main__":
    pass
        