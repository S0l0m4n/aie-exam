<?php

$headers = getallheaders();
echo "Your User-Agent is: " . $headers['User-Agent'] . "</br>";
echo "Your User-Agent is: " . $_SERVER['HTTP_USER_AGENT'] . "</br>";
