# streamlit new features (1.11) , cloud  and docker test
maybe a bit much in one test...


## build the docker container named 'streamlit_features'
- following [this simple demo](https://www.section.io/engineering-education/how-to-deploy-streamlit-app-with-docker/)
- the content is defined in Dockerfile
- using Docker with a WSL 2 Ubuntu 20.04 distro
> docker build -t streamlit_features:latest .

## run the docker container:

> docker run -p 8501:8501 streamlit_features:latest

The docker container can also be started from the windows Docker App!