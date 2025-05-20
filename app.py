import streamlit as st
from phishing_analysis import analyze_url

st.set_page_config(page_title="Phishing URL Detector", layout="centered")

st.title("🔐 Phishing Website Detector")
st.markdown("Enter a URL to scan for phishing risks using AI-powered analysis and Google Safe Browsing API.")

url = st.text_input("🔗 Enter URL")

if st.button("🚀 Analyze"):
    if url:
        with st.spinner("Analyzing the URL..."):
            result = analyze_url(url)

        st.subheader("📊 Analysis Report")
        st.write("**Uses HTTPS:**", "✅ Yes" if result["uses_https"] else "❌ No")
        st.write("**Suspicious Keywords:**", "⚠️ Yes" if result["suspicious_keywords"] else "✅ No")
        st.write("**Subdomain Count:**", result["subdomain_count"])
        st.write("**Form Present:**", "📝 Yes" if result["form_present"] else "❌ No")
        st.write("**Google Safe Browsing Threat:**", "⚠️ Threat Detected!" if result["is_threat_by_google"] else "✅ Clean")

        st.subheader("🔍 WHOIS Info")
        st.code(result["whois_info"], language="text")

        st.subheader("🌐 DNS Info")
        st.code(result["dns_info"], language="text")

        st.success("✅ Scan Completed!")
    else:
        st.warning("Please enter a valid URL.")
