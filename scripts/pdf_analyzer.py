#!/usr/bin/env python3
"""
PDF Paper Analyzer
Downloads and extracts text from research papers from public sources.
"""

import re
import sys
import requests
from pathlib import Path
from typing import Optional, Dict, List
import json

def extract_doi_from_filename(filename: str) -> Optional[str]:
    """
    Extract DOI from ScienceDirect filename pattern.
    Example: 1-s2.0-S2666920X25000736-main.pdf -> 10.1016/j.xxxx.2025.000736
    """
    # Pattern for ScienceDirect: 1-s2.0-SXXXXXXXXXXXXXXXXX-main.pdf
    match = re.search(r'1-s2\.0-([A-Z0-9]+)-main\.pdf', filename)
    if match:
        pii = match.group(1)
        # Construct potential DOI patterns
        return f"S{pii}"
    return None

def search_arxiv(title: str) -> Optional[Dict]:
    """Search arXiv for a paper by title."""
    try:
        import urllib.parse
        query = urllib.parse.quote(title)
        url = f"http://export.arxiv.org/api/query?search_query=ti:{query}&max_results=1"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            # Parse XML response (simplified)
            if '<entry>' in response.text:
                # Extract ID
                id_match = re.search(r'<id>([^<]+)</id>', response.text)
                if id_match:
                    arxiv_url = id_match.group(1)
                    pdf_url = arxiv_url.replace('/abs/', '/pdf/') + '.pdf'
                    return {
                        'source': 'arxiv',
                        'url': arxiv_url,
                        'pdf_url': pdf_url
                    }
    except Exception as e:
        print(f"arXiv search failed: {e}", file=sys.stderr)
    return None

def resolve_doi(doi: str) -> Optional[Dict]:
    """Resolve DOI to get paper metadata and PDF link."""
    try:
        # Try DOI.org resolver
        url = f"https://doi.org/{doi}"
        response = requests.get(url, allow_redirects=True, timeout=10)
        
        if response.status_code == 200:
            return {
                'source': 'doi',
                'url': url,
                'resolved_url': response.url
            }
    except Exception as e:
        print(f"DOI resolution failed: {e}", file=sys.stderr)
    return None

def download_pdf(url: str, output_path: Path) -> bool:
    """Download PDF from URL."""
    try:
        response = requests.get(url, timeout=30, stream=True)
        if response.status_code == 200:
            output_path.write_bytes(response.content)
            return True
    except Exception as e:
        print(f"Download failed: {e}", file=sys.stderr)
    return False

def extract_pdf_text(pdf_path: Path) -> Optional[str]:
    """Extract text from PDF using pdfplumber."""
    try:
        import pdfplumber
        
        with pdfplumber.open(pdf_path) as pdf:
            text_parts = []
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    text_parts.append(text)
            
            return '\n\n'.join(text_parts)
    except ImportError:
        print("pdfplumber not installed. Install with: pip install pdfplumber", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Text extraction failed: {e}", file=sys.stderr)
        return None

def extract_metadata_from_text(text: str) -> Dict:
    """Extract basic metadata from PDF text."""
    lines = text.split('\n')[:50]  # Check first 50 lines
    
    metadata = {
        'title': None,
        'authors': [],
        'abstract': None
    }
    
    # Simple heuristic: title is usually in first few lines, often all caps or bold
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) > 20 and len(line) < 200:
            if not metadata['title'] and i < 10:
                metadata['title'] = line
                break
    
    return metadata

def main():
    """Main function for testing."""
    if len(sys.argv) < 2:
        print("Usage: python pdf_analyzer.py <pdf_filename_or_title>")
        sys.exit(1)
    
    query = sys.argv[1]
    
    # Check if it's a filename or search query
    if query.endswith('.pdf'):
        doi = extract_doi_from_filename(query)
        if doi:
            print(f"Extracted PII: {doi}")
            result = resolve_doi(f"10.1016/j.{doi}")
            if result:
                print(json.dumps(result, indent=2))
    else:
        # Search by title
        result = search_arxiv(query)
        if result:
            print(json.dumps(result, indent=2))
        else:
            print("Paper not found")

if __name__ == '__main__':
    main()
