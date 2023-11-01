# Space Invaders!

In this exercise, we shall write a [space invaders](https://en.wikipedia.org/wiki/Space_Invaders) style game. Space Invaders was first released in 1978 and it was the first fixed shooter. Other games in the fixed shooter category that you may be familiar with are Galaxian, Centipede, and Galaga.

The game has a single screen or scene where the player controls a cannon that can move laterally on the screen. Directly above the player are four obstacles which can be used to protect the player from attack and limit the player's ability to shoot at the aliens.

The aliens are in a 5 by 11 grid and march slowly towards the player's cannon. As the player destroys aliens, the remaining alients march a little faster. The aliens shoot at the player and the player must avoid getting shot. Occasionally a red colored alien will fly across the top of the screen.

You can play the original [1978 Space Invaders game](https://archive.org/details/arcade_invaders) at the [Internet Archive](https://archive.org/)'s [Internet Arcade](https://archive.org/details/internetarcade).

An important detail is the soundtrack. It was the first game with a continuous background soundtrack. The four note soundtrack repeats slowly yet increases in tempo as fewer aliens remain on the screen.  

The shoot 'em up genre may not be as popular today as it was in the 1980s and 1990s however it is a great starting point for a student. A few of the technical challenges one can expect to confront with a shoot 'em up game are:

* How to determine when a bullet/laser intersects or collides with the player or enemy?
* How to animate the bullet/laser's movement?
* How to manage game state between the player's three lives?
* How to animate the player character, the non-player characters, and the enemies?

Remember, this assignment is an individual assignment where you are creating your own space invader game clone. 

Our space invader game shall have the following rules and requirements:

* The game must be written in Python using Pygame.

* The game must use object oriented design using the same principles from previous programming assignments. Projects which disregard this requirement will not be graded.

* The game must be graphical (not a text-based or text console game).

* The game must have at least one player (multi-player is at your discretion).

* The game may be controlled from the keyboard.

* The objective of the game is to score the highest score possible. Scores are increased by the number of aliens defeated and any additional power ups that are collected.

* The player has three lives at the start of every game. The player's character dies when an alien successfully shoots the player or the player collides with an alien. When the player's character dies, the player continues the game with a new player character until all the player's lives are exhausted.

* A player may earn additional lives by reaching specific scores. It is left to the student's discretion when to award extra lives.

* The player's character may only move laterally (left/right).

* The player's character shoots a laser that destroys aliens with a single shot. No alien requires multiple shots to be destroyed.

* There exists at least 2 obstacles between the player and the aliens. The obstacles are not required to be destructable like in the original game. The obstacles are permanent fixtures on the screen which cannot be destroyed or harmed by the aliens or the player character. Shots from the player or the aliens cannot pass through the obstacles. The position of the obstacles must be between the player and the aliens and left to your discretion. Aliens fly over the obstacle.

* The aliens present themselves as a grid. The original game used a gird of 5 by 11 aliens. At a minimum, the grid of aliens must be 4 by 4.

* The aliens march towards the player's position in a style similar to the original Space Invaders game.

* The aliens are visually distinct from the player's character. The aliens do not need to be visually distinct from one another.

* There is no requirement for bonus points or bonus opportunities like in the original game.

* The player scores a fixed number of points for every alien that is destroyed.

* Should the player destroy all the aliens, the game presents a cut scene which congratulates the player, waits for the player to press a key, and once pressed starts a new game where the score and number of lives are carried over from the previous game to the current game.

* The game presents a start up screen which summarizes the rules and controls. From the start up screen a player may start a new game. Other optional game play options may be presented on the start up screen such as the high score leaderboard, settings, etc.

* The player's points and lives are displayed somewhere on the screen and the display must not interfere with game play.

* The date and the score is saved to a JSON or Pickle file at the end of every game.

* A leaderboard of high scores is presented at the end of every game.

* The option to play again is given at the end of every game.

* A soundtrack and sound effects are mandatory. The sounds may be synthesized during game play or pre-recorded sounds.

* The main function must be called from the file named `invaders.py`.

