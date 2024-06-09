#!/usr/bin/env python3
import argparse
from services.esv_api_service import ESVService
import pyperclip

def main():
    parser = argparse.ArgumentParser(description="Retrieve Bible verses from the ESV API.")
    parser.add_argument('-r', '--reference', type=str, help="Bible verse reference (e.g., John 11:35)", default=None)

    args = parser.parse_args()

    esv_service = ESVService()
    
    if args.reference:
        # Get the verse via the reference
        verse = esv_service.get_bible_verse(args.reference)
        print(verse)
    else:
        # Handle the case where no reference is provided
        print("No reference provided. Please provide a Bible verse reference.")
    
    copy_to_clipboard = input("Copy to clipboard? ([Y]/n): ").strip().lower()
    
    if copy_to_clipboard == '' or copy_to_clipboard in ['yes', 'y']:
        pyperclip.copy(verse)
        print("Copied!")

if __name__ == "__main__":
    main()
    
