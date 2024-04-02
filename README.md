# NLP-Vaccination-Sentiment-Analysis
This repository contains the necessary code and resources for participating in the Zindi NLP Challenge titled "To Vaccinate or Not to Vaccinate." The challenge revolves around developing a machine learning model that can effectively determine the sentiment (positive, neutral, negative) in Twitter posts related to vaccination topics. By analyzing public sentiment, the solution aims to aid public health organizations and policymakers in devising effective strategies for vaccine communication and promotion.

## Summary
|     Jupyter Notebook                       | Published Article|    Link To Working App on Hugging Face
| -------------                  | -------------    |    -----------------
|[Notebook with code and full analysis](https://github.com/rasmodev/NLP-Vaccination-Sentiment-Analysis/blob/main/dev/NLP_Vaccination_Sentiment_Analysis_RoBERTa.ipynb)|  [Published Article](https://medium.com/@rasmowanyama/sentiment-analysis-of-covid-19-tweets-from-model-training-to-docker-deployment-e73ba2a7aebf)               |[App Link](https://huggingface.co/spaces/rasmodev/Covid-19_Tweets_Sentiment_Analysis_App)

## App Interface
Add the text you want to analyze and click on the **SUBMIT** button.

### Before Prediction

![App Screenshot](https://github.com/rasmodev/NLP-Vaccination-Sentiment-Analysis/blob/main/screenshots/HF_No_Pred.png)

### Negative Prediction
![App Screenshot](https://github.com/rasmodev/NLP-Vaccination-Sentiment-Analysis/blob/main/screenshots/HF_Negative.png)

### Neutral Prediction
![App Screenshot](https://github.com/rasmodev/NLP-Vaccination-Sentiment-Analysis/blob/main/screenshots/HF_Neutral.png)

### Positive Prediction
![App Screenshot](https://github.com/rasmodev/NLP-Vaccination-Sentiment-Analysis/blob/main/screenshots/HF_Positive.png)

## Challenge Description

Work has begun towards developing a COVID-19 vaccine, and monitoring public sentiment towards vaccinations is crucial. The challenge involves classifying Twitter posts as positive, neutral, or negative regarding vaccinations.

## Dataset

The dataset consists of labeled Twitter posts, each assigned a sentiment label (-1 for negative, 0 for neutral, 1 for positive). The `data` folder contains the following files:
- `Train.csv`: Labeled tweets for model training.
- `Test.csv`: Tweets for model testing.
- `SampleSubmission.csv`: Example submission format.

## Approach

1. Data Preprocessing: Tokenization, lowercasing, removing special characters, etc.
2. Model Selection: Choosing a pre-trained Hugging Face transformer model.
3. Fine-Tuning: Training the model on the training data.
4. Validation: Evaluating the model on the validation set.
5. Gradio App: Creating a user-friendly interface for the model using Gradio.
6. Model Deployment: Uploading the model and pipeline to the HuggingFace platform.
7. Dockerization: Containerizing the Gradio app for cloud deployment.

## Getting Started
### 1. Installing the required packages
pip install -r requirements.txt


### 2. Follow the notebooks in the `notebooks` folder for step-by-step guidance.

Explore the `app` folder for the Gradio app code and `docker` folder for Docker-related files.

## Usage

- Run the Jupyter notebooks in the `notebooks` folder to preprocess data, train the model, and evaluate its performance.
- Navigate to the `app` folder and run the Gradio app:
cd app
python app.py

markdown
Copy code
- For cloud deployment, follow the Dockerization instructions in the `docker` folder.

## Contributing

Contributions are welcome! Feel free to open issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
You can customize the repository structure, README content, and instructions based on your actual project progress and needs. Make sure to replace yourusername with your actual GitHub username in the repository clone link.

Remember to add your code files, notebooks, and any additional resources to the respective folders in the repository. If you have specific questions or need further assistance, feel free to ask!
