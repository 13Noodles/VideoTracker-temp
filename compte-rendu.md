# 1. Besoin & exigence
|N° Besoin|N° Exigence|Besoin|Exigence|
|:-------:|:---------:|------|--------|
|    1    |     1     |Enregistrer les données acquises au cours du pointage (temps, positionX, positionY) au format csv avec le séparateur point-virgule (cahier des charges)|Le logiciel doit pouvoir enregistrer les données qu'il a accumulé (temps, positionX, positionY) au format csv avec le séparateur point-virgule|
|    ⇧    |     2     |⇧|Le logiciel doit être capable de detecter si une erreur à lieu quand l'utilisateur lui demande d'enregistrer ses données|
|    ⇧    |     3     |⇧|Des tests doivent vérifier le bon fonctionnement des différentes fonctions du logiciel|

# 2. Les taches (qui sont aussi dans l'issue #1)

|N° Besoin|N° Exigence | N° tache | Description de la tache | commentaire |Assigné à| temps estimé | temps effectif |
|:-------:|:----------:|:--------:|-------------------------|:-----------:|:-------:|:------------:|:--------------:|
|    1    |      1     |     1    |Créer une classe Point qui a pour propriétés `x` et `y`| |N.Houalet| | |
|    1    |      1     |     2    |Ajouter au constructeur de `Point`  les arguments `x` et `y`. leurs valeurs devont être assigné aux propriétés du même nom du `Point`| |⇧| | |
|    1    |      1     |     3    |Ajouter à la classe Point le getter `getX(self) -> float`| |⇧| | |
|    1    |      1     |     4    |Ajouter à la classe Point le getter `getY(self) -> float`| |⇧| | |
|    1    |      1     |     5    |Créer une classe `FileRepo`| |⇧| | |
|    1    |      1     |     6    |Ajouter à la classe `FileRepo` la méthode `transformDataToCSV`|`transformDataToCSV` prendra en argument deux array de même taille, un contenant des Point, un contenant des Int. savePath sera le chemin de destination du fichier exporté, il inclura le chemin des dossiers+le nom du fichier+son extension. le formatage du fichier sauvegardé devra utilisé des ";" comme séparateur et être  de la forme : `\|temps\|positionX\|positionY\|`|
| |⇧| |
|    1    |      1     |     7    |Ajouter une propriété `saveDir:str` au Model| |⇧| | |
|    1    |      1     |     8    |Ajouter une propriété `points:list[Point]` au Model| |⇧| | |
|    1    |      1     |     9    |Ajouter une propriété `temps:list[int]`| |⇧| | |
|    1    |      1     |    10    |Ajouter une propriété `fileRepo:FileRepo` au Model| |⇧| | |
|    1    |      1     |    11    |Ajouter au constructeur du Model un argument `defaultSaveDir` qui aura par defaut la valeur "saves". Le constructeur devra assigner `defaultSaveDir` à `saveDir`.
| |⇧| | |
|    1    |      1     |    12    |Ajouter une méthode `getPoint(pointId:int)->Point` au Model la méthode devra renvoyer le Point correspondant à pointId ou `None` si il n'y a pas de point avec cet id| |⇧| | |
|    1    |      1     |    13    |Ajouter une méthode `getTemps(tempsId:int)->int` au Model| la méthode devra renvoyer l'int (temps) correspondant à tempsId ou `None` si il n'y a pas de temps avec cet id| |⇧| | |
|    1    |      1     |    14    |Ajouter une méthode `exportToCSV(filename:str)` au `Model`|cette fonction appellera `FileRepo.transformDataToCSV` en lui donnant trois arguments : l'array de Point stocké dans une des propriété du Model, l'array d'Int stocké dans une des propriété du Model,le chemin où sera sauvegardé le fichier exporté. Ce chemin sera formé en utilisant la propriété `saveDir` du model et l'argument `filename`.|⇧| | |
|    1    |      1     |    15    |Ajouter une fonction `RandomPoints(n:int) -> list[Point]` dans le fichier test.py| Cette fonction créera une liste de points aléatoire pour les tests| |⇧| |
|    1    |      1     |    16    |Ajouter un test pour vérifier que les méthodes en lien avec les Points et temps dans le `Model` fonctionnent bien| |⇧| | |
|    1    |      1     |    16    |Ajouter un test pour vérifier que `FileRepo.transformDataToCSV` fonctionne quand on lui donne des valeurs correctes| |⇧| | |
|    1    |      1     |    16    |Ajouter un test pour vérifier que `FileRepo.transformDataToCSV` tente bien de créer des dossier pour récupérer certaines erreurs de chemin invalide.| |⇧| | |
|    1    |      1     |    16    |Ajouter une méthode `addPoint(x: int, y: int, t: int)` au model| |⇧| | |
|    1    |      1     |    16    |Ajouter une méthode `getPointCount` au model| |⇧| | |
