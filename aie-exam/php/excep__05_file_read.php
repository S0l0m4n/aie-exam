<?php

$filename = "foo.txt";

try {
    $fp = fopen($filename);
    $text = $fp->read();
} catch (Exception) {
    // ...
}
