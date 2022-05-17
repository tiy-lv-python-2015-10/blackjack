# Blackjack

## Quickstart
```shell
pip install -i https://test.pypi.org/simple/ flynn-blackjack

python -m blackjack
```

## Description

This assignment takes place over a Wednesday night and a weekend. Feel free to adjust if needed.

* Day 1: Plan how to create a game of blackjack.
* Weekend: Implement the game of Blackjack.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Object-oriented design.
* How to track state by using objects.

### Performance Objectives

After completing this assignment, you should be able to:

* Design a system using responsibilities and collaborators.
* Turn your design into objects.
* Build an interactive game.
* Test an object-oriented program.

## Details

### Deliverables

* A Git repo called blackjack containing at least:
  * a `README.md` file explaining your design.
  * a `lib/blackjack` directory with a file for each of your classes, with their responsibilities and collaborators described in a comment at the top of the file
  * a full suite of tests for your project

### Requirements  

* Passing unit tests
* No PEP8 or Pyflakes warnings or errors

## Day 1

Read through [the rules of blackjack](https://en.wikipedia.org/wiki/Blackjack) carefully. After reading through them, write out the steps to run the game in outline format. (See the additional resources for more on the rules of blackjack.)

After that, go through your steps and find all the actors -- that is, nouns that take actions. Create class-responsibility-collaborator (CRC) cards for each and then create empty classes for each of them with the responsibilities and collaborators at the top as a comment. Here is an example that you might find in `lib/blackjack/card.py`:

```py
class Card:
    """A playing card.

    Responsibilities:

    * Has a rank and a suit.
    * Has a point value. Aces point values depend on the Hand.

    Collaborators:

    * Collected into a Deck.
    * Collected into a Hand for each player and a Hand for the dealer.
    """  
```

Lastly, implement the `Card` and `Deck` classes.

## Weekend Lab

### Normal Mode

Take your notes and code from the previous day. Using those, create a game of Blackjack that one person plays on the command line against a
computer dealer, with the following rules:

* The game should start the player with $100 and bets are $10.
* The only valid moves are hit and stand.
* Allow the player to keep playing as long as they have money.
* The dealer uses one deck in their shoe and reshuffles after each round.

### Hard Mode

In addition to the requirements from **Normal Mode**:

* The dealer uses a shoe of six decks. With a shoe, the dealer uses something called a _cut card_. A plastic card is inserted somewhere near the bottom of the shoe. Once it is hit, the shoe is reshuffled at the end of the round. You can simulate this by reshuffling after there are 26 or less cards left in the shoe.
* The player can choose how much they want to bet before each round.
* Add doubling-down.
* Add surrender (early surrender as opposed to late surrender.)
* Add [insurance](https://en.wikipedia.org/wiki/Blackjack#Insurance).
* Add splitting hands.

## Nightmare Mode

In addition to the requirements from **Hard Mode**:

* Add the ability to choose rulesets, like:
  * No surrender/early surrender/late surrender.
  * Dealer hits soft 17 vs dealer stands of soft 17.
  * Number of decks used in the shoe.

Each choice should be able to be made separately.

## Notes

This is again an assignment with a text-based interface, which can be very hard to test. You will do best at this assignment by building all the logic for each piece and testing it well before then adding the interface on top of it.

## Additional Resources

* Other Blackjack rule summaries:
  * http://www.pagat.com/banking/blackjack.html
  * http://wizardofodds.com/games/blackjack/basics/#toc-Rules
* [Portland Pattern Repository page on CRC cards](http://c2.com/cgi/wiki?CrcCard)
* [A Brief Tour of Responsibility-Driven Design](http://www.wirfs-brock.com/PDFs/A_Brief-Tour-of-RDD.pdf)
* [Building Skills in Object-Oriented Design](http://www.itmaybeahack.com/book/oodesign-python-2.1/html/index.html)

## How to Publish
- Update the version in setup.py
- `python setup.py sdist bdist_wheel`
- `twine upload --repository testpypi dist/*`
- Enter test pypi username & password
