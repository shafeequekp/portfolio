import re

file_path = 'core/templates/core/index.html'

with open(file_path, 'r') as f:
    content = f.read()

# Pattern for {{ ... }} that might be split across lines
content = re.sub(r'\{\{([^\}]+)\}\}', lambda m: '{{' + m.group(1).replace('\n', ' ').strip() + '}}', content, flags=re.DOTALL)

# Pattern for {% ... %} that might be split across lines
content = re.sub(r'\{%([^\%]+)%\}(?!\})', lambda m: '{%' + m.group(1).replace('\n', ' ').strip() + '%}', content, flags=re.DOTALL)

# Double check for the specific Hero section issue which might have nested tags or weird spacing
content = re.sub(r'Hi, I\'m <span[^>]*>\{% if profile %\}\{\{\s+profile\.name \}\}', r'Hi, I\'m <span style="color: var(--primary-color);">{% if profile %}{{ profile.name }}', content)

with open(file_path, 'w') as f:
    f.write(content)

print("Fixed split template tags in index.html.")
