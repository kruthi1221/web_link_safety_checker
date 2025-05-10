from flask import Flask, render_template, request
import requests
import re
import ssl
import socket
from urllib.parse import urlparse
from datetime import datetime
import whois

app = Flask(__name__)

def check_https(link):
    return link.startswith("https://")

def check_ssl_certificate(link):
    # …your SSL‐check code here…

def check_url_structure(link):
    # …your regex check code here…

def check_redirection_chains(link):
    # …your redirect check code here…

def check_trust_seals(link):
    # …your trust‐seal check code here…

def check_ip_address(link):
    # …your IP‐check code here…

def check_url_shortening(link):
    # …your shortening‐service code here…

def check_domain_reputation(link):
    # …your WHOIS‐age check code here…

def main(link):
    features = {
        "HTTPS Encryption": check_https(link),
        "SSL Certificates": check_ssl_certificate(link),
        "URL Structure and Legitimacy": check_url_structure(link),
        "Redirection Chains": check_redirection_chains(link),
        "Trust Seals or Logos": check_trust_seals(link),
        "IP Address": check_ip_address(link),
        "URL Shortening": check_url_shortening(link),
        "Domain Reputation": check_domain_reputation(link),
    }
    return features

@app.route('/', methods=['GET', 'POST'])
def index():
    results = {}
    overall_safety = None
    link_color = None
    if request.method == 'POST' and 'link' in request.form:
        link = request.form['link']
        results = main(link)
        safe_count = sum(results.values())
        overall_safety = safe_count >= 3
        link_color = "green" if overall_safety else "red"
    return render_template('index.html',
                           results=results,
                           overall_safety=overall_safety,
                           link_color=link_color)

@app.route('/feedback', methods=['POST'])
def feedback():
    thank_you = False
    if request.method == 'POST' and 'feedback' in request.form:
        thank_you = True
    return render_template('thank_you.html', thank_you=thank_you)

if __name__ == '__main__':
    app.run(debug=True)
