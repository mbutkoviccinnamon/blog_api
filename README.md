Code related to blog post What do data engineers do? Create APIs on https://cinnamon.agency/blog/post/what_do_data_engineers_do
Installing requirements

virtualenv --python=/usr/local/bin/python3.9 env
source env/bin/activate

Flask is a lightweight web application framework, which can be used to develop various modules of an application, but for simplicity we will use it to manage HTTP requests only. We will use pip to install it:

pip install flask 

We can run the application with:

python3.9 api.py 
You should see a message like this:

* Serving Flask app 'api' (lazy loading)
* Environment:production
WARNING:This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode:on
* Running on http://127.0.0.1:5000/(Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN:591-543-544
Great! Now we can test our application directly in the browser. Open your browser and type in the URL http://127.0.0.1:5000/and press Enter.
