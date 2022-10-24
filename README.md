# DALI-Challenge
data challenge

For the data challenge, I create a person-vs-computer game of Guess Who where characters are members contained in the data set.
The program first breaks encapsulates each element in the json file inside an instance of the Tile Class. Here, data is minorly
manipulated to better fit the game. For example, race is consolidated into one variable. 

Next, the program picks a random group of 24 individuals to serve as characters. With these characters selected, each person's
image is loaded into a graphics window. The user is able to make guesses via a text box. The text box is more finicky than I'd like.
Users must type attribute they are guessing (i.e year) and then the characters exact attribute (i.e '21), excluding upper/lower case,
for their guess to count. So an example entry may look like: "year '21" or "major computer science".

If the user guesses an attribute correctly possessed by the computer's randomly selected character, all characters without this attribute
are highlighted red (to indicate elimination). If the user guesses an attribute not possessed by the computer's randomly selected 
character, then all characters with this attribute are eliminated. These are the rules of Guess Who.

When the user is ready, they may guess the name. If correct, the computer's randomly selected character becomes highlighted green.
If wrong all tiles become highlighted red. Game over.
