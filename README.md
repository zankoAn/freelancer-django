# freelancer-django
The freelancer website is written by Django to help freelancers and employers to find and create new jobs/projects.
<br><br>

## DB SCHEME
  > You can see the database scheme of this website by clicking on this link :point_right:
      [SCHEME](https://drawsql.app/zanko-1/diagrams/freelancer)

## Features
  - Add a new job/project with so amazing capability.
  - Users can send offers to the projects and can see each other suggestions.
  - Each user can have a special cv and etc.. and also employers can search by user skill, Experience or etc...
  - Pricing boards for employers who want their projects to be seen more and done faster.
  - etc

<br>

## #Quick Setup 
  Fir of all you need to install the `PostgreSQL`  package in your system and activate the `Postgres service`.<br>

  The second step is to install library dependence whit exists in the `reqruements.txt` you can install it by this command below:
  ```
  pip install -r requrements.txt
  ```
  
  Then We need to export all environment variables to initialize project configurations.
  <details>
     <summary>Config</summary>
     <p>You can change or set DB, email, Django or etc.. configurations in /freelancer-django
/config/.env file.<br><br></p>
  </details>
  
  ```
  export $(grep -v '^#>' ./config/.env | xargs);
  ```
  After all, you can run the project by 3 commands below:
  ```
  python manage.py makemigrations 
  python manage.py migrate
  python manage.py runserver
  ```
  ### **Of course, these setups will be changed later...**
  <br>
  
## TODO 
 - [x] Create job models, views and urls. 
 - [x] Create apply models, views and urls. 
 - [x] Create job categorys.
 - [x] Create job tags.
 - [ ] Create payment models, views and urls. 
 - [ ] Add about, pricing-pannel, FAQ sections.
 - [ ] Dockerize project.
 - [ ] Handel WebServer base configurations.
 - [ ] Handel WebServer security configurations.
 - [ ] Handel WebServer other configurations. 
 - [ ] Create Rest-Api by DRF.
 - [ ] Make TestCase for job models, views and urls.
 - [ ] Make TestCase for apply models, views and urls.
 - [ ] Make TestCase for account models, views and urls.
 - [ ] Make TestCase for Rest-Api.
 - [ ] Make Api documentation
 
