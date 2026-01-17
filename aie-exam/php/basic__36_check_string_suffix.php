<?php

define("USAGE_STR", "Usage: " . $argv[0] . " <str1> <str2>");

if ($argc != 3) {
    echo USAGE_STR . "\n";
    exit(1);
}

$str1 = $argv[1];
$str2 = $argv[2];

$l1 = strlen($str1);
$l2 = strlen($str2);
if ($l2 > $l1) {
    echo "First string should be longer than the second\n";
    echo USAGE_STR . "\n";
    exit(1);
}

$result = ($str2 == substr($str1, -$l2));
# str_ends_with(str1, str2) is a valid func

printf("'%s' %s as the suffix of '%s'\n",
    $str2, $result ? "appears" : "does NOT appear", $str1);
