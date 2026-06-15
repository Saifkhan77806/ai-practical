:- dynamic visited_state/2.


goal :-
retractall(visited_state(_, _)), state(0,0).

state(2,0) :-
write('Goal reached: (2,0)'), nl.


state(X,Y) :-X < 4,
\+ visited_state(4,Y),
assertz(visited_state(X,Y)),
write('Fill the 4-Gallon Jug: ('), write(X), write(','), write(Y),
write(') --> (4,'), write(Y), write(')'), nl, state(4,Y).

state(X,Y) :-Y < 3,
\+ visited_state(X,3),
assertz(visited_state(X,Y)),
write('Fill the 3-Gallon Jug: ('), write(X), write(','), write(Y),
write(') --> ('), write(X), write(',3)'), nl, state(X,3). 
state(X,Y) :-X > 0,
\+ visited_state(0,Y),
assertz(visited_state(X,Y)),
write('Empty the 4-Gallon jug on ground: ('), write(X), write(','), write(Y), write(') --> (0,'), write(Y), write(')'), nl,
state(0,Y).


state(X,Y) :-Y > 0,
\+ visited_state(X,0),
assertz(visited_state(X,0)),
write('Empty the 3-Gallon jug on ground: ('), write(X), write(','), write(Y), write(') --> ('), write(X), write(',0)'), nl,
state(X,0).


state(X,Y) :-X + Y >= 4, Y > 0,
NewY is Y - (4 - X),
\+ visited_state(4,NewY), assertz(visited_state(X,Y)),
write('Pour water from 3-Gallon jug to 4-Gallon until it is full: ('), write(X), write(','), write(Y),
write(') --> (4,'), write(NewY), write(')'), nl, state(4,NewY).

state(X,Y) :- 
X + Y >= 3, X > 0,
NewX is X - (3 - Y),
\+ visited_state(NewX,3), assertz(visited_state(X,Y)),
write('Pour water from 4-Gallon jug to 3-Gallon until it is full: ('), write(X), write(','), write(Y),
write(') --> ('), write(NewX), write(',3)'), nl, state(NewX,3).

state(X,Y) :-X + Y =< 4, Y > 0,
NewX is X + Y,
\+ visited_state(NewX,0), assertz(visited_state(X,Y)),
write('Pour all the water from 3-Gallon jug to 4-Gallon: ('), write(X), write(','), write(Y),
write(') --> ('), write(NewX), write(',0)'), nl, state(NewX,0).

state(X,Y) :-X + Y =< 3, X > 0,
NewY is X + Y,
\+ visited_state(0,NewY), assertz(visited_state(X,Y)),
write('Pour all the water from 4-Gallon jug to 3-Gallon: ('), 
write(X), write(','), write(Y),
write(') --> (0,'), write(NewY), write(')'), nl, state(0,NewY).
