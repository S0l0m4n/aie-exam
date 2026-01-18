<?php
/* Fetch the CSV data and return the array of names sorted alphabetically */

define("URL", "https://coderbyte.com/api/challenges/logs/user-info-csv");

$fp = fopen(URL, 'rb');

// get the keys from the first line
$keys = fgetcsv($fp);

// read each other line, to get values, and add to the contacts array
$contacts = [];
while ($values = fgetcsv($fp)) {
    $contacts[] = array_combine($keys, $values);
}

fclose($fp);

usort($contacts,
    function ($a, $b) {
        return strcmp($a['Name'], $b['Name']);
    });

foreach ($contacts as $contact) {
    printf("%s / %s / %s\n", $contact['Name'], $contact['Email'], $contact['Phone']);
}
