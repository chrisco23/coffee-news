# Coffee News
AI-powered Google News clickbait killer for Arch/Sway.

**Mod+C** → 8 clickable summaries → no clickbait mornings.

## Install
\`\`\`bash
chmod +x coffee-news.py
echo 'alias coffee-news ~/coffee-news/coffee-news.py' >> ~/.config/fish/config.fish
echo 'bindsym $mod+c exec ~/coffee-news/coffee-news.py' >> ~/.config/sway/config
\`\`\`

## Features
- Google News RSS → 8 headlines
- Ollama/llama3.1 rewrites clickbait  
- Clickable summary links
- Source labels (Guardian, Reuters)
