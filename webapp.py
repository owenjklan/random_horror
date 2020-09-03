#!/usr/bin/env python3
import json
import sqlite3
from flask import (
    g, Flask, render_template,
)

import random_horror

DATABASE = 'random_horror_001.sq3'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


app = Flask("Random-Horror")


@app.route('/', methods=['GET'])
@app.route('/<num>')
def index(num=3):
    horrors = json.loads(random_horror.randomise(int(num), True))
    outhtml = ""
    outhtml += render_template(
        'roll_result.html',
        horrors=horrors,
    )
    return outhtml


def main():
    app.run(host="0.0.0.0", port="800")


if __name__ == '__main__':
    main()
