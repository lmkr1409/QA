<!-- TOC -->

- [Database design](#database-design)
    - [courses](#courses)
    - [questions](#questions)
    - [answers](#answers)
    - [exam](#exam)
    - [exam_questions](#exam_questions)
- [API Specifications](#api-specifications)
    - [[GET] fetch all courses](#get-fetch-all-courses)
    - [[POST] create course](#post-create-course)
    - [[GET] question details and their answers](#get-question-details-and-their-answers)
    - [[GET] list of questions](#get-list-of-questions)
    - [[GET] list of answers for a question](#get-list-of-answers-for-a-question)
    - [[POST] create answer for a question](#post-create-answer-for-a-question)
    - [[POST] submit exam](#post-submit-exam)

<!-- /TOC -->

## Database design

### courses

column|datatype|description
--|--|--|
c_id | int | primary key column
course_name | varchar | Name of the Course
created_on | timestamp | Course creation time

### questions

column|datatype|description
--|--|--|
q_id|int|primary key column
question|varchar| Actual question
single_or_multi| enum(Single/Multi) | describes if the questions answer is single value or multiple values
positive_score| float | score for correct answer
negative_score | float | Negative scoring for wrong answer
c_id | int | Foreign key column referencing courses

### answers

column|datatype|description
--|--|--|
a_id | int | primary key column
option | varchar | content of answer
is_correct | boolean | Is this option is 100% correct
q_id | int | Foreign key column referencing questions table

### exam

column|datatype|description
--|--|--|
e_id | int | each exam id
score | float | score obtained in the exam
max_score | float | maximum score of the exam

### exam_questions

column|datatype|description
--|--|--|
eq_id | int| primary key column
e_id | int | Foreign key column referencing exam table
q_id | int | Foreign key column referencing questions table
selected_option | int | Foreign key column referencing answers table


## API Specifications

### [GET] fetch all courses
> /course/

### [POST] create course
> /course/

### [GET] question details and their answers

> /fetch_question_nd_answers?c_id=1

### [GET] list of questions

> /list_of_questions?c_id=1

### [GET] list of answers for a question
> /answers?q_id=1

### [POST] create answer for a question
> /answers

### [POST] submit exam
> submit_exam

* Request
```json
{
    "course_id":123,
    "score":20,
    "max_score":25,
    "exam_questions":[
        {
            "question":"Question 1",
            "option":"Option 1",
            "is_correct":"False"
        },
        {
            "question":"Question 2",
            "option":"Option 2",
            "is_correct":"False"
        }
    ]
}
```
