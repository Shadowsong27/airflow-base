# Base Airflow DAGs

This is an Airflow 2 template repo. It contains an out of box Airflow 2 instance for
1. using a decoupled remote Git repo as the DAG folder
2. automatically synced at a given interval using a cron script
3. containerized and ready to be scaled horizontally

which is not supported (v2.1.0) natively by Airflow at the time of designing this solution.
 
 
If you are using commercially managed Airflow solution such as AWS MWAA,
 you should be able to store the DAGs in a s3 bucket, then you probably do not need this.

# Disclaimer

I am not an expert at OS level configurations, so some of the strategy used here may not be 
optimal, or secure. Please use at discretion, and PRs / patches are always welcomed.
 
# Usage

### Prepare the DAG folder repo 

Prepare another git repo to store your DAGs. 
Recommended to have a separate branch for different Airflow / data pipeline environments. 
So a possible git model could be:

`master/main` branch will be used to collect changes and PRs and deployed in staging environment,
`production` for actual Production Airflow. 
Local testing will be automatically using your personal development branch.

### Prepare the Plugin repo

This repo will be installed via pip into the image. You can either prepare it as a package,
 or simply do `pip install git+ssh ...` on a private or public repo
 
### Modify fields for local use

One important thing when developing your DAG is to visualise Airflow Tasks when building it,
so the strategy here used is to have your DAG repo and this Airflow scheduler repo resides in the 
same local environment.

The scheduler repo will read the DAG repo using the configured path, mount the directory as a volume into the 
container. Thus every changes you make in your local computer will instantly be reflected by the Airflow
hosted inside the container. 

To make this happen you will need to modify the following fields, all fields required modification are enclosed 
using `<>` sign. 

1. modify `.ssh/id_rsa` to include your deployment key if your plugin repo and DAG repo are private 
2. modify `docker/docker-compose.yml` to use the DAG folder name of your repo. This ensures that in local dev mode,
 we are using the local DAG folder mounted into the container
3. modify `.script/refresh_dags.sh` to use the DAG folder name of your repo
4. modify `.env` to include Environment Variables such as AWS credentials in your container environment
5. modify `Dockerfile` to include your git clone repo link and repo name, and your PRODUCTION branch, this will be overwritten
 if you are in local dev mode because of the `docker-composes.yml` file, in production depending on your container
 solution, remember to remove the `AIRFLOW__CORE__DAGS_FOLDER` overwrite to allow Airflow read DAG folder from the 
 path configured in the `airflow.cfg` 
6. modify `requirements.txt` to include your customized plugins as a third party library, and other 
 libraries if needed
7. modify `airflow.cfg` to include your DAG repo name (and other configurations if you need to)

### For deployment

For deployed environment, we will not be using any mounted volume, instead Environment Variables will be 
used to overwrite the existing functions.

Most importantly, you will need to make sure 

This includes those secrets such as `AIRFLOW__CELERY__RESULT_BACKEND`, `AIRFLOW__CORE__FERNET_KEY` and 
`AIRFLOW__CORE__SQL_ALCHEMY_CONN`.

### Start

- run `make build` to build the image
- run `make up` to start the service



# Improvements

- Make environment a configurable by the Environment Variable
 
 





