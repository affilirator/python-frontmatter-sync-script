# Explanation of the Frontmatter Replacement Script

The Python script automates the process of replacing the frontmatter in Markdown files located in `Directory2` with the corresponding frontmatter from files in `Directory1`, assuming the files share the same names (e.g., `post-about-me.md`). Below is a step-by-step explanation of how the script works.

## 1. Imports and Setup

- **Libraries Used**:
  - `os`: For interacting with the operating system (though not directly used here, included for potential extensions).
  - `re`: For regular expression operations to parse and manipulate frontmatter.
  - `pathlib.Path`: For handling file paths in a cross-platform way.
- The script defines three main functions: `extract_frontmatter`, `replace_frontmatter`, and `main`.

## 2. `extract_frontmatter` Function

- **Purpose**: Reads a Markdown file and extracts its frontmatter (the metadata block between `---` delimiters at the start of the file).
- **How It Works**:
  - Opens the file in read mode with UTF-8 encoding.
  - Reads the entire file content.
  - Uses a regular expression (`re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)`) to match the frontmatter:
    - `^---\n`: Matches the opening `---` followed by a newline.
    - `(.*?)`: Captures the frontmatter content (non-greedy match to stop at the closing delimiter).
    - `\n---\n`: Matches the closing `---` followed by a newline.
  - Returns the captured frontmatter or `None` if no frontmatter is found.

## 3. `replace_frontmatter` Function

- **Purpose**: Replaces the frontmatter in a Markdown file with new frontmatter provided as input.
- **How It Works**:
  - Opens the file in read mode and reads its content.
  - Checks if the file has existing frontmatter using a regular expression.
  - If frontmatter exists:
    - Uses `re.sub` to replace the existing frontmatter with the new one, preserving the rest of the file content.
    - The new frontmatter is formatted as `---\n{new_frontmatter}\n---\n`.
  - If no frontmatter exists:
    - Prepends the new frontmatter to the file content.
  - Writes the modified content back to the file.

## 4. `main` Function

- **Purpose**: Orchestrates the process of matching files between directories and applying frontmatter replacements.
- **How It Works**:
  - Defines paths for `Directory1` and `Directory2` using `Path`.
  - Checks if both directories exist; if not, prints an error and exits.
  - Iterates over all `.md` files in `Directory1` using `dir1.glob('*.md')`.
  - For each file in `Directory1`:
    - Constructs the corresponding file path in `Directory2` using the same filename.
    - Checks if the file exists in `Directory2`.
    - If it exists:
      - Calls `extract_frontmatter` to get the frontmatter from the `Directory1` file.
      - If frontmatter is found, calls `replace_frontmatter` to update the `Directory2` file.
      - Prints a success message (e.g., "Updated frontmatter for post-about-me.md").
    - If no corresponding file exists in `Directory2`, prints a message.
    - If no frontmatter is found in the `Directory1` file, prints a message.

## 5. Execution

- The script runs the `main` function when executed directly (`if __name__ == '__main__':`).
- It processes all Markdown files systematically, ensuring that only matching files are updated and providing feedback for each file.

## Key Features

- **Robust File Matching**: Uses `pathlib.Path` for reliable cross-platform path handling and matches files by name.
- **Regular Expressions**: Accurately identifies and manipulates frontmatter, handling cases with or without existing frontmatter.
- **Error Handling**: Checks for directory existence, file existence, and valid frontmatter, with clear feedback.
- **Non-Destructive**: Only modifies the frontmatter, preserving the rest of the file content.

## Example Scenario

- **Directory1**:
  - `post-about-me.md`:
    ```markdown
    ---
    title: About Me
    date: 2023-01-01
    ---
    Content here...
    ```
- **Directory2**:
  - `post-about-me.md`:
    ```markdown
    ---
    title: Old Title
    author: Someone
    ---
    Other content...
    ```
- **Script Execution**:
  - Reads frontmatter from `Directory1/post-about-me.md`.
  - Replaces frontmatter in `Directory2/post-about-me.md`.
  - Resulting `Directory2/post-about-me.md`:
    ```markdown
    ---
    title: About Me
    date: 2023-01-01
    ---
    Other content...
    ```

This script is efficient, handles edge cases, and provides clear feedback, making it suitable for batch-processing Markdown files with frontmatter.
