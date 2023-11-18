import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import render_template, request, jsonify
import overpy
from flask import Flask


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

def get_shops(latitude, longitude):
    api = overpy.Overpass()
    query = f"""
        (node["shop"](around:1000,{latitude},{longitude});
         node["building"="retail"](around:1000,{latitude},{longitude});
         node["building"="supermarket"](around:1000,{latitude},{longitude});
         node["healthcare"="pharmacy"](around:1000,{latitude},{longitude});
        );out;
    """
    return api.query(query)
@app.route('/get_nearby_shops', methods=["POST"])
def get_nearby_shops():
    data = request.get_json()
    latitude = data['lat']
    longitude = data['lon']
    shops = get_shops(latitude, longitude)


    shops_data = [{'lat': float(node.lat), 'lon': float(node.lon), 'name': node.tags.get('name', 'Unknown Shop')} for
                  node in shops.nodes]

    return jsonify(shops_data)

@app.route('/map')
def switch_map():
    return render_template('map.html')

def send_email(name, email, phone, message):
    sender_email = "unihack235@gmail.com"
    receiver_email = "unihack235@gmail.com"
    password = "Secretos1"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "New Contact Form Submission"

    body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.example.com', 587)  # Replace with your SMTP server
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # TO DO:
    # if request.method == 'POST':
    #     name = request.form['name']
    #     email = request.form['email']
    #     phone = request.form['phone']
    #     message = request.form['message']
    #
    #     # Send an email using the data
    #     send_email(name, email, phone, message)

    return render_template('contact.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('home3.html')

    return render_template('login.html')

        # Retrieve the user from the database
    #     user = User.query.filter_by(username=username).first()
    #
    #     # Check if user exists and password is correct
    #     if user and check_password_hash(user.password, password):
    #         # Login logic here (e.g., creating a user session)
    #         return 'Logged in successfully!'
    #     else:
    #         # Invalid credentials
    #         return 'Invalid username or password.'
    # else:
    #     # Show the login form
    #     return render_template('login.html')

@app.route("/register")
def register():
    return


if __name__ == "__main__":
    app.run(debug=True)
