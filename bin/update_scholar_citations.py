#!/usr/bin/env python3
"""Update Google Scholar citations for publications."""

import sys
import time
from pathlib import Path

try:
    from scholarly import scholarly
    import yaml
except ImportError as e:
    print(f"Error importing required modules: {e}")
    print("Please install required packages: pip install scholarly PyYAML")
    sys.exit(1)


def load_config():
    """Load Jekyll config."""
    try:
        with open('_config.yml', 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print("Error: _config.yml not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading _config.yml: {e}")
        sys.exit(1)


def update_citations(scholar_id):
    """Fetch citation counts from Google Scholar."""
    print(f"Fetching citations for scholar ID: {scholar_id}")
    
    try:
        # Search for author
        search_query = scholarly.search_author_id(scholar_id)
        author = scholarly.fill(search_query, sections=['publications'])
        
        citations = {}
        pub_count = len(author.get('publications', []))
        print(f"Found {pub_count} publications")
        
        for i, pub in enumerate(author.get('publications', []), 1):
            try:
                time.sleep(5)  # Be nice to Google Scholar
                print(f"Processing publication {i}/{pub_count}...")
                
                filled_pub = scholarly.fill(pub)
                pub_id = filled_pub.get('author_pub_id', '')
                
                if pub_id:
                    # Extract just the publication ID part
                    pub_id_short = pub_id.split(':')[-1] if ':' in pub_id else pub_id
                    # Store with full key format: scholar_id:pub_id
                    full_key = f"{scholar_id}:{pub_id_short}"
                    citation_count = filled_pub.get('num_citations', 0)
                    citations[full_key] = citation_count
                    print(f"  {full_key}: {citation_count} citations")
                    
            except Exception as e:
                print(f"  Warning: Failed to process publication {i}: {e}")
                continue
        
        return citations
        
    except Exception as e:
        print(f"Error fetching citations: {e}")
        print("\nThis could be due to:")
        print("1. Invalid scholar_userid")
        print("2. Google Scholar rate limiting")
        print("3. Network issues")
        return {}


def main():
    print("Starting citation update process...")
    
    # Load config
    config = load_config()
    scholar_id = config.get('scholar_userid')
    
    if not scholar_id:
        print("Error: No scholar_userid found in _config.yml")
        print("Please add your Google Scholar ID to _config.yml:")
        print("  scholar_userid: YOUR_SCHOLAR_ID")
        sys.exit(1)
    
    # Fetch citations
    citations = update_citations(scholar_id)
    
    # Check if we got any data
    if not citations:
        print("\n⚠️  Warning: No citations retrieved.")
        print("⚠️  This could indicate Google Scholar is blocking requests.")
        print("⚠️  Not updating citations.yml to preserve existing data.")
        sys.exit(0)  # Exit successfully without updating
    
    # Check if all values are 0 - likely a scraping failure
    non_zero_count = sum(1 for count in citations.values() if count > 0)
    total_count = len(citations)
    
    if total_count > 0 and non_zero_count == 0:
        print(f"\n⚠️  Warning: All {total_count} citation counts are 0.")
        print("⚠️  This likely indicates Google Scholar blocked the scraping request.")
        print("⚠️  Not updating citations.yml to preserve existing data.")
        sys.exit(0)  # Exit successfully without updating
    
    # If more than 80% are zeros, something might be wrong
    if total_count > 0 and (non_zero_count / total_count) < 0.2:
        print(f"\n⚠️  Warning: Only {non_zero_count}/{total_count} citations have non-zero counts.")
        print("⚠️  This may indicate partial scraping failure.")
        print("⚠️  Not updating citations.yml to preserve existing data.")
        sys.exit(0)  # Exit successfully without updating
    
    # Ensure _data directory exists
    data_dir = Path('_data')
    data_dir.mkdir(exist_ok=True)
    
    # Write citations
    output_file = data_dir / 'citations.yml'
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            yaml.dump(citations, f, default_flow_style=False, sort_keys=True, allow_unicode=True)
        
        print(f"\n✓ Successfully wrote {len(citations)} citation counts to {output_file}")
        print(f"✓ {non_zero_count} publications have non-zero citations")
        
    except Exception as e:
        print(f"Error writing citations file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()