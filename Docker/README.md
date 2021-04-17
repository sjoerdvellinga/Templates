# Creation of dockerfiles

* create a new directory  
mkdir Example1  
cd Example1  
* create a file in the present working directory  
touch Dockerfile  
* open the file in any text editor, such as VS Code  
code .  
  
# Template for flask-dockerfile
******************************************************
FROM python:3.7.2-slim  
  
COPY . /app  
WORKDIR /app  
  
RUN pip install --upgrade pip  
RUN pip install flask  
  
  
ENTRYPOINT [“python”, “app.py”]  
******************************************************