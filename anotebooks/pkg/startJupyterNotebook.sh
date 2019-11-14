
#sudo apt-get update && apt-get install -y ipython ipython-notebook
# sudo pip3 install jupyter matplotlib

(export CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt; jupyter notebook --allow-root --ip="*" --NotebookApp.token='yaml')
#jupyter notebook

