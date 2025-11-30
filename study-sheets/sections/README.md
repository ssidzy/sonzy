# Sections Directory

This directory contains modular content files for each section that can be included in `main.tex`.

## Structure

Each section has its own content file:
- `section01-content.tex` - Section 01: Welcome to Electronics I
- `section02-content.tex` - Section 02: Understanding Electricity (to be created)
- `section03-content.tex` - Section 03: Simulator Tutorial (to be created)
- ... and so on for all 31 sections

## How It Works

The main.tex file uses `\input{study-sheets/sections/sectionXX-content.tex}` to include the content.

### Benefits of Modular Approach:
1. **Easy to manage** - Each section is a separate file
2. **Reusable** - Content can be included in multiple documents
3. **Collaborative** - Different people can work on different sections
4. **Clean organization** - Main document stays clean, content is separated

## Usage in main.tex

```latex
% In main.tex, update configuration:
\newcommand{\topicname}{Your Topic Name}
\newcommand{\sectionnumber}{Section XX}
\newcommand{\sectionname}{Section Name}

% Then include the content file:
\input{study-sheets/sections/section01-content.tex}
```

## Content File Format

Each content file should contain only the four main sections:
1. TL;DR (The Gist)
2. Detailed Explanation
3. Practical Example & Numerical
4. Key Points (Interview Focus)

**No preamble, no document structure** - just the content to be included.
