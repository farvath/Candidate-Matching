## Candidate Matching
This project implements a candidate matching system that recommends suitable candidates for job openings. It leverages machine learning techniques to analyze historical hiring data and improve matching accuracy.

## Key features
1. **Text Vectorization:**  Uses TF-IDF vectorization to represent job descriptions and candidate profiles as numerical features.
2. **Similarity Calculation:** Employs cosine similarity to measure the similarity between job requirements and candidate qualifications based on their vector representations. (Initial approach focused on titles and skills, later expanded to include profile descriptions as well)

## Dataset 
Dataset for creating candidate profile : [Link](https://www.kaggle.com/stackoverflow/stack-overflow-2018-developer-survey#survey_results_public.csv)
Dataset for job-postings [Link](https://www.kaggle.com/PromptCloudHQ/us-technology-jobs-on-dicecom)

## Feature Extraction and preprocessing
1. Initially traditional EDA was done on both the dataset . Duplicates and non english words were removed (NLTK Libraries).
2. Stopword removal and stemming can improve the accuracy of similarity comparisons (Porter's Stemmer).
3. An adjustable threshold in the `create_similarity_dictionary` function allows us  to control the level of strictness for considering job titles as similar (You may refer `preprocessing/cleaning_recommendations.ipynb`).
4. Cleaned and merged dataset can be found in `data/cleaned_recommendation`.
5. Complete Inference has been done on the dataset and results can be found in `inference.ipynb` file.


## Usage
You may indiviually run the `End-to-End/Candidate_Matching.ipynb` file or run using streamlit application :

1. First clone the repository :
    ```bash
    git clone https://github.com/farvath/Candidate-Matching.git
    ```
2. Replace the pre-processed data paths stored in pickle files (e.g., df.pkl and similarity.pkl), make sure these files are present in the same directory as your application (app.py).
3. In your terminal, navigate to your project directory(app.py) and run the following command:
   ```bash
   streamlit run app.py
   ```

## Interface
<img src="https://github.com/farvath/ChessCognito/blob/main/setup.jpg" width="400px" height="400px" alt="alt text">