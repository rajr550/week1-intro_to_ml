import pandas as pd
import numpy as np
scores=np.random.randint(50,101,size=10)
df=pd.DataFrame({"Name":["Raj","Sham","Karan","karn","ram","rajesh","mahesh","aditya","dhruv","vaishnav"],
               "Subject":["maths","science","english","maths","maths","english","science","science","maths","english"],
               "Score":scores,
               "grade":""})
def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

df["Grade"] = df["Score"].apply(assign_grade)

sorted_df = df.sort_values(by='Score', ascending=False)
print(sorted_df)

avg_score = df.groupby('Subject')['Score'].mean()
print(avg_score)
def pandas_filter_pass(dataframe):
    return dataframe[dataframe['Grade'].isin(['A', 'B'])]
