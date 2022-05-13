#!/opt/homebrew/bin/python3
# encoding: utf-8

from flask import Flask, jsonify, request

from google.cloud import storage

import constants
import helpers

app = Flask(__name__)

@app.route('/upload', methods=['POST', 'PUT'])
def upload():
    if (request.headers.get('Content-Type') != 'application/json'):
        # HTTP 415: unsupported media type
        abort(415, 'Content type not supported')

    req_body = request.get_json()

    gcs_client = storage.Client(project=constants.PROJECT_ID)
    bucket = helpers.get_create_bucket(constants.BUCKET_NAME, gcs_client)

    blob = bucket.blob(req_body['name'])
    blob.upload_from_string(req_body['contents'])

    blob.upload_from_filename(source_file_name)
    return jsonify({'message': 'upload successful.'})

@app.route('/files/<file_id>', methods=['GET'])
def getById(file_id):
    return jsonify({'message': f'getByIdsuccessful for file {file_id}'})

@app.route('/files', methods=['GET'])
def getAll():
    return jsonify({'messsage': "getAll successful."})

@app.route('/download', methods=['GET'])
def download():
    return jsonify({'message': 'download successful.'})

app.run(debug=True)