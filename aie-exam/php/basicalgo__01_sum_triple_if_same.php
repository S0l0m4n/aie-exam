<?php

function sum_triple_if_same($x, $y)
{
    if ($x == $y) {
        return 3 * $x;
    } else {
        return $x + $y;
    }
}

assert(sum_triple_if_same(3, 6) == 9);
assert(sum_triple_if_same(3, 2) == 5);
assert(sum_triple_if_same(5, 5) == 15);
