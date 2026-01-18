<?php

/* create n copies of the given string */
/* the standard func str_repeat does the same thing */
function create_n_copies($str, $n)
{
    $answer = "";
    while ($n > 0) {
        $answer = $answer . $str;
        $n--;
    }
    return $answer;
}

assert(create_n_copies("JS", 1) == "JS");
assert(create_n_copies("JS", 2) == "JSJS");
assert(create_n_copies("JS", 3) == "JSJSJS");
