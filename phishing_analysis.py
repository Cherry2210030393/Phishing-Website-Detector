import re
import socket
import requests
import whois
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

def check_https(url):
    return url.startswith("https")

def contains_suspicious_keywords(url):
    keywords = ['login', 'verify', 'update', 'bank', 'free', 'gift', 'confirm']
    return any(kw in url.lower() for kw in keywords)

def count_subdomains(url):
    return url.count('.') - 1

def check_forms(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        return len(soup.find_all('form')) > 0
    except:
        return False

def google_safe_browsing_check(url):
    api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"
    body = {
        "client": {"clientId": "phishing-detector", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    try:
        response = requests.post(api_url, json=body)
        matches = response.json().get("matches", [])
        return len(matches) > 0
    except Exception as e:
        return False

def get_whois_info(url):
    try:
        domain = re.findall(r"https?://([^/]+)", url)[0]
        return whois.whois(domain)
    except:
        return "WHOIS data not found"

def get_dns_info(url):
    try:
        domain = re.findall(r"https?://([^/]+)", url)[0]
        return socket.gethostbyname(domain)
    except:
        return "DNS resolution failed"

def analyze_url(url):
    return {
        "uses_https": check_https(url),
        "suspicious_keywords": contains_suspicious_keywords(url),
        "subdomain_count": count_subdomains(url),
        "form_present": check_forms(url),
        "is_threat_by_google": google_safe_browsing_check(url),
        "whois_info": str(get_whois_info(url)),
        "dns_info": get_dns_info(url),
    }
