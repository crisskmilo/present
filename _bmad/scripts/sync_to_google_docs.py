"""
Google Docs Synchronization Script for PRESENTE Project.
Synchronizes local documentation (Word .docx or Markdown .md) with the live Google Doc.
"""

import os
import sys
import argparse

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
]

DEFAULT_DOC_ID = "1ITIkSfXrBsBcQUikDZKATdGbFsCSNM7so-M235DBM1I"
DEFAULT_CREDENTIALS_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "resources", "credential_google_docs.json"
)
DEFAULT_DOCX_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "docs", "present-mvp-proposal.docx"
)
DEFAULT_MD_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "docs", "present-mvp-proposal.md"
)


def sync_to_google_doc(credentials_path: str, doc_id: str, docx_path: str = None, md_path: str = None) -> None:
    """
    Synchronizes the target Google Doc using Service Account credentials.
    Prefers updating via .docx to retain rich formatting, tables, and images.
    """
    if not os.path.exists(credentials_path):
        print(f"Error: Credentials file not found at: {credentials_path}")
        print("Please ensure 'credential_google_docs.json' is placed inside the resources/ directory.")
        sys.exit(1)

    print(f"Authenticating with Service Account from: {credentials_path}")
    creds = service_account.Credentials.from_service_account_file(credentials_path, scopes=SCOPES)

    drive_service = build('drive', 'v3', credentials=creds)
    docs_service = build('docs', 'v1', credentials=creds)

    print(f"Connecting to Google Doc ID: {doc_id}")

    # Strategy 1: Upload rich .docx preserving tables, headings, and embedded diagrams
    if docx_path and os.path.exists(docx_path):
        try:
            print(f"Uploading rich Word document (.docx with diagrams): {docx_path}")
            media = MediaFileUpload(
                docx_path,
                mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                resumable=True
            )
            updated_file = drive_service.files().update(
                fileId=doc_id,
                media_body=media
            ).execute()
            print(f"Google Doc updated successfully! (File ID: {updated_file.get('id')})")
            print(f"Live Document Link: https://docs.google.com/document/d/{doc_id}/edit")
            return
        except Exception as err:
            print(f"Warning: .docx upload failed: {err}. Falling back to plain text sync...")

    # Strategy 2: Direct text batchUpdate via Google Docs API
    if md_path and os.path.exists(md_path):
        try:
            print(f"Reading Markdown content from: {md_path}")
            with open(md_path, 'r', encoding='utf-8') as file:
                content = file.read()

            doc = docs_service.documents().get(documentId=doc_id).execute()
            doc_content = doc.get('body', {}).get('content', [])
            end_index = doc_content[-1].get('endIndex', 1) - 1

            requests = []
            if end_index > 1:
                requests.append({
                    'deleteContentRange': {
                        'range': {
                            'startIndex': 1,
                            'endIndex': end_index
                        }
                    }
                })
            requests.append({
                'insertText': {
                    'location': {
                        'index': 1
                    },
                    'text': content
                }
            })

            docs_service.documents().batchUpdate(
                documentId=doc_id,
                body={'requests': requests}
            ).execute()
            print("Google Doc text synchronization completed successfully!")
            print(f"Live Document Link: https://docs.google.com/document/d/{doc_id}/edit")
        except Exception as err:
            print(f"Error updating Google Doc via API: {err}")
            sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Synchronize PRESENTE project documentation to Google Docs.")
    parser.add_argument("--credentials", default=DEFAULT_CREDENTIALS_PATH, help="Path to credential_google_docs.json")
    parser.add_argument("--doc-id", default=DEFAULT_DOC_ID, help="Google Document ID")
    parser.add_argument("--docx", default=DEFAULT_DOCX_PATH, help="Path to .docx file")
    parser.add_argument("--md", default=DEFAULT_MD_PATH, help="Path to .md file")

    args = parser.parse_args()
    sync_to_google_doc(
        credentials_path=args.credentials,
        doc_id=args.doc_id,
        docx_path=args.docx,
        md_path=args.md
    )


if __name__ == "__main__":
    main()
