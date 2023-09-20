# Description
Simple rock-paper-scissors game

# Install
```
apt-get install git python
git clone https://github.com/gl1tchdev/RPSmin
cd RPSmin
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
# Run
## Development
```shell
python app.py 
```
## Production 
Use [this](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04) and ```wsgi.py``` to run app with gunicorn and nginx
# Demo
Test it: http://rps.glitchdev.space
