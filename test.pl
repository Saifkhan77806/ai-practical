% Facts
likes(alice, pizza).
likes(bob, burger).
likes(charlie, pizza).

% Rule
friends(X, Y) :-
    likes(X, Food),
    likes(Y, Food),
    X \= Y.