<?php

echo "Hello World!\n";

$firstname = 'Joey';
$lastname = 'Johnson';

echo "Jacob\nJones\n";

echo "$firstname $lastname\n";

$fullname = $firstname . " " . $lastname;

echo "$fullname\n";

$animal = "bird";

if ($animal == "dog") {
    echo "Woof!\n";
} elseif ($animal == "cat") {
    echo "Meow!?\n";
} elseif ($animal == "bird") {
    echo "Chirp!\n";
} else {
    echo "I'm not a dog, cat or bird\n";
}

$set = [1,2,3,4,5];
foreach ($set as $x) {
    echo "$x";
    echo ($x < 5 ? " " : "\n");
}

$values = ["one", "two", "three"];
foreach ($values as $value) {
    if ($value == "two") {
        break;
    }
    echo "Break $value\n";
}

$cars = [
 ['make' => 'Toyota', 'model' => 'Camry'],
 ['make' => 'Honda', 'model' => 'Accord'],
];

foreach ($cars as $car) {
    echo "{$car['make']} = {$car['model']}\n";
}

echo mb_strtoupper("dog\n");

function sum($a, $b) {
    return $a + $b;
}

$S = sum(1, 2);

$sumx = function ($a, $b) {
    return $a + $b;
};

echo $sumx(1, 2) . "\n";
#echo $sumx("one", "two") . "\n";

class Bicycle
{
    public $colour;

    public function echoColour()
    {
        echo $this->colour . "\n";
    }
}

$bike = new Bicycle();
$bike->colour = "blue";
$bike->echoColour();

class Car
{
    public function drive()
    {
        echo "driving...\n";
    }
}

class Racecar extends Car
{
    public function drive()
    {
        parent::drive();
        echo "driving even faster...\n";
    }
}

$r = new Racecar();
$r->drive();

class Phone
{
    private $number;

    public function setNumber($number)
    {
        if (substr($number, 0, 1) != "7")
        {
            $this->number = $number;
        }
        else
        {
            echo "Not allowed to set a number starting with 7\n";
        }
    }

    public function showNumber()
    {
        echo $this->number . "\n";
    }
}

$phone = new Phone();
$phone->setNumber("123-456-786");
$phone->setNumber("723-456-786");
$phone->showNumber();

class Hat
{
    private $colour;

    public function __construct($colour)
    {
        $this->colour = $colour;
    }

    public function showColour()
    {
        echo $this->colour . "\n";
    }
}

$hat = new Hat("blue");
$hat->showColour();

class House
{
    private static $popularColour;
    public $colour;

    public static function setDefaultColour($colour)
    {
        self::$popularColour = $colour;
    }

    public function __construct()
    {
        $this->colour = self::$popularColour;
    }
}

$house1 = new House;
echo "house1 colour = $house1->colour\n";

House::setDefaultColour("green");
$house2 = new House;
echo "house2 colour = $house2->colour\n";

$house3 = new House;
echo "house3 colour = $house3->colour\n";

class TinyHouse
{
    private $colour;
    private $wheels;
    private $trailer;

    public static function build($colour, $wheels, $trailer)
    {
        return new self($colour, $wheels, $trailer);
    }

    public function __construct($colour, $wheels, $trailer)
    {
        $this->colour = $colour;
        $this->wheels = $wheels;
        $this->trailer = $trailer;
    }

    public function info()
    {
        echo "This tiny house is $this->colour, has $this->wheels wheels ";
        echo "and has ";
        echo $this->trailer ? "a" : "no";
        echo " trailer\n";

        echo "This tiny house is $this->colour, has $this->wheels wheels "
           . "and has " . ($this->trailer ? "a" : "no") . " trailer\n";

        printf("This tiny house is %s, has %s wheels and has %s trailer\n",
            $this->colour, $this->wheels, ($this->trailer ? "a" : "no"));
    }
}

$tinyHouse = TinyHouse::build("blue", 3, false);
$tinyHouse->info();

interface Payment
{
    public function charge($amount);
}

class CreditCard implements Payment
{
    public function charge($amount)
    {
        // implement function here
    }
}

$card = new CreditCard();
if ($card instanceof Payment) {
    $card->charge(25);
    echo "Card charged\n";
}

abstract class CellPhone
{
    abstract public function unlock();

    public function turnOn()
    {
        echo "Phone is turning on...\n";
    }
}

class iPhone extends CellPhone
{
    public function unlock()
    {
        echo "Touching fingerprint reader...\n";
    }
}

class Android extends CellPhone
{
    public function unlock()
    {
        echo "Typing passcode...\n";
    }
}

$iphone = new iPhone();
$iphone->turnOn();
$iphone->unlock();

$android = new Android();
$android->turnOn();
$android->unlock();

#$cellphone = new CellPhone(); // not allowed

class Processor
{
    public function charge($card)
    {
        if (strlen($card) != 16) {
            throw new Exception("Card number is incorrect");
        }
    }
}

class MyException extends Exception {};

$processor = new Processor();
try {
    $processor->charge("1234");
} catch (Exception $e) {
    echo $e->getMessage() . "\n";
}

try {
    throw new Exception("My exception was triggered");
} catch (MyException $e) {
    echo $e->getMessage() . "\n";
} catch (Exception $e) {
    echo "Normal exception was caught here\n";
}
