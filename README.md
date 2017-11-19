<h1>Introduction</h1> 
JSON web api’s that return the latest weather info given a specific station code 

<h1>Installation</h1>
<p>install python </p>
<p>install redis </p>
<p>pip install -r requirements.txt</p>
<p>python manage.py migrate </p>

<h1>Run local server</h1> 

python manage.py runserver or ./manage runserver <br>

now open browser and hit url localhost:8000/metar/info?scode=KSGS
