import os
import re
from pathlib import Path

def extract_frontmatter(file_path):
    """Extract frontmatter from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Match frontmatter between --- delimiters
        match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if match:
            return match.group(1)
        return None

def replace_frontmatter(file_path, new_frontmatter):
    """Replace frontmatter in a markdown file with new frontmatter."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace existing frontmatter or add new if none exists
    if re.match(r'^---\n.*?\n---\n', content, re.DOTALL):
        new_content = re.sub(r'^---\n.*?\n---\n', f'---\n{new_frontmatter}\n---\n', content, count=1, flags=re.DOTALL)
    else:
        new_content = f'---\n{new_frontmatter}\n---\n{content}'
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    dir1 = Path('Directory1')
    dir2 = Path('Directory2')
    
    # Ensure directories exist
    if not dir1.exists() or not dir2.exists():
        print("One or both directories do not exist.")
        return
    
    # Get all markdown files from Directory1
    for file1 in dir1.glob('*.md'):
        file2 = dir2 / file1.name
        
        # Check if corresponding file exists in Directory2
        if file2.exists():
            # Extract frontmatter from Directory1 file
            frontmatter = extract_frontmatter(file1)
            if frontmatter:
                # Replace frontmatter in Directory2 file
                replace_frontmatter(file2, frontmatter)
                print(f"Updated frontmatter for {file2.name}")
            else:
                print(f"No frontmatter found in {file1.name}")
        else:
            print(f"No matching file found for {file1.name} in Directory2")

if __name__ == '__main__':
    main()
