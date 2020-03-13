import os
import re
import sys
import pathlib
from typing import List

def count_words_in_markdown(markdown: str):
    text: str = markdown

    # Comments
    text = re.sub(r'<!--(.*?)-->', '', text, flags=re.MULTILINE)
    # Tabs to spaces
    text = text.replace('\t', '    ')
    # More than 1 space to 4 spaces
    text = re.sub(r'[ ]{2,}', '    ', text)
    # Footnotes
    text = re.sub(r'^\[[^]]*\][^(].*', '', text, flags=re.MULTILINE)
    # Indented blocks of code
    text = re.sub(r'^( {4,}[^-*]).*', '', text, flags=re.MULTILINE)
    # Replace newlines with spaces for uniform handling
    text = text.replace('\n', ' ')
    # Custom header IDs
    text = re.sub(r'{#.*}', '', text)
    # Remove images
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', text)
    # Remove HTML tags
    text = re.sub(r'</?[^>]*>', '', text)
    # Remove special characters
    text = re.sub(r'[#*`~\-–^=<>+|/:]', '', text)
    # Remove footnote references
    text = re.sub(r'\[[0-9]*\]', '', text)
    # Remove enumerations
    text = re.sub(r'[0-9#]*\.', '', text)

    return len(text.split())


topFolder: pathlib.Path = pathlib.Path('C:\\Users\\jackm\\Documents\\GitHub\\jackmckew.dev\\content\\')

allMarkdown: List  = []

for singleFile in topFolder.glob('**/*'):
     if singleFile.suffix == '.md':
         # Append path        
         allMarkdown.append(singleFile)

totalNumberOfWords: int = 0
for singlePost in allMarkdown:
    with open(singlePost, 'r', encoding='utf8') as f:
            totalNumberOfWords += count_words_in_markdown(f.read())        

print(totalNumberOfWords)