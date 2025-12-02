"""Update Google Scholar citations for publications."""

import scholarly
import yaml
from pathlib import Path
import time

def load_config():
    """Load Jekyll config."""
    with open('_config.yml', 'r') as f:
        return yaml.safe_load(f)

def update_citations(scholar_id):
    """Fetch citation counts from Google Scholar."""
    try:
        search_query = scholarly.search_author_id(scholar_id)
        author = scholarly.fill(search_query, sections=['publications'])
        
        citations = {}
        for pub in author['publications']:
            time.sleep(1)  # Be nice to Google Scholar
            filled_pub = scholarly.fill(pub)
            pub_id = filled_pub.get('author_pub_id', '')
            if pub_id:
                # Store with full key format: scholar_id:pub_id
                full_key = f"{scholar_id}:{pub_id.split(':')[-1]}"
                citations[full_key] = filled_pub.get('num_citations', 0)
        
        return citations
    except Exception as e:
        print(f"Error fetching citations: {e}")
        return {}

def main():
    config = load_config()
    scholar_id = config.get('scholar_userid')
    
    if not scholar_id:
        print("No scholar_userid found in _config.yml")
        return
    
    print(f"Fetching citations for scholar ID: {scholar_id}")
    citations = update_citations(scholar_id)
    
    # Ensure _data directory exists
    Path('_data').mkdir(exist_ok=True)
    
    # Write citations
    with open('_data/citations.yml', 'w') as f:
        yaml.dump(citations, f, default_flow_style=False, sort_keys=True)
    
    print(f"Updated {len(citations)} citation counts")

if __name__ == "__main__":
    main()