# LP4-Machine-Learning-Web-Apps-Using-Streamlit-and-Gradio
Model deployment forms part of the CRISP-DM framework and its importance cannot be overlooked. Model Deployment is the method by which you integrate a machine learning model into an existing production environment to make practical business decisions based on data. 

## Objectives of this project
1. Building customizable Graphic User Interface components with Streamlit and Gradio.
2. Deploying Machine Learning models to Streamlit App for real-time prediction.
3. Deploying Machine Learning models to Gradio App for real-time prediction.

There are many ways to make web interfaces to allow interaction with Machine Learning models and we will cover two of them.

[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![MIT licensed](https://img.shields.io/badge/license-mit-blue?style=for-the-badge&logo=appveyor)](./LICENSE)
![Issues](https://img.shields.io/github/issues/PapiHack/wimlds-demo?style=for-the-badge&logo=appveyor)
![PR](https://img.shields.io/github/issues-pr/PapiHack/wimlds-demo?style=for-the-badge&logo=appveyor)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

## Introduction

Now that you know how to build some Machine Learning models, it is the time to discover how to embeded it into a web app with a user-friendly interface. You have already saw, of course, some ML tools and you maybe played with it. If so, you know that it is much more interesting to interact with a ML model through a beautiful interface than using a notebook, especially when you are not an expert of this domain.  

In this project, we aim to help you to discover how to embed a ML model into a web app to interact with it much easier, by inputing the required information, making predictions and showing the result.


<!-- You can find the slides of my talk at <https://meissa-wimlds-presentation.netlify.app>. -->

## Description

<!-- 
[gradio](https://gradio.app/)
[streamlit](https://streamlit.io/)
-->

You will have a minimal interface demo with [Gradio](https://gradio.app/) & [Streamlit](https://streamlit.io/), this will just serve you to make sure that everything works correctly. Then, you will have to make your own interfaces, those allowing you to interact with a Machine Learning model, that is to say:
- Pass values through the interface;
- Recover these values in backend;
- Apply the necessary processing;
- Submit the previously processed values to the ML model to make the predictions;
- Process the predictions obtained and display them on the interface.

## Instructions

Your task is to understand the frameworks and build your app integrating a ML model.
Clone this repository to use it as a template, do not forget to change the readme at the end of the project.
Your work should follow these next steps.

1.  Build a Streamlit app, during 2 first weeks, to embed the regression model you built a few weeks ago. 

2.  Build a Gradio app, during 2 last weeks, to embed the classification model you built a few weeks ago.


Upon completion of your project, you are required to write a blog post
on your thought process on medium, LinkedIn, personal blog, or any other
suitable blogging site.

## Rubrics

Streamlit:

-   **Excellent:** Have an that works correctly with a nice and personalized interface.

-   **Good:** Have an app that launches, makes prediction and shows result.

-   **Fair:** Have an app that launches but having bugs regarding prediction or interface.


Gradio:

-   **Excellent:** Have an that works correctly with a nice and personalized interface.

-   **Good:** Have an app that launches, makes prediction and shows result.

-   **Fair:** Have an app that launches but having bugs regarding prediction or interface.

## Installation

You have two ways in order to setup and run this project.

### Manual Setup

For manual installation, you need to have [`Python3`](https://www.python.org/) on your system. Then you can clone this repo and being at the repo's `root :: friendly_web_interface_for_ML_models> ...`  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

The both long command-lines have a same structure, they pipe multiple commands using the symbol **;** but you may manually execute them one after another.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that it will be allow to import them into the python's scripts and notebooks without any issue.


## Resources
Here are some ressources you would read to have a good understanding of Gradio and Streamlit :
- [Get started with Streamlit](https://docs.streamlit.io/library/get-started/create-an-app)

- [Get started with Gradio](https://gradio.app/getting_started/)





## Author

- .[Jonas AFUTU](https://www.linkedin.com/in/jonas-afutu/)
