from flask import Flask, jsonify, request, make_response
import json, uuid, subprocess

app = Flask(__name__)


@app.route('/re-auth', methods=['GET'])
def re_auth():
    subprocess.check_output("pb -a", shell=True, universal_newlines=True)
    return(jsonify({"status": "done"}))


@app.route('/resource/<resource_id>/password', methods=['GET'])
def resource_password(resource_id):
    try:
        res_id_checked = uuid.UUID(resource_id)
        requested_password = subprocess.check_output("pb -p '%s'" % res_id_checked, shell=True, universal_newlines=True).strip().split("\n")[0].strip()
        return(jsonify({"resource_id": res_id_checked, "password": requested_password}))
    except ValueError as e:
        return(jsonify({"error": str(e)}))


@app.route('/resource/<resource_id>/username', methods=['GET'])
def resource_username(resource_id):
    try:
        res_id_checked = uuid.UUID(resource_id)
        requested_username = subprocess.check_output("pb -u '%s'" % res_id_checked, shell=True, universal_newlines=True).strip().split("\n")[0].strip()
        return(jsonify({"resource_id": res_id_checked, "username": requested_username}))
    except ValueError as e:
        return(jsonify({"error": str(e)}))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6581, debug=True)
