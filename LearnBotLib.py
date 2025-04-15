from __future__ import annotations
import discord
import math


class LearnBotSystem:
    def __init__(self):
        #CacheMemorie
        self.active : list[ExerciseCard] = []
        self.inactive : list[ExerciseCard] = []
        self.pendingKill : list[KillCard] = []
        self.pendingInfo : list[InfoCard] = []
        
        
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
        
        self.exercise

    
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


#LearnProfile Classes

#used to derive language specific objects; This object shouldn't be created
class LearnProfile:
    def __init__(self, language : str, user : discord.User, lerningscore : float, grade : int):
        self.LANGUAGE : str = language
        
        #loaded from file
        self.user : discord.user = user
        self.lerningscore : float 
        self.grade : int
        
        #only stored in cache, never loaded from file
        self.pendingExercise : list[ExerciseCard] = []
        self.pendingKill : list[KillCard] = []
        self.pendingInfo : list[InfoCard] = []


#testing area     
if __name__ == "__main__":
    pass
        