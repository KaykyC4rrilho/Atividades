
<?php
    function soma_valores($valor1, $valor2){

        $soma= $valor1 + $valor2;
        echo "A soma de $valor1 e $valor2 é $soma <br>";
    }

    function adicao_valores ($valor1, $valor2){

        $soma = $valor1 + $valor2;
        return $soma;
    }
    function clubes(){
        global $clubes;
        $clubes[]= "Flamengo";
        $clubes[]= "Alvaro";
        $clubes[]= "Katyky";
        return $clubes;
    }

    foreach(clubes() as $clube){
        echo $clube."<br>";

    }
    $n1= 10 ;
    $n2 = 20;
    soma_valores($n1, $n2);
    echo adicao_valores($n1, $n2);

    function formatar_nomes(){
        $prim_nome= "Kayky";
        $sobrenome= "Brito";
        global $nome;
        $nome = $sobrenome.",". $prim_nome;
    }
    echo "<br><b>Passagem de parâmetros por valor e por referência</b><br>";

    formatar_nomes();
    echo $nome."<br>";

function dobro($valor){
    $valor = 2 * $valor;
}
$valor = 5
dobro($valor);
echo$valor."<br>";
duplica($valor);
echo $valor;
?>





echo"<br><b>Valor padrão de parametro</b><br>";

function dois_valores($valor1, $valor2=10){
    echo "os valores são $valor1 e $valor2 <br>";
}

dois_valores(5, 15);
dois_valores(7);

?>