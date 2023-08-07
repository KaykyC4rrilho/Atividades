<?php
function Impar_ou_Par($vetor){
    foreach($vetor as $v){
        if ($v % 2 == 0 )
        echo "$v é par. <br>";
    
    else
        echo "$v é ímpar. <br>";
    }
}



/*foreach($vetor as $v){
    if ($v % 2 == 0 )
        echo "$v é par. <br>";
    
    else
        echo "$v é ímpar. <br>";

}
if ($vetor % 2 == 0)
    echo "$vetor é par";
else
    echo "$vetor é ímpar";*/


?>




