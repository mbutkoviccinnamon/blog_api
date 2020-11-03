from flask import Flask, request, jsonify
import csv

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def hello():
    return f"Hello, world!"


@app.route('/owid-covid-data_simplified', methods=['GET'])
def read_records():
    query_parameters = request.args
    input_country = query_parameters.get('country')
    input_date = query_parameters.get('date')
    result_records = []
    with open('owid-covid-data_simplified.csv') as csv_file:
        sreader = csv.reader(csv_file, delimiter=',')
        for row in sreader:
            if (row[0] == input_country or input_country is None) and (row[1] == input_date or input_date is None):
                result_records.append({"location": row[0], "date": row[1], "new_cases": row[2]})
    return jsonify(result_records)


@app.route('/owid-covid-data_simplified', methods=['PUT'])
def write_into_csv():
    input_country = request.json.get('country')
    input_date = request.json.get('date')
    input_new_cases = request.json.get('new_cases')

    with open('owid-covid-data_simplified.csv') as inf:
        reader = csv.reader(inf.readlines())

        with open('owid-covid-data_simplified.csv', 'w') as outf:
            found_record = False
            writer = csv.writer(outf)
            for line in reader:
                if line[0] == input_country and line[1] == input_date:
                    writer.writerow([line[0], line[1], input_new_cases])
                    found_record = True
                    break
                else:
                    writer.writerow(line)
            if not found_record:
                writer.writerow([input_country, input_date, input_new_cases])
            writer.writerows(reader)

    return jsonify(request.json)


@app.route('/owid-covid-data_simplified', methods=['DELETE'])
def delete_from_csv():
    query_parameters = request.args
    input_country = query_parameters.get('country')
    input_date = query_parameters.get('date')
    deleted_flag = False

    with open('owid-covid-data_simplified.csv') as inf:
        reader = csv.reader(inf.readlines())

        with open('owid-covid-data_simplified.csv', 'w') as outf:
            writer = csv.writer(outf)
            for line in reader:
                if line[0] == input_country and line[1] == input_date:
                    deleted_flag = True
                    break
                else:
                    writer.writerow(line)
            writer.writerows(reader)

    return jsonify({"deleted": deleted_flag})


app.run()
