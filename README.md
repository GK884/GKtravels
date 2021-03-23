# GKtravels
A fully responsive website built on HTML, CSS, Bootstrap and Flask which is used to book tour plans with in India.
This website is deployed on heroku https://gktravels.herokuapp.com/


steps for use in your local system:

  fork the repo
  clone in your local pc
  make a seperate environment
  install requirements.txt (pip install -r requirements.txt)
  Run the app.py

steps for Deployment on Heroku:

  download heroku cli first from this link https://devcenter.heroku.com/articles/heroku-cli
  check heroku is installed in our system do open 'Anaconda prompt' or 'Terminal' and just type 'heroku' in there for confirmation.
  type "heroku login"
  login on heroku or do sign up
  go to your heroku dashboard and create a new app and give name
  in your conda terminal create a new environment "conda create -n python=3.6" put your environment name in place of
  go to the file location
  'git init'
  'heroku git:remote -a check on your dashboard
  'git add .'
  git commit -am "first-commit"
  'git push heroku master'
  
you will get the link on the terminal of your deployed app
