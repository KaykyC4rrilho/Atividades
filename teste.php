<?php include "operações.php";?>
<html>
    <head>
        <title> chamada de função </title>
    </head>
    <body>
        <?php
            $n1 = 2
            $n2 = 3
            $resp1 = soma_valores($n1, $n2);
            $resp2 = dobro($n);
            echo "A soma de $n1 e $n2 é $resp1.<br>";
            echo "O dobro do $n2 é $resp2.<br>";
            ?>
    </body>