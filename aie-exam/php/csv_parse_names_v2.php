<?php
/* Fetch the CSV data and return the array of names sorted alphabetically */

define("URL", "https://coderbyte.com/api/challenges/logs/user-info-csv");

$data = file_get_contents(URL);

$entries = explode("\n", trim($data)); // trim removes whitespace

// remove column header entry
$keys = explode(",", array_shift($entries));

// create an array of arrays (dicts), each dict keying the fields of the subarray
$contacts = [];
foreach ($entries as $entry) {
    $values = explode(",", $entry);
    $contacts[] = array_combine($keys, $values);
}

usort($contacts,
    function ($a, $b) {
        return strcmp($a['Name'], $b['Name']);
    });

foreach ($contacts as $contact) {
    printf("%s / %s / %s\n", $contact['Name'], $contact['Email'], $contact['Phone']);
}
