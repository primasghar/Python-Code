# Implement a backend service that gets the ICAO code of an airport and then returns the name and location of
# the airport in JSON format. The information is fetched from the airport database used on this course.
# For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK. The response must be in
# the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.

from flask import Flask, Response
import json

from query_db_functions import fetch_airport_info_query

app = Flask(__name__)


@app.route('/airport/<text>')
def airport(text):
    try:
        icao = text.upper()
        airport_details = fetch_airport_info_query(icao)

        response = {{
            "ICAO": icao,
            "Name": airport_details[0],
            "Location": airport_details[1]
        }}

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
