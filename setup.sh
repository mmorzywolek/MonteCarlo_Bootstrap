mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
enableWebsocketCompression = false\n\
\n\
" > ~/.streamlit/config.toml
