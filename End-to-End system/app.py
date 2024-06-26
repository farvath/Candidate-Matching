import streamlit as st
import pandas as pd
import pickle

df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(title):
    """Recommends similar jobs based on pre-computed similarity matrix.

    Args:
        title (str): The job to find similar positions for.

    Returns:
        list: A list of dictionaries containing details of the top 5 most
             similar job titles, including `uniq_id`, `jobtitle`, `company`,
             `jobdescription`, and `advertiserurl` (assuming these columns exist
             in `job_df`). If the title doesn't exist, returns an error message.
    """

    try:
        idx = df[df['jobtitle'] == title].index[0]
        idx = df.index.get_loc(idx)
    except IndexError:
        return f"The job title '{title}' does not exist in the dataset."

    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])[1:5]

    jobs = []
    for i in distances:
        job_details = {
            'Job Id': df.iloc[i[0]].uniq_id,
            'job title': df.iloc[i[0]].jobtitle,
            'company': df.iloc[i[0]].company,
            'Apply Link': df.iloc[i[0]].advertiserurl
        }
        jobs.append(job_details)

    return jobs


# Streamlit web app
st.title('Candidate Matching')

title = st.selectbox('Search Title', df['jobtitle'])

jobs = recommend(title)

if jobs:

    st.subheader('Current Job Openings :')

    # Convert recommendations to pandas DataFrame for table display
    df_jobs = pd.DataFrame(jobs)

    # Display recommendations as HTML table with styling
    st.write(df_jobs.to_html(escape=False, border=0, index=False), unsafe_allow_html=True)

else:
    st.write(f"Currently no jobs available for '{title}'.")
