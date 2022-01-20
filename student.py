import pandas as pd
import plotly_express as px

df=pd.read_csv("student.csv")
student=df.groupby(["student_id","level"] ,as_index=False)["attempt"].mean()

scatter=px.scatter(student, x="student_id", y="level", 
size="attempt", color="attempt")
scatter.show()