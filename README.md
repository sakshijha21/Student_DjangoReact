# Student_DjangoReact
A three page web portal that captures marks of students in one page and displays the leaderboard in another page  Frontend has a Homepage having 2 choices Enter marks View Leaderboard  Enter marks page Takes  Roll No  Name Marks in Maths Marks in Physics Marks in Chemistry Total Automatically calculated Percentage View Leaderboard Page  Grid to display the rankings of the students based on percentage by default and  having sorting and searching functionality For frontend reactjs and backend django is used MySQL Datastore is used for storing of marks
 Go to Command Prompt and enter cd "C:\Program Files\MySQL\MySQL Server 8.0\bin"-> Enter password and get into mysql msql->create databse "info"; mysql->use info;

Open folder Project>backend run following commands Install Django with "pip install django", to have the django-admin command available. ->python manage.py makemigrations ->python manage.py migrate ->python manage.py runserver go to 'http://127.0.0.1:8000/student/'

In other terminal open project->frontend ->install npm ->npm start go to 'http://localhost:3000/'
