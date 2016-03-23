<?php
    try {
        $dbh = new PDO('mysql:host=localhost;dbname=demo', 'demo','demo');
        foreach($dbh->query('SELECT * from demo') as $row) {
            print_r($row);
        }
        $dbh = null;
    } catch (PDOException $e) {
        print "Error!: " . $e->getMessage() . "<br/>";
        die();
    }
?>