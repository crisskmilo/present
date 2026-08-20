"""
Sync live Google Doc source to local docs/ directory for BMAD analysis.
"""
import os
import sys
import urllib.request

DOC_ID = "1ITIkSfXrBsBcQUikDZKATdGbFsCSNM7so-M235DBM1I"
EXPORT_URL = f"https://docs.google.com/document/d/{DOC_ID}/export?format=txt"
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TARGET_PATH = os.path.join(PROJECT_ROOT, "docs", "present-mvp-proposal.md")

def sync_doc():
    print(f"Fetching latest content from Google Doc: {EXPORT_URL}...")
    try:
        req = urllib.request.Request(
            EXPORT_URL,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            content = response.read().decode("utf-8")
        
        os.makedirs(os.path.dirname(TARGET_PATH), exist_ok=True)
        
        header = (
            f"<!-- Auto-synced from Google Docs ({EXPORT_URL}) -->\n"
            f"# PRESENTE - MVP Proposal & Initiative\n"
            f"- **Source URL:** https://docs.google.com/document/d/{DOC_ID}/edit?usp=sharing\n"
            f"- **Sync Target:** `docs/present-mvp-proposal.md`\n\n---\n\n"
        )
        
        with open(TARGET_PATH, "w", encoding="utf-8") as f:
            f.write(header + content)
            
        print(f"Successfully synced Google Doc to: {TARGET_PATH}")
        return True
    except Exception as e:
        print(f"Error syncing Google Doc: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    success = sync_doc()
    sys.exit(0 if success else 1)
