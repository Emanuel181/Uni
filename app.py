from flask import Flask, render_template, request, jsonify
import overpy

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route("/login")
def login():
    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)