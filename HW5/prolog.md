% Правило для вычисления суммы элементов пустого списка (сумма равна 0).
sum_list([], 0).

% Правило для вычисления суммы элементов непустого списка.
% Сумма равна голове списка (Head) плюс сумма хвоста списка (TailSum).
sum_list([Head | Tail], Sum) :-
    sum_list(Tail, TailSum),
    Sum is Head + TailSum.

% Пример использования:
% Подставьте свой список вместо [1, 2, 3, 4, 5].
% Пример вызова: sum_list([1, 2, 3, 4, 5], Result).
