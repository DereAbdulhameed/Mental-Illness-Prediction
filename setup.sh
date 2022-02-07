mkdir -p ~/.streamlit/
echo "
[general]n
email = "your-email@domain.com"n
" > ~/.streamlit/credentials.toml
echo "
[server]n
headless = truen
enableCORS=falsen
port = $PORTn
" > ~/.streamlit/config.toml
