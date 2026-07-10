from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg') # Prevents GUI errors on servers
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return "Starter Kit Connected! Vibe code here."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
