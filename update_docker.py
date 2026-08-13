import os

filepath = '/Users/mehedihasanmridul/website/musafly-backend/docker-compose.yml'
with open(filepath, 'r') as f:
    content = f.read()

# Add media volume to web service
if '- media_data:/app/media' not in content:
    content = content.replace(
        '    volumes:\n      - .:/app',
        '    volumes:\n      - .:/app\n      - media_data:/app/media'
    )

# Add media volume to top level volumes
if '  media_data:' not in content:
    content = content.replace(
        'volumes:\n  postgres_data:',
        'volumes:\n  postgres_data:\n  media_data:'
    )

with open(filepath, 'w') as f:
    f.write(content)

