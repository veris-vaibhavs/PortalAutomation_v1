wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f
wget https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip && sudo mv chromedriver /usr/bin/chromedriver && sudo chown root:root /usr/bin/chromedriver && sudo chmod +x /usr/bin/chromedriver
pwd

#  mv chromedriver /usr/bin/chromedriver

