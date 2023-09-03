import traceback
from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def DoAction(self):
        pass

class Steve(Character):
    def DoAction(self):
        print('*Копает алмезеры*')
class Alex(Character):
    def DoAction(self):
        print('*Охотится на свинок*')
class Jenny(Character):
    def DoAction(self):
        print('*Трахается с чедом*')
class Villager(Character):
    def DoAction(self):
        print('*Разводит гоев на шекели*')      

class World():
    def __init__(self,Player1,Player2,Player3,Player4): #И тут у нас проблемка, на вход можно подать всё что угодно: числа, строки, хоть говно
        Player1.DoAction()                              #Судя по методам мы хотим что бы в конструктор попали именно объекты типа Character
        Player2.DoAction()
        Player3.DoAction()
        Player4.DoAction()
        
class World1():
    def __init__(self,Player1: Character,Player2: Character,Player3: Character,Player4: Character): 
        Player1.DoAction()                              #А вот и клоунада, решаем проблемы динамической типизации тупо превратив её в статическую
        Player2.DoAction()
        Player3.DoAction()
        Player4.DoAction()
print('World')
try:                                                    #Самый клоунский вариант решения проблемы
    World(1,['hui','chiileeen'],'skovoroda',Villager()) #Вот пример того что мы можем подать всё что угодно
except Exception as e:
    print('Ошибка:\n', traceback.format_exc(),'\n')
                                                        #Вывод:
                                                        #Int не имеет метода DoAction
World(Alex(),Jenny(),Steve(),Villager())
                                                        #Вывод:
                                                        #*Охотится на свинок*
                                                        #*Копает алмезеры*
                                                        #*Разводит гоев на шекели*
                                                        #*Трахается с чедом*
input('Wait')
print('World1')
try:                                                    
    World1(1,['hui','chiileeen'],'skovoroda',Villager())
except Exception as e:
    print('Ошибка:\n', traceback.format_exc(),'\n')
                                                        #Вывод:
                                                        #Int не имеет метода DoAction
                                                        #Таже самая ошибка
                                                        #Тоесть типизация вообще не помогла
World1(Alex(),Jenny(),Steve(),Villager())
                                                        #Вывод:
                                                        #*Охотится на свинок*
                                                        #*Копает алмезеры*
                                                        #*Разводит гоев на шекели*
                                                        #*Трахается с чедом*
input('Wait')