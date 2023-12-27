## Database design

* courses

column|datatype|description
--|--|--|
c_id | int | primary key column
course_name | varchar | Name of the Course
created_on | timestamp | Course creation time

* questions

column|datatype|description
--|--|--|
q_id|int|primary key column
question|varchar| Actual question
single_or_multi| enum(Single/Multi) | describes if the questions answer is single value or multiple values
positive_score| float | score for correct answer
negative_score | float | Negative scoring for wrong answer
c_id | int | Foreign key column referencing courses

* answers

column|datatype|description
--|--|--|
a_id | int | primary key column
option | varchar | content of answer
is_correct | boolean | Is this option is 100% correct
q_id | int | Foreign key column referencing questions table

* exam

column|datatype|description
--|--|--|
e_id | int | each exam id
score | float | score obtained in the exam
max_score | float | maximum score of the exam

* exam_questions

column|datatype|description
--|--|--|
eq_id | int| primary key column
e_id | int | Foreign key column referencing exam table
q_id | int | Foreign key column referencing questions table
selected_option | int | Foreign key column referencing answers table


## API Specifications