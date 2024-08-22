from flask import Flask, render_template

app = Flask(__name__)

@app.route('/marketplace', methods=['GET'])
def marketplace():
    return render_template('marketplace.html')

@app.route('/seller', methods=['GET'])
def seller():
    return render_template('seller.html')

# Run the server
if __name__ == '__main__':
    app.run(port=8000, debug=True)
