🛡️ Phishing Website Detector
A web-based tool to detect phishing websites using AI-powered techniques, Google's Safe Browsing API, and heuristic checks.

🎯 Goal
This project aims to help users detect and report potential phishing websites by scanning and analyzing URLs for known threats, suspicious behavior, and phishing indicators.

🚀 Features
🔍 Scan and analyze URLs for phishing threats

🧠 Google Safe Browsing API integration

🕵️ OpenPhish & PhishTank lookup for known phishing URLs

🔬 Heuristic checks:

Suspicious keywords

IP-based URLs

Recently registered domains (WHOIS)

Presence of <iframe> or JavaScript-based forms

🌐 Domain WHOIS Info

🧬 DNS Lookup & IP Address

📑 Clean and readable threat analysis report

🌐 Domain WHOIS Info

🧬 DNS Lookup & IP Address

📑 Clean and readable threat analysis report

🧰 Tech Stack
Frontend: Streamlit (for interactive UI)

Backend: Python

Libraries & APIs:

requests – API calls

BeautifulSoup – HTML form/iframe parsing

re – Regex for IP detection

whois – Domain info

Google Safe Browsing API

OpenPhish Feed / PhishTank API



📦 Installation
1.Clone this repo
git clone https://github.com/yourusername/phishing-website-detector.git
cd phishing-website-detector

2.Install dependencies
pip install -r requirements.txt

3.Add your Google Safe Browsing API key
Create a .env file and add:
GSB_API_KEY=your_api_key
PHISHTANK_API_KEY=your_phishtank_key

4.Run the app
streamlit run app.py



⚙️ Features in Action
Feature	Description
HTTPS Check	Flags if the site doesn't use HTTPS
WHOIS Domain Age Check	Flags domains registered in the last 7 days
IP Address URLs	Flags URLs using IPs (e.g., http://192.168.0.1/index.html)
Iframe & JS Forms	Detects hidden or suspicious forms in the HTML
Threat Intelligence	Checks URL against Google Safe Browsing, OpenPhish, and PhishTank


📂 Folder Structure
phishing-website-detector/
│
├── app.py               # Main Streamlit app
├── detector.py          # URL analysis logic
├── utils/
│   ├── whois_lookup.py  # WHOIS checker
│   ├── dns_check.py     # DNS and IP utilities
│   └── threat_check.py  # API threat checks
├── requirements.txt
├── .env
└── README.md

🛡️ Disclaimer
This tool is for educational and cybersecurity awareness purposes only. It does not guarantee complete protection from phishing or malicious URLs.
