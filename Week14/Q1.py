# ============================================================
#  WEEK 14 LAB — Q1: API EXPLORER
#  COMP2152 — Berhan Erdogan
# ============================================================

import urllib.request
import json


def make_request(url):
    try:
        resp = urllib.request.urlopen(url)
        body = resp.read().decode()
        status = resp.status
        headers = dict(resp.headers)
        return { "status": status, "headers": headers, "body": body}
    except urllib.error.HTTPError as e:
        return { "status": 0, "headers": {}, "body": "", "error": str(e) }

def parse_json(body):
    try:
        data = json.loads(body)
        return data
    except ValueError:
        return None

def check_api_info(response):
    findings = []
    headers = response.get("headers", {})

    if "Server" in headers:
        findings.append(f"Server version exposed: {headers['Server']}")
    if "X-Powered-By" in headers:
        findings.append(f"Technology exposed: {headers['X-Powered-By']}")
    if headers.get("Access-Control-Allow-Origin") == "*":
        findings.append(f"CORS: open to all origins")
    
    return findings




# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q1: API EXPLORER")
    print("=" * 60)

    url = "http://httpbin.org/headers"
    print(f"\n--- Requesting {url} ---")

    resp = make_request(url)

    if resp and resp.get("status"):
        print(f"  Status: {resp['status']}")

        print("\n--- Response Headers ---")
        for key, val in resp["headers"].items():
            print(f"  {key:<16}: {val}")

        print("\n--- Parsed JSON Body ---")
        data = parse_json(resp["body"])
        if data:
            for key, val in data.items():
                print(f"  {key}: {val}")
        else:
            print("  (not JSON or parse failed)")

        print("\n--- Security Findings ---")
        findings = check_api_info(resp)
        if findings:
            for f in findings:
                print(f"  {f}")
        else:
            print("  (no issues found)")
    else:
        error = resp.get("error", "unknown") if resp else "make_request returned None"
        print(f"  Error: {error}")

    print("\n" + "=" * 60)
