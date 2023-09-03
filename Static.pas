
type 
  Character = abstract class //объявляем абстрактный класс от которого у нас будет всё наследоватся, он нам пригодится
    constructor();
    begin
    end;
    procedure DoAction(); virtual;
    begin
      Println('Idk');
    end;
  end;
  Steve = class(Character)
    procedure DoAction(); override;
    begin
      println('*Копает алмезеры*');
    end;  
  end;
  Alex = class(Character)
    procedure DoAction(); override;
    begin
      println('*Охотится на свинок*');
    end;   
  end;
  Jenny = class(Character)
    procedure DoAction(); override;
    begin
      println('*Трахается с чедом*');
    end;    
  end;
  Villager = class(Character)
    procedure DoAction(); override;
    begin
      println('*Разводит гоев на шекели*');
    end;    
  end;
  
  World = class
    //constructor(Player1:steve;Player2:alex;Player3:jenny;Player4:villager) 
    //тут проблемка: вдруг у нас в мире будет 4 стива?
    //А вдруг мы захотим сделать в мире блядушник?
    //Но у нас не выйдет, тк игроки строго затипизированы
    constructor(Player1:character;Player2:character;Player3:character;Player4:character);
    //Что бы решить эту проблему нам пригодился тот самый абстрактный класс "Сharacter"
    //И проблема мигом решается
    begin
      Player1.DoAction;
      Player2.DoAction;
      Player3.DoAction;
      Player4.DoAction;
    end;
    //И что получается, что бы компенсировать топорность статической типизации
    //Нами пришлось напердолить абстрактный класс
    
    //В нашем случае код маленький и проблем не возникает
    //Но вдруг у нас большой проект, тогда придётся либо говнокодить либо
    //либо придётся пердоилть целуб иерархию (или как там называется?) абстрактных классов
  end;
  
begin
  new World(new Alex, new Steve, new Villager, new Jenny);
  //Вывод:
  //*Охотится на свинок*
  //*Копает алмезеры*
  //*Разводит гоев на шекели*
  //*Трахается с чедом*
end.  