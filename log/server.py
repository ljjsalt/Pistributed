from flask import Flask, request
from log import LOG

plog = LOG()
plog.Run("pistributed")

app = "Pistributed"
@app.route("/log", methods=['GET', 'POST'])
def reigisterHandlers():
    if request.method == 'POST':
        # validate request
        # if invalid, write header

        # write received msg
        plog.write()
