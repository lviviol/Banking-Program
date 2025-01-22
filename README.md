# Banking Project (Python)

Create Python Banking Program  
Credits Bro Code https://www.youtube.com/watch?v=JlMyYuY1aXU  

Purpose  
Purpose of this project is to practise Python aided by a video tutorial.  

Problem  
During the practise, a few limitations was observed:  
1. Unlimited amount of invalid inputs is allowed for "Deposits & Withdrawal"
2. Program runs into error when string is being input.
3. Output information is clustered with input options, making hard to read.

Enhancements (Version 1)
1. To solve the problem of invalid inputs, "try-except" coding block is used to reject invalid input with.
2. A simple statement is added to guide user to provide correct input.
3. To prevent unlimited amount of invalid inputs (hogging), a "Lock Account" action is triggered after 3 invalid inputs each for Deposits & Withdrawal.


Enhancements (Version 2)
1. to prevent continuous hogging, the program is upgraded with a countdown timer after account is locked.
3. After countdown completes, program returns to Banking screen

