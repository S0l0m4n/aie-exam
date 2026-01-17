<?php

$filename = $argv[1];

$fp = fopen($filename, 'r');

$count = 0;
while (fgets($fp) != false) {
    $count++;
}

fclose($fp);

printf("%s contains %s lines\n", $filename, $count);

$lines = file($filename);

echo "---\n";

foreach ($lines as $line) {
    echo $line;
}

echo "---\n";

printf("%s contains %s lines\n", $filename, count($lines));
