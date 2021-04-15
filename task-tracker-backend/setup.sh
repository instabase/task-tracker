pyenv install 3.7.3
pyenv global 3.7.3
pip install -r requirements.txt

# deps only needed for CD deployments 
pip install jinja2==12.10 jinja2-cli==0.7.0