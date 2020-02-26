## Kata Workshop

### Problem

![white-and-red-bowling-set](https://user-images.githubusercontent.com/232740/75391907-a82c6380-58f3-11ea-9479-8f44d3601761.jpg)

The game consists of 10 frames. In each frame the player has two opportunities to knock down 10 pins. The score for the frame is the total number of pins knocked down, plus bonuses for strikes and spares.

A spare is when the player knocks down all 10 pins in two tries. The bonus for that frame is the number of pins knocked down by the next roll.

A strike is when the player knocks down all 10 pins on his first try. The bonus for that frame is the value of the next two balls rolled.

In the tenth frame a player who rolls a spare or strike is allowed to roll the extra balls to complete the frame.  However no more than three balls can be rolled in the tenth frame.

### Examples

<table>
  <tr>
    <th colspan="2">1</th>
    <th colspan="2">2</th>
    <th colspan="2">3</th>
    <th colspan="2">4</th>
    <th colspan="2">5</th>
    <th colspan="2">6</th>
    <th colspan="2">7</th>
    <th colspan="2">8</th>
    <th colspan="2">9</th>
    <th colspan="2">10</th>
    <th>Score</th>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>20</td>
  </tr>
  <tr>
    <td>5</td>
    <td>5</td>
    <td>3</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>16</td>
  </tr>
  <tr>
    <td>10</td>
    <td>-</td>
    <td>3</td>
    <td>4</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>24</td>
  </tr>
  <tr>
    <td>10</td>
    <td>-</td>
    <td>10</td>
    <td>-</td>
    <td>10</td>
    <td>-</td>
    <td>10</td>
    <td>-</td>
    <td>10</td>
    <td>-</td>
    <td>10</td>
    <td>-</td>
    <td>10</td>
    <td>-</td>
    <td>10</td>
    <td>-</td>
    <td>10</td>
    <td>-</td>
    <td>10</td>
    <td>10/10</td>
    <td>300</td>
  </tr>
</table>

### Learning Outcomes

* [Three Rules of TDD](https://blog.gowtham-sai.com/three-laws-of-tdd-a84dd5204eae)
* Red/Green/Refactor TDD Cycle
* Staying Green While Refactoring
* Refactoring in Small Steps
* Basic Data Structures (Array, Set, Dictionary, Map)
