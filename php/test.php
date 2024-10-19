<?php

function test_find_string()
{
    $name="/home/test";

    $pos=strpos($name,"/home");

    if($pos === false)
    {
        echo "/home not in string $name";
    }
    else
    {
        echo "pos $pos";
    }
}

function test_find_ext()
{
    $name="test.txt";


    if(strpos($name,".") !== false)
    {
        $columns=explode(".",$name);
        array_pop($columns);
    }

    echo  implode(".",$columns);
}

test_find_ext();
