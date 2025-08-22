### Note: This repository was created as a **teaching kit** for IEEE Epsilon 2021, where I conducted a workshop on building and deploying an end-to-end ML application with Streamlit and GCP.For the cloud deployment setup, I adapted standard boilerplate files (Dockerfile, Makefile, app.py, app.yaml) from [Mark Douthwaite’s Streamlit project template](https://github.com/markdouthwaite/streamlit-project). All other components — the diabetes dataset, EDA notebooks, CNN model, student-friendly Streamlit app, and step-by-step workshop instructions — were developed by me specifically for this training context.  
### This repo is intentionally beginner-oriented, designed to help participants follow along and learn. It is not meant to represent advanced ML research or production-grade systems.



# IEEE Epsilon 2021

![image](https://user-images.githubusercontent.com/17146805/113475152-7b9d3080-9491-11eb-9dff-bf140b9f494a.png)


EEE SIES GST with its sub-chapters MTT-S and Computer Society in feature intends to conduct a Symposium which will be an Academic Convention wherein the invited Industry Experts will speak about a particular subject of their research. The topics will run along the track of a theme for the Symposium. The target is to create an educational and orderly ambience where ideas are addressed and exchanged. This kit was designed to help participants follow along with the workshop.

### Project Objective 
Teach beginners how to develop an end-to-end application that accepts patient data and predicts if they have diabetes or not. 

### Project Description 
* Analyze data and generate visuals for better understanding using the Python libraries Pandas, Numpy, Matplotlib, Plotly & Seaborn. 
* Conceptualize and developed a CNN using Tensorflow and Keras to predict if a patient is diabetic or not. 
* Build a CNN model and develop an application using Python's Streamlit package. 
* Deploy the Streamlit application to the cloud using Google Cloud Platform's App Engine. 
 

#  Contents:

 [data](https://github.com/VinitaSilaparasetty/ieee_epsilon_2021/tree/master/data): Contains the data for the model and the data for the streamlit app.

 [deploy](https://github.com/VinitaSilaparasetty/ieee_epsilon_2021/tree/master/deploy): Contains all the files to deploy the app.

 [eda](https://github.com/VinitaSilaparasetty/ieee_epsilon_2021/tree/master/eda): Contains the jupyter notebook with the analysis and preparation of the data.


# Instructions to use this Kit:

![image](https://user-images.githubusercontent.com/17146805/113475203-be5f0880-9491-11eb-8cec-a67810719367.png)

1) Use the jupyter notebook in [eda](https://github.com/VinitaSilaparasetty/ieee_epsilon_2021/tree/master/eda) to prepare diabetes.csv (You can find it [here](https://github.com/VinitaSilaparasetty/ieee_epsilon_2021/tree/master/data))

2) All the files required for deployment can be found in [deploy](https://github.com/VinitaSilaparasetty/ieee_epsilon_2021/tree/master/deploy)

3) Follow the instructions in [Deploymnet Instructions](https://github.com/VinitaSilaparasetty/ieee_epsilon_2021/blob/master/Deployment%20Instructions.pdf) to deploy the streamlit app.

4) Use patient_records.csv to test the streamlit app after deployment.


[Linkedin](https://www.linkedin.com/in/vinita-silaparasetty/)


