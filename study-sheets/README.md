# Study Sheets Directory

This directory contains individual study sheet `.tex` files for each electronics topic.

## Naming Convention
Files follow the pattern: `sectionXX-YY-topic-name.tex`
- `XX` = Section number (01-31)
- `YY` = Topic number within section
- `topic-name` = Kebab-case topic name

## Example Files

### Completed Examples
- `section04-21-ohms-law.tex` - Fully populated example for Ohm's Law

### Template
- Use `../main.tex` as the base template for new study sheets

## How to Create a New Study Sheet

1. Copy `main.tex` to this directory with appropriate naming
2. Update the configuration section at the top:
   ```latex
   \newcommand{\topicname}{Your Topic Name}
   \newcommand{\sectionnumber}{Section XX}
   \newcommand{\sectionname}{Section Name}
   ```
3. Fill in the four main sections with content
4. Compile: `pdflatex filename.tex`

## Compilation

To compile all study sheets:
```powershell
Get-ChildItem *.tex | ForEach-Object { pdflatex $_.Name }
```

To compile a single file:
```powershell
pdflatex section04-21-ohms-law.tex
```

## Output
PDF files will be generated in this same directory.
