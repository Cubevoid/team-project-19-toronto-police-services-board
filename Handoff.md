# Handoff Instructions

## Local Development

See [README.md](README.md) for setup instructions on your local machine.

## Manual Deployment

### Introduction

We use Docker to build and package the project. This means that it should be able to run on any server running almost any operating system. Thus, you can deploy it on your own server, using a Virtual Machine in a public cloud service like AWS or Google Cloud, or using a fully-managed cloud service for Docker containers, such as Google Cloud Run.

You can use either build and deploy the Docker image manually or a CI/CD service like GitHub Actions to build and deploy the Docker image.

### Building the Project

#### Backend

To build the Docker image, first make sure you have [Docker](https://docs.docker.com/engine/install/) and Git installed on the server you are deploying to.

Next, clone this Git repository and build the Docker image using

```[sh]
docker build -t backend --build-arg FRONTEND_URL={frontend URL} --build-arg BACKEND_URL={backend URL}.
```

Make sure to replace `{frontend URL}` and `{backend URL}` with the correct values for deployment.

You can also add `--build-arg SUPERUSER_EMAIL={email}` and `--build-arg DJANGO_SUPERUSER_PASSWORD={password}` to change the initial admin credentials. (By default they are `admin@example.com` and `admin`)

(Note: you may need to use `sudo` in front of `docker` commands on some Linux systems.)

The build process will take a couple of minutes, but after it is done you can verify by running `docker images`.

#### Frontend

Now we build the frontend. We are not using a Docker image for this since it would be cost-ineffective, as the frontend files are static JavaScript. We used Firebase Hosting to host the frontend, but there are some other services out there such as CDNs.

Make sure you have `npm` installed on your local machine.

Run `npm install` to install the dependencies of the project and then run `npm run build` to build a production version.

Now we can deploy these files to our hosting provider.

For Firebase, follow [these instructions](https://firebase.google.com/docs/hosting/quickstart) to set up Firebase and deploy your project.

You will probably need to remove the current `.firebaserc` and `firebase.json` files so that the Firebase CLI does not get confused.

### Running the Project

Now, just like for local development, you can run the backend on the server using:

```[sh]
docker run -e "PORT=8080" -p 8080:8080 backend
```

you can run on a different port by simply replacing the number 8080 above with the port number you'd like to use.

If you deployed to a service like Firebase in the previous step, then the frontend should already be running.

## Automated Deployment

We used GitHub Actions for our CI/CD, but there are other tools such as Travis or CircleCI that will work similarly.

The GitHub Actions scripts are set up in the `.github/workflows/` directory, and you should reference them throughout this guide.