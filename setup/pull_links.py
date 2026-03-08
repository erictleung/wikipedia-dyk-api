#!/usr/bin/env python3

"""
This script here is to help pull all the text and links from Wikipedia's "Did you know" archive.
"""

import json
import re
from pprint import pprint

import requests
from bs4 import BeautifulSoup


URL = 'https://en.wikipedia.org/wiki/Wikipedia:Recent_additions/2004/February'
OUTPUT_FILE = 'wikipedia_dyk_feb_2004.json'


def scrape_wikipedia_dyk(url, output_file=OUTPUT_FILE):
    # 1. Fetch the page
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        return

    # 2. Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', {'class': 'mw-parser-output'})

    # Regex to identify Wikipedia timestamps: e.g., "12:34, 28 February 2004 (UTC)"
    timestamp_pattern = r'\d{2}:\d{2},\s\d{1,2}\s\w+\s\d{4}'

    # Tracking items
    results = []
    current_date = None
    current_date_heading = None
    current_heading = None
    extracted_data = {}

    # 3. Iterate through elements
    # We look for h3 (Date) and ul (List of facts)
    for element in content.find_all(['div', 'ul'], recursive=False):

        print(f"Element h3/ul found: {element}")

        # Identify Headings from h3
        if element.class in ['h3']:
            headline = element.find('span', {'class': 'mw-headline'})
            print(f"Heading found: {headline}")

            if headline:
                print(f"Found non-empty headline and saving it in extracted data")
                current_heading = headline.get_text().strip()
                extracted_data[current_heading] = []

        # Identify the Bullet Points (Text)
        elif element.name == 'ul':

            # Extract bullet points as a list
            list_items = [li.get_text().strip() for li in element.find_all('li')]
            print(f"Found list items:")
            pprint(list_items)

            # Setup tracking of last time stamp
            timestamp = None
            facts = []

            # Loop through elements
            for item in list_items:
                if re.search(timestamp_pattern, item):
                    timestamp = item  # This <li> is the date-time key
            else:
                facts.append(item)

            # If no timestamp was found in the <li>, fallback to the <h3> heading
            entry_key = timestamp if timestamp else current_date_heading

            results.append({
                'batch_timestamp': entry_key,
                'parent_heading': current_date_heading,
                'hooks': facts
            })

    # Save to JSON
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    return results


# URL provided
data = scrape_wikipedia_dyk(URL)
print(f"Extracted {len(data)} batches. Example key: {data[0]['batch_timestamp']}")

