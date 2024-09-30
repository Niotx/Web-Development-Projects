<!-- Contact Form (contact.php) -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <?php
    if (isset($_GET['success']) && $_GET['success'] == 'true') {
        echo "<p>Email sent successfully!</p>";
    }
    ?>
    <form action="send_email.php" method="POST">
        <input type="text" name="name" placeholder="Your Name" required><br>
        <input type="email" name="email" placeholder="Your Email" required><br>
        <input type="text" name="phone" placeholder="Your Phone" required><br>
        <textarea name="message" placeholder="Your Message" required></textarea><br>
        <input type="submit" value="Send">
    </form>
</body>
</html>
