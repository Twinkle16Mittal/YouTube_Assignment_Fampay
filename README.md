# YouTube_Assignment_Fampay

How to set up locally in your system..

1 First make the directory using command "mkdir djangoyoutube"

2 Create Virtualenv "python3 -m venv venv"

3. Activate Virtualenv "source /venv/bin/activate

4. Install requirements.txt "pip install -r requirements.txt"

5 Before Starting the server first tou need to create database in your postgres .

  Run these commands
  - psql postgres (to activate postgres server)
  - create database youtubedata;
  - \c youtubedata (Connected youtubedata locally)
  - \dt (check how many tables are present inside this Database)
  
5 Run the command in the terminal "python3 manage.py runserver"

6. In the other terminal(same repository activate virtualenv) run "python3 manage.py process_tasks

If you Hit the Rest Api using Postman 

 Method = "GET" ,http://127.0.0.1:8000/data/ 

 Method "POST" , parmas = title and description , http://127.0.0.1:8000/data/
 
 
 
 




