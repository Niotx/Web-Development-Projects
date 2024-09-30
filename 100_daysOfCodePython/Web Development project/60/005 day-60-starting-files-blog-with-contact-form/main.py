from flask import Flask, render_template, request
import smtplib
import requests
import ssl
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail



posts = requests.get("https://api.npoint.io/badc9f38b1a0b76398ef").json()
OWN_EMAIL = 'parandshimi@gmail.com'
OWN_PASSWORD = 'Parand1411'
app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_content = f"""
    <h1>New Contact Form Submission</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Phone:</strong> {phone}</p>
    <p><strong>Message:</strong> {message}</p>
    """

    message = Mail(
        from_email=email,
        to_emails='parandshimi@gmail.com',
        subject='New Contact Form Submission',
        html_content=email_content
    )

    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(f"Status Code: {response.status_code}")
        print(f"Body: {response.body}")
        print(f"Headers: {response.headers}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    app.run(debug=True)