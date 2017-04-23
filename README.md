
Project plan
==================

## Project description:

Online game store for JavaScript games

## Technologies:
Django, JavaScript, HTML5, CSS, Bootstrap

## Group Webornio:
* Henrik Hartiala, henrik.hartiala@student.tut.fi, 211528
* Tommi Nikula, tommi.nikula@student.tut.fi, 240341
* Juho Vähätalo, juho.vahatalo@student.tut.fi, 240549
* Rudi Ritosalo, rudi.ritosalo@student.tut.fi, 240111


## Implementation of features


### Authentication
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
 
*Update plan/trello(timeless)*



Final submission
---------------------------------------
What features you implemented and how much points do you think you should get for those? You must do this by giving a link to your group’s filled copy of the Project Demonstration document. For info about the Project Demonstration document, go to Before the Demonstration, creating the Project Demonstration document under Project Demonstrations heading that comes after this.
Implemented features and estimated points (X = feature implemented):

Mandatory requirements
1) Basic requirements 10/11:
	X a)Valid CSS and HTML
	X b)The service should work on modern browsers
	X c)Code should be commented well
	X d)Write your own code
	X e)Reusability
	X f)Modularity
	X g)Versatile use of Django’s features
	X h)Sensible URL scheme
	X i)Security
	X j)Crash & idiot proof
	k)Register as a player and developer
2)Authentication (100-200 Points) 0/2:
	a)Login, logout and register, both as player or developer
	b)Email validation
3)Basic player functionalities(100-300 Points)
	X a)As a player: buy games
	X b)As a player: play games
	c)As a player: see game high scores and record their score to it
	d)As a player: Payment is handled by a mockup payment service: 
	e)As a player: Security restrictions, e.g. player is only allowed to play the games they’ve purchased
	f)As a player: How your players find games (are they in a category, is there a search functionality?)
4)Basic developer functionalities(100-200 Points)
	a)As a developer: Add a game (URL) and set price for that game and manage that game (remove, modify)
	b)As a developer: Basic game inventory and sales statistics (how many of the developers' games have been bought and when)
	c)As a developer: Security restrictions, e.g. developers are only allowed to modify/add/etc. their own games, developer can only add games to their own inventory, etc
5)Game/service interaction (100-200 Points)
	a)When player has finished playing a game (or presses submit score), the game sends a postMessage to the parent window containing the current score. This score must be recorded to the player's scores and to the global high score list for that game. See section on Game Developer Information for details.
	b)Messages from service to the game must be implemented as well
6)Quality of Work (100-200 Points)
	a)Quality of code (structure of the application, comments)
	b)Purposeful use of framework (Don't-Repeat-Yourself principle, Model-View-Template separation of concerns)
	c)User experience (styling, interaction)
	d)Meaningful testing
7)Non-functional requirements (100-200 Points)
	a)Project plan
	b)Overall documentation, demo, teamwork, and project management as seen from the history of your GitLab project (and possible other sources that you submit in your final report)
8)Own JavaScript game(s) (100-300 Points)
	a)Communicates with the service (the game has to use at least these three service features: high score, save, load)
	b)Technical quality of the game (code, comments, communication with the game store)
	c)Non-technical qualities of the game AKA the fun factor



Where do you feel that you were successful and where you had most problems. Give sufficient details, this will influence the non-functional points awarded.
How did you divide the work between the team members - who did what? Was the work divided equally? If someone was supposed to do something, but didn’t, mark this down, too.
Instructions how to use your application and link to Heroku where it is deployed.
If a specific account/password (e.g. game developer) is required to try out and test some aspects of the work, please provide the details
Update your project plan to reflect what was done. Just be honest, this course is about learning.
Make sure your names, emails and student IDs are in the document. Just to be sure. :-)
