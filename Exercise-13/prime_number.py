from flask import Flask, Response
import json
# Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not.
# Use the prior prime number exercise as a starting point. For example, a GET request for number 31 is given as:
# http://127.0.0.1:5000/prime_number/31. The response must be in the format of {"Number":31, "isPrime":true}.

app = Flask(__name__)

@app.route('/prime_number/<number>')

def prime_number(number):
    try:
        num = int(number)
        list_of_factors = []

        for i in range(1, num+1):
            if num % i == 0:
                list_of_factors.append(i)

        if len(list_of_factors) == 2 and list_of_factors[0] == 1 and list_of_factors[1] == num:
            response = {
                "Number":num,
                "isPrime": True,
                "status": 200
            }

            return response

    except ValueError:
        response = {
            "message": "Invalid number",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)




