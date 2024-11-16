# Medical Domain : Disease Analysis using Multi-model `(Images, Texts, Videos and Audios)`

What is multi-model ?

It is a multimodal model with text, visual, and audio input and output capabilities

What is GPT-4.o and GPT-4 Vision ?

It is a multimodal model with text, visual, and audio input and output capabilities, building on the previous iteration of GPT-4 with Vision model, GPT-4 Turbo. The power and speed of GPT-4o come from being a single model handling multiple modalities. Previous GPT-4 versions used multiple single-purpose models (voice to text, text to voice, text to image) and created a fragmented experience of switching between models for different tasks. GPT-4o has a 128K context window and has a knowledge cut-off date of October 2023.

What is Gemini multi-model ?

Hugging face based multi-model like Lemma 3.2, Mistral etc

How to access these multi-models ?

We needed to first download onto our local machine via sending a access requirest but they require huge storage becouse model size is huge thus the inference time will be large to response to any prompt

We will use the GPT-4 Vision model for disease analysis for given a medical test image and how to diagnose the disease so, it act as assistant. eg : skin disease image and give you suggesion.

Deployment - Cloud Platform

Docker(Image Containerization) - for creating inter(user interface like flask, django and fast api or streamlit) application

OpenAI, Bedrock(AWS), VertexAI(GCP), Azure OpenAI(Microsoft) - all platform provides multi-model.

We will deploy it using azure open ai on azure cloud thus explore generative ai in cloud using azure. or Generative Ai in cloud using AWS.

Why to use them for our application becouse they are already tested, secure and very power full tools if we use the third party tool then we have to externally install it on our dev enviroment.

Onen LLM vs Cloud LLM

Open Source multi-models have very high cost to run the deployment while cloud services are cost efficients.


### Project Setup : How to run the project

1. Create a new enviroment
```bash
conda create -n multi-model python=3.10 -y

conda list
```
2. Activation of multi-model conda enviroment
```bash
conda activate multi-model
```

3. To install the all required packages for the projects.
```bash
pip list
pip install -r requirements.txt
```

4. run the deployement
```bash
streamlib run app.py
```


## Reference

1. [Everything You Need to Know About GPT-4o - DEV Community](https://dev.to/mohith/everything-you-need-to-know-about-gpt-4o-29cm)
2. [intro_gemini_multimodal_use_cases.ipynb - Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/intro_multimodal_use_cases.ipynb#scrollTo=RQT500QqVPIb)
