# we have installed pyOpenSSL to serve our website through https instead of http
# werkzeug to work with RunServerPlus of django extension
# RunServerPlus is a part of django extension which works with our site to run it with https


####################################################################################
#----------------- python manage.py runserver_plus --cert-file cert.crt_____________#
# We have provided a file name to the runserver_plus command for the SSL/TLS certificate. Django 
# Extensions will generate a key and certificate automatically.
# Open https://mysite.com:8000/account/login/ in your browser. Now you are accessing your site 
# through HTTPS. Note we are now using https:// instead of http://.
# Your browser will show a security warning because you are using a self-generated certificate instead 
# of a certificate trusted by a Certification Authority (CA).