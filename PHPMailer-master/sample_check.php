<?php
require 'class.phpmailer.php';

$mail = new PHPMailer;

$mail->isSMTP();                                      // Set mailer to use SMTP
$mail->Host = 'smtp.sendgrid.net';  // Specify main and backup server
$mail->SMTPAuth = true;                               // Enable SMTP authentication
$mail->Username = 'syncNscan';                            // SMTP username
$mail->Password = 'pass@word2';  
$mail->Port=587;                         // SMTP password
$mail->SMTPSecure = 'tls';                            // Enable encryption, 'ssl' also accepted

$mail->From = 'sbpraveen34@iitj.ac.in';
$mail->FromName = 'Mailer';
$mail->addAddress('sbpraveen34@iitj.ac.in');  // Add a recipient

$mail->WordWrap = 50;                                 // Set word wrap to 50 characters
    // Optional name
$mail->isHTML(true);                                  // Set email format to HTML

$mail->Subject = 'Here is the subject';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';
$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

if(!$mail->send()) {
   echo 'Message could not be sent.';
   echo 'Mailer Error: ' . $mail->ErrorInfo;
   exit;
}

echo 'Message has been sent';
?>
