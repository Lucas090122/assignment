from flask import Flask

app = Flask(__name__)


@app.route("/prime_number/<int:number>")
def prime_number(number):
    if number == 1:
        prime = False
    else:
        for num in range(2, int(number ** 0.5) + 1):
            if number % num == 0:
                prime = False
                break
        else:
            prime = True
    result = {'Number': number, 'isPrime': prime}
    return result


app.run()
