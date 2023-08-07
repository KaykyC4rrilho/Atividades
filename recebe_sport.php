<html> 


    <head> 
          
          <title> Recebe Esporte </title> 
          <meta charset= "UTF-8">

    </head>

    <body> 

         <?php

           if(isset($_POST["volei"])){
            echo "Volei<br>";
           }
           if(isset($_POST["natacao"])){
            echo "Natação<br>";
           }
           if(isset($_POST["futebol"])){
            echo "Futebol <br>";
           }
           if(isset($_POST["basquete"])){
            echo "Basquete <br>";
           }
           if(isset($_POST["handball"])){
            echo "handball <br>";
           }

 


           

         
         ?>


    </body>



</html>