# ClassicSnakeGame

**main.py**
1. **Screen and Setup:**
   - It imports the necessary modules, including `Screen` from Turtle graphics, and custom modules `Snake`, `Food`, and `ScoreBoard`.
   - It sets up the game window with a black background, a title ("Slytherin"), and a screen size of 600x600 pixels.
   - The screen's update and refresh behavior is adjusted for smoother animation using `tracer(0)` to turn off automatic screen updates.

2. **Initialization:**
   - `Snake`, `Food`, and `ScoreBoard` instances are created.
   - The Snake represents the player's character, Food represents the objects the snake needs to eat, and ScoreBoard keeps track of the player's score.

3. **Keyboard Controls:**
   - The game listens for arrow key inputs (Up, Down, Left, Right) to control the snake's movement.

4. **Game Loop:**
   - The game loop (`while game_is_on`) is responsible for the game's continuous execution.
   - The screen is updated each frame, and a small time delay (`time.sleep(0.1)`) is used to control the speed of the game.
   - The `move` method of the `Snake` class is called to move the snake.
   - Collision with food is checked, and if the snake's head is close to the food, the food is refreshed, and the snake's length increases, while the player's score is incremented.

5. **Collision Detection:**
   - Collision with the game boundaries is checked. If the snake goes out of bounds, the game is reset, and the snake is placed back at the starting position.
   - There is commented-out code to check for collision with the snake's own tail (tail biting). However, this functionality is not enabled by default, as it's disabled by the comments.

6. **Game Over:**
   - If the snake collides with the boundaries or its own tail, the scoreboard is reset, and the snake is reset to its starting position.

7. **Exit Behavior:**
   - The game screen remains open until the user clicks on it, allowing them to exit the game at their discretion.


**snake.py**
1. **Initialization:**
   - The `Snake` class initializes the snake object. It creates a list of segments to represent the snake, with the head as the first segment.
   - The starting position of the snake is defined by a list of coordinates (`STARTING_POSITION`) and is created when an instance of the class is initialized.

2. **Creating the Snake:**
   - The `create_snake` method initializes the snake by creating segments for each starting position specified in `STARTING_POSITION`.

3. **Adding a Snake Segment:**
   - The `add_segment` method adds a new segment to the snake at a given position. This segment is a square-shaped Turtle object with a white color.

4. **Extending the Snake:**
   - The `extend` method adds a new segment to the snake's tail by duplicating the position of the last segment.

5. **Snake Movement:**
   - The snake's movement is controlled by methods such as `up`, `down`, `left`, and `right`. These methods set the heading of the snake's head, allowing it to move in different directions (UP, DOWN, LEFT, RIGHT).

6. **Resetting the Snake:**
   - The `home` method resets the snake's head to the starting position.

7. **Resetting Segments:**
   - The `reset_seg` method clears the existing snake segments and creates a new snake with its head in the starting position.

8. **Moving the Snake:**
   - The `move` method updates the position of each segment of the snake to follow the segment in front of it, creating a smooth slithering effect. The snake's head moves forward by a distance defined by `MOVE_DISTANCE`.

This code allows for the creation and movement of a snake in a game, with methods for controlling its direction, extending its length, and resetting the game state as needed.


**food.py**
1. **Initialization:**
   - The `Food` class is a subclass of the `Turtle` class, used to create the game's food item.
   - It initializes the appearance and attributes of the food, including its shape, color, and size.
   - The food is initially placed off-screen by calling the `refresh` method.

2. **Refreshing Food Position:**
   - The `refresh` method is responsible for randomly repositioning the food item within the game's playing field.
   - It generates random x and y coordinates within a specific range (-280 to 280), ensuring the food appears within the visible game area.
   - The `goto` method is used to move the food to its new position.

This code creates a food item represented as a small circle in the game, and the `refresh` method allows for the random placement of food to keep the game challenging. The food's appearance and initial positioning can be customized to fit the style and requirements of the game.


**scoreboard.py**
1. **Initialization:**
   - The `ScoreBoard` class is a subclass of the `Turtle` class (from the Turtle graphics library) used for displaying and managing the game's score.
   - It sets the initial attributes, such as color, position, and font, and hides the turtle cursor.

2. **High Score Tracking:**
   - It reads the high score from a text file ("prevScore.txt") and initializes the current score to zero.

3. **Display Score:**
   - It displays the current score and high score at the top of the game screen.
   - The `write` method is used to display the scores with a specified font and alignment.

4. **Updating the Score:**
   - The `update` method clears the previous score display and updates it with the new scores.

5. **Resetting Score:**
   - The `reset` method is called when the game is over or needs to be reset.
   - If the current score surpasses the previous high score, it updates the high score and writes it to the "prevScore.txt" file.
   - The current score is then reset to zero, and the display is updated.

6. **Increasing Score:**
   - The `increase_score` method increments the current score by 1 and updates the score display.

