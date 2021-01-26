## Assignment Explanation

*Assignment was completed using Python 3.7.3* 

The following program outputs the number of ways pennies, nickels, dimes, and quarters can be combined to sum exactly $1.00. The algorithm outputs all the valid combinations, as well as the total count of combinations possible.

The application also produces the same output, but for an arbitrary set of currency names and denominations, and for an arbitrary total sum (given the user's input). 

For example, the following input arguments:

    "Coin,1.5,Arrowhead,3,Button,150"

should produce the following output:

    Coin Arrowhead Button
       0         0    150
       0         1    100
       0         2     50
       0         3      0
       1         0     50
       1         1      0

    Count: 6

## Build Procedure

`python main.py Coin,1.5,Arrowhead,3,Button,150`

The user may replace the argument with a comma delimited list of their choosing, specifying the name of each denomination, along with the number required of that denomination to reach the target sum. 

If the user chooses not to supply a comma delimited list, "Coin,1.5,Arrowhead,3,Button,150" will be used by default.