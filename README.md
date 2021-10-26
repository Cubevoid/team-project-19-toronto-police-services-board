# Silicon Artists

## Description

We are building a website with a backend for the Toronto Police Services Board to allow administrators to record meeting information/minutes and display the information and agendas of these meetings to the general public. The website will help make Board meetings more accessible to the general public in Toronto interested in being engaged more with oversight of the Toronto Police Service Users: Board Administrator / Board Members. Currently the partner is using a 300-page long PDF to record this information and modifying it using Joomla CMS. This process is labour intensive and not very accessible to the public. The product will allow for all the information to be displayed clearly and for administrators to update and add to the information easily.

## Key Features

The key features the application needs to provide are the agendas and the meeting minutes. For both of these, the administrator (Diana) needs to be able to create, edit, and manage them through the admin side of the application. Agendas will have Agenda Items which may include rich text and attachments, as well as the decision that was reached during the meeting. Meeting minutes also have rich text and will include a YouTube link to the meeting recording.

On the other side of the application, a user from the general public needs to be able to access public agendas and meeting minutes through the frontend. Ideally, the user is able to access them in both HTML and PDF formats.

Full list of feature requirements from partner: 
https://docs.google.com/document/d/1OiMUVkmLtp8k1CTZHFGiqfV4dzAGzjcG/edit?usp=sharing&ouid=101500265431798349247&rtpof=true&sd=true

## Instructions

There are two different types of end users for the application: the admin (Diana) and the member of the public. Only the admins need to log into the site in order to make changes to the agendas and meeting minutes. For this, an admin user is pre-created at deployment, and then this admin can manage other users if need be.

The admin site where the agendas and meeting minutes are managed is the Django Admin Site. After the admin logs in, they can create a Meeting with various fields such as a title and date. Each meeting can have an Agenda and Meeting Minutes, which can be created under the Meeting. The Agenda will be a list of Agenda Items, possibly with one or more attachments. After the Agenda has been created, the admin can manage the Meeting Minutes. The admin decides when they want to generate a PDF of the entire meeting agenda and post it to the public website.

A member of the public can access the public-facing side of the application without logging in. On the homepage they will be able to select an upcoming or past meeting. After selecting a meeting, they are able to view the meeting agenda and the minutes in their browser, but they can also download a PDF of the Agenda if it has been posted. Also, if the admin has provided a YouTube link to the meeting recording in the minutes, then the website will show an embedded YouTube video of the meeting.

## Development requirements

*Languages: Python 3.9 (Pipenv) and Node 12 (npm).*

There are two ways to run the backend locally:

### Option 1: Manual setup

- To set up the Python backend’s dependencies, we are using Pipenv (install using `pip install pipenv` or `pip3 install pipenv`). To install the dependencies, navigate to the project directory and run `pipenv install`. Note that the dependencies are listed in the `Pipfile` and their versions in the `Pipfile.lock`.
- To activate the virtual environment, run `pipenv shell`.
- Set up the database using `python manage.py makemigrations` and `python manage.py migrate`.
- Create a new user with `python manage.py createsuperuser` which will prompt you for credentials.
- Run the development server using `python manage.py runserver`.

### Option 2: Docker

Make sure you have Docker installed on your machine.

- Build the docker image using `docker build -t backend .` (you may need `sudo` if you are on Linux)
- Run the docker image using `docker run -e "PORT=8080" -p 8080:8080 backend` (again, you may need `sudo`). You can use whichever port you’d like.

### Frontend

For the frontend, you will need `npm`.

- To install the dependencies, run `npm install`.
- You can run the frontend using `npm start`.
- To produce a minified build for deployment, use `npm run build`.

## Deployment and Github Workflow

We use a Git feature workflow with a `develop` branch. Thus, the `master` branch represents the code that has been deployed to the demo server, the `develop` branch represents ongoing work on the project, and other feature branches are created from `develop`. A pull request will start from a feature branch and is reviewed by at least one other group member before being merged into `develop`. Once the group is satisfied with the state of a project, we create a pull request and at least three members review it before it goes into `master`.

Note that on every push to every branch, we use GitHub Actions to run automated unit testing of the application.

We chose this Git workflow because our application has several different components and features which need to be worked on at the same time. This way, everyone can work on their own component and we can easily merge them together and deploy the application.

For deployment, we use automation through GitHub Actions. The backend is deployed using a workflow that builds a Docker image using the Dockerfile, uploads it to Google Container Registry, and deploys it to Google Cloud Run where it is publicly accessible. The frontend is deployed using a different workflow which creates a minified production build of the React app (using `npm run build`) and deploys it to Firebase Hosting where it is also publicly accessible. The credentials for Google Cloud and Firebase are stored in the Repository Secrets in GitHub.

For all of our GitHub Actions workflows, we made sure to implement caching of the dependencies/libraries and build artifacts so that subsequent runs of the workflows would be much faster. This way, we do not waste Actions time.

We decided to use severless platforms for deployment like Google Cloud Run and Firebase in order to simplify deployment and the eventual handoff to our partner. This way, we do not have to manage server infrastructure such as VMs, and because we are testing our code with low volume, we easily fall into the free tier of GCP.

## Licenses

We are using the MIT license for the codebase. Therefore, anyone has the ability to reuse the code, provided they include the same notice in their derivative work. Our partner is okay with any open-source license, since they are interested in sharing the code with other police departments, so we decided to use a very permissive one to keep everyone’s options open in the future.
