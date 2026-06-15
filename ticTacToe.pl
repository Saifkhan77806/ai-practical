% ==========================
% Tic Tac Toe in Prolog
% Human = x
% Computer = o
% ==========================

% Winning combinations

win(Board, Player) :-
    rowwin(Board, Player).

win(Board, Player) :-
    colwin(Board, Player).

win(Board, Player) :-
    diagwin(Board, Player).

% Rows

rowwin([P,P,P,_,_,_,_,_,_], P).
rowwin([_,_,_,P,P,P,_,_,_], P).
rowwin([_,_,_,_,_,_,P,P,P], P).

% Columns

colwin([P,_,_,P,_,_,P,_,_], P).
colwin([_,P,_,_,P,_,_,P,_], P).
colwin([_,_,P,_,_,P,_,_,P], P).

% Diagonals

diagwin([P,_,_,_,P,_,_,_,P], P).
diagwin([_,_,P,_,P,_,P,_,_], P).

% Alternate players

other(x,o).
other(o,x).

% Display board

display([A,B,C,D,E,F,G,H,I]) :-
    write([A,B,C]), nl,
    write([D,E,F]), nl,
    write([G,H,I]), nl, nl.

% ==========================
% Move generation
% ==========================

move([b,B,C,D,E,F,G,H,I], P, [P,B,C,D,E,F,G,H,I]).
move([A,b,C,D,E,F,G,H,I], P, [A,P,C,D,E,F,G,H,I]).
move([A,B,b,D,E,F,G,H,I], P, [A,B,P,D,E,F,G,H,I]).
move([A,B,C,b,E,F,G,H,I], P, [A,B,C,P,E,F,G,H,I]).
move([A,B,C,D,b,F,G,H,I], P, [A,B,C,D,P,F,G,H,I]).
move([A,B,C,D,E,b,G,H,I], P, [A,B,C,D,E,P,G,H,I]).
move([A,B,C,D,E,F,b,H,I], P, [A,B,C,D,E,F,P,H,I]).
move([A,B,C,D,E,F,G,b,I], P, [A,B,C,D,E,F,G,P,I]).
move([A,B,C,D,E,F,G,H,b], P, [A,B,C,D,E,F,G,H,P]).

% ==========================
% Self-play mode
% ==========================

game(Board, Player) :-
    win(Board, Player),
    !,
    write('Player '),
    write(Player),
    write(' wins!'),
    nl.

game(Board, Player) :-
    other(Player, Other),
    move(Board, Player, NewBoard),
    !,
    display(NewBoard),
    game(NewBoard, Other).

selfgame :-
    game([b,b,b,b,b,b,b,b,b], x).

% ==========================
% Human vs Computer
% ==========================

x_can_win_in_one(Board) :-
    move(Board, x, NewBoard),
    win(NewBoard, x).

orespond(Board, NewBoard) :-
    move(Board, o, NewBoard),
    win(NewBoard, o),
    !.

orespond(Board, NewBoard) :-
    move(Board, o, NewBoard),
    \+ x_can_win_in_one(NewBoard),
    !.

orespond(Board, NewBoard) :-
    move(Board, o, NewBoard),
    !.

% ==========================
% Human move
% ==========================

xmove([b,B,C,D,E,F,G,H,I],1,[x,B,C,D,E,F,G,H,I]).
xmove([A,b,C,D,E,F,G,H,I],2,[A,x,C,D,E,F,G,H,I]).
xmove([A,B,b,D,E,F,G,H,I],3,[A,B,x,D,E,F,G,H,I]).
xmove([A,B,C,b,E,F,G,H,I],4,[A,B,C,x,E,F,G,H,I]).
xmove([A,B,C,D,b,F,G,H,I],5,[A,B,C,D,x,F,G,H,I]).
xmove([A,B,C,D,E,b,G,H,I],6,[A,B,C,D,E,x,G,H,I]).
xmove([A,B,C,D,E,F,b,H,I],7,[A,B,C,D,E,F,x,H,I]).
xmove([A,B,C,D,E,F,G,b,I],8,[A,B,C,D,E,F,G,x,I]).
xmove([A,B,C,D,E,F,G,H,b],9,[A,B,C,D,E,F,G,H,x]).

xmove(Board, _, Board) :-
    write('Illegal move!'),
    nl.

% ==========================
% Instructions
% ==========================

explain :-
    write('You are X'), nl,
    write('Enter position number followed by a period.'), nl,
    display([1,2,3,4,5,6,7,8,9]).

% ==========================
% Game loop
% ==========================

playo :-
    explain,
    playfrom([b,b,b,b,b,b,b,b,b]).

playfrom(Board) :-
    win(Board, x),
    !,
    write('You win!'),
    nl.

playfrom(Board) :-
    win(Board, o),
    !,
    write('Computer wins!'),
    nl.

playfrom(Board) :-
    \+ member(b, Board),
    !,
    write('Cats game! (Draw)'),
    nl.

playfrom(Board) :-
    read(N),
    xmove(Board, N, NewBoard),
    display(NewBoard),

    ( win(NewBoard, x) ->
        playfrom(NewBoard)
    ;
        orespond(NewBoard, ComputerBoard),
        display(ComputerBoard),
        playfrom(ComputerBoard)
    ).