<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $message = $_POST['message'];

    $to = "mmnaseri4444@gmail.com"; // Your email address
    $subject = "New Contact Form Submission";
    $email_body = "Name: $name\nEmail: $email\nPhone: $phone\nMessage: $message";

    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";

    if (mail($to, $subject, $email_body, $headers)) {
        // Redirect back to the contact page with a success message
        header("Location: contact.php?success=true");
    } else {
        echo "Failed to send email. Please try again later.";
    }
}
?>
