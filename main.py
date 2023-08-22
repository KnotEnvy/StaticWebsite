from flask import Flask, render_template, request, redirect, url_for, flash
from web_page import WebPage
from company_info import CompanyInfo
from contact_form import ContactForm
from email_service import EmailService
from flask import jsonify


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages

@app.route('/')
def index():
    web_page = WebPage()
    return render_template('index.html', content=web_page.render())

@app.route('/company-info')
def about_us():
    company_info = CompanyInfo()
    return render_template('about_us.html', company_description=company_info.description)

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Create ContactForm object and validate
    contact_form = ContactForm(name=name, email=email, subject=subject, message=message)
    if contact_form.validate():
        email_service = EmailService()
        email_service.send_email(
            subject='New Contact Form Submission',
            body=contact_form.message,
            recipient='info@aiconfidant.com'
        )
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('thank_you'))  # Redirect back to the thank you page
    else:
        flash('There was an error sending your message. Please try again.', 'error')
        return redirect(url_for('index'))  # Redirect back to the home page with an error message



@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
