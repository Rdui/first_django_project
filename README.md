
Project plan
==================

Project description:
____________________________
Online game store for JavaScript games

Technologies:
____________________________
Django, JavaScript, HTML5, CSS, Bootstrap

Group Webornio:
Henrik Hartiala, henrik.hartiala@student.tut.fi, 211528
Tommi Nikula, tommi.nikula@student.tut.fi, 240341
Juho Vähätalo, juho.vahatalo@student.tut.fi, 240549
Rudi Ritosalo, rudi.ritosalo@student.tut.fi, 240111


## Implementation of features


Authentication
____________________________
Different kind of users are implemented by extending Django’s default User model. User types include player and developer. 
Views: registration and logging in.

Basic player functionalities
----------------------------

A player can buy and play games, see game high scores and record their high scores. Games are categorized by tags added by the developer and players can search games using tags. 
Views: gameplay, game list/search, buy game

Basic developer functionalities
-------------------------------
A developer can add a game by giving an URL. A developer can set a price for the game and modify the game.
Views: Add game, modify game, sales statistics

Optional functionalities that we plan to implement
--------------------------------------------------
* 3rd party login
* save/load and resolution feature
* RESTful API
* Mobile friendly
* Social media sharing
* Testing your service with other groups games
* Profile page which shows that users owned games and highscores to those games (if any)
* Rating games: As an owner of a precise game, you may rate it 1-5 stars. Rating of the game will show in the gamelist and you can order the games in the list by rating.

Working plan
----------------------------------------
We will meet face-to-face as a group at least 1-2 times a week. We will use Trello for project planning and management (already in use: Assistant can check our trello at: https://trello.com/b/BCTaupB8). Telegram is also used for communication and arranging meetings. 






Implementation order / Timetable
---------------------------------------
1. Get to know to the project and plan the project
2. Get the tools&enviroment ready for all participants
3. Setup the project
4. Model for users and views for login and registeration
5. Plan all the models
6. Implement models in a logical order
7. Plan and implement view for gamelisting and game description
8. Plan and implement the payment service
9. Plan the optional features
10. Implement optional features
* Update plan/trello
(*timeless)

