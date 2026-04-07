# ============================================================
#  WEEK 14 LAB — Q2: HTTP SECURITY HEADER CHECKER
#  COMP2152 — Berhan Erdogan
# ============================================================

import urllib.request


# Security headers every website should have
REQUIRED_HEADERS = {
    "Content-Type":              "Defines the content format",
    "X-Frame-Options":           "Vulnerable to clickjacking",
    "X-Content-Type-Options":    "Vulnerable to MIME sniffing",
    "Strict-Transport-Security": "No HTTPS enforcement",
    "Content-Security-Policy":   "No XSS protection policy",
    "X-XSS-Protection":         "No XSS filter",
}

def check_headers(url):
    findings = []

    try:
        resp = urllib.request.urlopen(url)
        headers = dict(resp.headers)

        for rh in REQUIRED_HEADERS:
            if rh in headers:
                findings.append({"header": rh, "present": True, "value": headers[rh]})
            else:
                findings.append({"header": rh, "present": False, "value": "MISSING"})
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
         print(f"Request failed: {e}")
    return findings


# TODO: Complete generate_report(url, results)
#   Print the URL
#   missing_count = 0
#   For each result:
#     If present: print f"  ✓ {header}: {value}"
#     If missing: print f"  ✗ {header}: MISSING — {REQUIRED_HEADERS[header]}"
#       Increment missing_count
#   Print f"  Missing {missing_count} of {len(results)} security headers!"
def generate_report(url, results):
    print(url)
    missing_count = 0

    for r in results:
        if r['present']:
            print(f"  ✓ {r['header']}: {r['value']}")
        else:
            print(f"  ✗ {r['header']}: MISSING — {REQUIRED_HEADERS[r['header']]}")
            missing_count += 1
    print(f"  Missing {missing_count} of {len(results)} security headers!")


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q2: HTTP SECURITY HEADER CHECKER")
    print("=" * 60)

    urls = [
        "http://httpbin.org",
        "https://www.google.com",
    ]

    for url in urls:
        print(f"\n--- Checking {url} ---")
        results = check_headers(url)
        if results:
            generate_report(url, results)
        else:
            print("  (could not connect or not implemented)")

    print("\n" + "=" * 60)
