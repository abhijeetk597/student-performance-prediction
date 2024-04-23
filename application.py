from fastapi import FastAPI, Form
import uvicorn
from enum import Enum
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = FastAPI()

class Lunch(str, Enum):
    a = "free/reduced"
    b = "standard"

class PEdu(str, Enum):
    a = "associate's degree"
    b = "bachelor's degree"
    c = "high school"
    d = "master's degree"
    e = "some college"
    f = "some high school"

class Gender(str, Enum):
    a = "male"
    b = "female"

class RaceEthnicity(str, Enum):
    a = "group A"
    b = "group B"
    c = "group C"
    d = "group D"
    e = "group E"

class TestPrepCourse(str, Enum):
    a = "none"
    b = "completed"


@app.post('/predict')
async def predict_salary(
    # gender: str = Form(...),
    # race_ethnicity: str = Form(...),
    # parental_level_of_education: str = Form(...),
    # lunch: str = Form(...),
    # test_preparation_course: str = Form(...),
    # reading_score: int = Form(...),
    # writing_score: int = Form(...)

    gender: Gender = Gender.a,
    race_ethnicity: RaceEthnicity = RaceEthnicity.a,
    parental_level_of_education: PEdu = PEdu.a,
    lunch: Lunch = Lunch.a,
    test_preparation_course: TestPrepCourse = TestPrepCourse.a,
    reading_score: int = Form(...),
    writing_score: int = Form(...)
                        ):
    data = CustomData(gender = gender,
                        race_ethnicity = race_ethnicity,
                        parental_level_of_education = parental_level_of_education,
                        lunch = lunch,
                        test_preparation_course = test_preparation_course,
                        reading_score = reading_score,
                        writing_score = writing_score)
    pred_df=data.get_data_as_data_frame()
    predict_pipeline=PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    return {float(results[0])}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
