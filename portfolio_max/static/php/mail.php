<?php

// Taking all values
$name     = $_POST['name'];
$email    = $_POST['email'];
$msg      = $_POST['message']; // Corrected here
$output   = "Name: " . $name . "\n\nEmail: " . $email . "\n\nMessage: " . $msg;

$to       = 'frettchen.95@icloud.com';
$headers  = 'FROM: "' . $email . '"';

$send     = mail($to, $name, $output . "\n\n***This message has been sent from Rokstar", $headers);
?>
