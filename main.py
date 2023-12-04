#!/usr/bin/env python3
import requests
import argparse
from services.esv_api_service import ESVService

def get_bible_verse(reference, api_key):
    url = f"https://api.esv.org/v3/passage/text/?q={reference}"
    headers = {'Authorization': f'Token {api_key}'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return "Error: Unable to retrieve the verse."


def main():
    parser = argparse.ArgumentParser(description="Retrieve Bible verses from the ESV API.")
    parser.add_argument('reference', type=str, help="Bible verse reference (e.g., Romans 12:1-10)")

    args = parser.parse_args()

    esv_service = ESVService()
    verse = esv_service.get_bible_verse(args.reference)
    print(verse)

if __name__ == "__main__":
    main()
