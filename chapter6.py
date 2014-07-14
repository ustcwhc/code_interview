#!/user/bin/python
# filename: chapter6.py

# All the problems are brain teasers

# PROBLEM 6.1
# Add arithmetic operators (+, -, *, /) to make the following expression true:
# 3 1 3 6 = 8
# You can use any parentheses you'd like
# Solution:
# (3 + 1) / 3 * 6 = 8


# PROBLEM 6.2
# There is an 8x8 chess board in which two diagonally opposite corners have
# been cut off. You are given 31 dominos, and a single domino can cover exactly
# two squares. can you use the 31 dominos to cover the entire board?
# Solution:
# Impossible.
# Reason:
# Split the 8x8 into 16 2x2 pieces, Fill the 2x2 pieces one by one
# Finally a 2x2 board will have a two diagonally corners will bee cut off
# It is impossible to fill the board


# PROBLEM 6.3
# A 5kg bottle A and a 3kg bottle B, how to measure 4kg water?
# Solution:
# 1. Fill 5kg in A, pull to 3kg of B=> 2kg A and 3kg B
# 2. Empty B, pull 2kg in B=> 0kg A and 2kg B
# 3. Fill A=> 5kg A and 2kg B
# 4. Use A to fill B=> 4kg A and 3kg B
# 5. Bingo


# PROBLEM 6.4
# n people and c hats, one night to remove one hat. Everyone can see others but
# cannot see themselves. How long does it take to remove the hat.
# Solution:
# Only one night, because everybody at day time can counting the overall hats
# to destimate whether he has a hat


# PROBLEM 6.5
# There are 100 floors, an egg drops from the Nth floor or above will break.
# You are given 2 eggs. Find N, while minimizing the number of droops for
# the worse case
# Solution:
# For the first egg: drop by 1, 2, 4, 8, ...
# For the second egg: when first egg not break at i, and break at 2i,
# drop from i, i+1, i+2, ..., 2i
# Find the N

