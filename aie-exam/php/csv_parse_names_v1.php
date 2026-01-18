<?php
/* Fetch the CSV data and return the array of names sorted alphabetically */

define("URL", "https://coderbyte.com/api/challenges/logs/user-info-csv");

/*
$fp = fopen(URL, 'rb');
$data = "";
while (($chunk = fread($fp, 100)) > 0) {
    $data .= $chunk;
}
fclose($fp);
 */

$data = file_get_contents(URL);

$entries = explode("\n", $data);

// remove column header entry
[$name, $email, $phone] = explode(",", $entries[0]);

// create an array of values, (name, email, phone) in each entry
$values = array_splice($entries, 1);

// create an array of arrays (dicts), each dict keying the fields of the subarray
$contacts = [];
foreach ($values as $value) {
    [$n, $e, $p] = explode(",", $value);
    $contacts[] = [$name => $n, $email => $e, $phone => $p];
}

$names = array_column($contacts, $name);
sort($names);

$sorted = [];
foreach ($names as $n) {
    foreach ($contacts as $contact) {
        if ($contact[$name] == $n) {
            $sorted[] = $contact;
            break;
        }
    }
}

foreach ($sorted as $contact) {
    printf("%s / %s / %s\n", $contact[$name], $contact[$email], $contact[$phone]);
}
