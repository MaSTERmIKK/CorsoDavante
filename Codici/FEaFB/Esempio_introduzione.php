<?php
// Dichiarazione di una variabile
$eta = 22;

// Controllo se la variabile esiste ed è valorizzata
if (isset($eta)) {

    // Condizione logica
    if ($eta >= 18) {
        echo "Accesso consentito<br>";
    } else {
        echo "Accesso negato<br>";
    }

    // Array di nomi
    $nomi = ["Anna", "Luca", "Marco"];

    // Funzione personalizzata
    function stampaNomi($lista) {
        foreach ($lista as $nome) {
            echo $nome . "<br>";
        }
    }

    // Chiamata della funzione
    stampaNomi($nomi);
}
?>
