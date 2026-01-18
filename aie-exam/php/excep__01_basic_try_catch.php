<?php

$x = [1, 2, 3];

try {
    throw new Exception("Bad exception");
} catch (Exception $e) {
    echo "Exception occurred! " . $e->getMessage() . "\n";
}
