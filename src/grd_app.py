import gradio as gr
import pandas as pd
import pickle
import os


import gradio as gr

def predict_churn(gender, contract, internet_service, online_security, online_backup,
                  device_protection, tech_support, streaming_tv, streaming_movies):
    # Perform churn prediction based on the input features
    # Replace this with your actual prediction code
    prediction = "Churn prediction"

    return prediction

gr.Interface(
    fn=predict_churn,
    inputs=[gr.inputs.Dropdown(['Female', 'Male'], label='Gender'),
            gr.inputs.Dropdown(['Month-to-month', 'One year', 'Two year'], label='Contract'),
            gr.inputs.Dropdown(['DSL', 'Fiber optic', 'No'], label='Internet Service'),
            gr.inputs.Radio(['Yes', 'No', 'No internet service'], label="Online Security"),
            gr.inputs.Radio(['Yes', 'No', 'No internet service'], label="Online Backup"),
            gr.inputs.Radio(['Yes', 'No', 'No internet service'], label="Device Protection"),
            gr.inputs.Radio(['Yes', 'No', 'No internet service'], label="Tech Support"),
            gr.inputs.Radio(['Yes', 'No', 'No internet service'], label="TV Streaming"),
            gr.inputs.Radio(['Yes', 'No', 'No internet service'], label="Movie Streaming")],
    outputs=gr.outputs.Label(),
    title="Customer Churn Prediction App",
    description="Let's Get Started With Some Predictions!"
).launch()
