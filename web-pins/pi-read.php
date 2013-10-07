<?php

$pin = $_GET['pin'];

$command = "sudo python pitoast.py $pin";

$result = shell_exec($command);

echo($result);


?>