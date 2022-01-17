# SchoolVerse Scraping Server

A server operated through a REST API that has a function to scrape user informations from various platforms, and then writes the information to SchoolVerse firebase. The credentials are decrypted, then passed through a scraper function that uses bs4 and python requests to pull information and output as JSON, which is then exported via Firebase Admin SDK. 

This server only contains a REST API (accepting POST requests), and no website, so interaction will only make work with either an HTTP service, code, or cURL. 

## General Information

#### Current Average Execution Time:
2-3 Seconds 

#### Currently Supported Platforms
- Schoology

#### Platforms In Development
- Veracross

#### Future Platforms
- Showbie
- Google Classroom

## How To Run
1. Ensure you are running the latest version of python
2. Enter the directory for the project either by using 'cd' or by using your prefered programming software
3. Open and enter a virtual environment, install dependencies with either
#### METHOD 1
~~~
pip install virtualenv
~~~
~~~
vitualenv env
~~~
~~~
/env/bin/activate
~~~
~~~
pip install -r requirements.txt
~~~
#### METHOD 2
~~~
cd scripts/dev
~~~
~~~
sh firstrun.sh
~~~
~~~
cd ..
~~~
~~~
cd ..
~~~
#### METHOD 3
or if you already have some packages installed, then make sure you
have the latest versions by running a custom script:
~~~
cd scripts/dev
~~~
~~~
sh dependencies.sh
~~~
~~~
cd ..
cd ..
~~~
and it should uninstall and reinstall all pip packages ONLY if you are running a virtual env. 

4. Gather and correctly place various secrets
- firebase secrets
- .env

5. During release, the next step would be to run the server. For now, run testing:

#### Test The Scraper:
In testing simply open run 'scraper.py' and
enter a valid Schoology username and password. 

#### Test Full Stack
Obtain secrets file and place in firebase_manager directory. Then simply run "full_stack.py" and enter a valid Schoology username and password. Don't
forget to click enter a few times as there are 'input()' statements to help
make the code easier to test

#### Unit-Testing
Simply run the command 
~~~
pytest
~~~
to execute all unit-tests found in the tests directory not including the 
folder 'non-unit'. It can test anything that does not require secrets. 

<hr>
This is open source to encourage improvements, suggestions and security. 
<hr>


