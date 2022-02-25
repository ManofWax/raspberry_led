from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from gpiozero import LED

app = Flask(__name__)
Bootstrap(app)
led_gpio = LED(2, initial_value=False)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/led", methods=['GET', 'POST'])
def led():
    led = led_gpio
    led_status = "on" if led.is_lit else "off"
    if request.method == 'POST':
        led_status = request.form['led_status']
        if led_status == "on":
            led.on()
        else:
            led.off()

    return render_template('led.html', led_status=led_status)


