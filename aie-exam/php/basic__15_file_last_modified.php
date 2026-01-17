<?php

$filename = basename($_SERVER['PHP_SELF']);

printf("%s was last modified %s\n",
    $filename,
    date("F d Y H:i:s", filemtime($filename)));
