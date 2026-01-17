<?php
$s = 25;
$t = 50;
function subtraction()
{
#   $GLOBALS['v'] = $GLOBALS['t'] - $GLOBALS['s'];
    global $s, $t;
    $GLOBALS['v'] = $t - $s;
}
subtraction();
echo $v . "\n";

$findit = array('/php/super-variables/test.php', 
    '/php/super-variables/test1123.php',
    '/php/super-variables/php-self-advanced-example1.php'
);

for ($j=0; $j<count($findit); $j++) {
    echo $findit[$j] . "\n";
    if ($_SERVER['PHP_SELF'] == $findit[$j]) {
        printf("-> Found PHP_SELF = %s (#%)\n", $findit[$j], $j);
        break;
    }
}

echo "---" . "\n";
echo $_SERVER['PHP_SELF'] . "\n";
echo "---" . "\n";

foreach ($_SERVER['argv'] as $arg) {
    echo $arg . "\n";
}

var_dump($argc);

#echo $_SERVER['GATEWAY_INTERFACE'];

$x = 4563;
var_dump($x);

$samt = 2000;

echo "My salary this month is: $$samt\n";

const INDIA = "India";
echo INDIA . "\n";
