# gpt-for-pdf

# How to use

Clone this repository:

```
$ git clone https://github.com/ramoonmedeiro/gpt-for-pdf.git
```

Change directory to gpt-for-pdf:

```
$ cd gpt-for-pdf/
```
Create a .env file with OPENAI API KEY, ex: OPENAI_API_KEY='sk-...'

Create a virtual environment and download the requirements.txt:

```
$ python3 -m venv venv
$ pip3 install -r requirements.txt
```

Run streamlit server and access in http:localhost:8501 or run the Dockerfile:

```
$ docker build . -t gpt_pdf_server:1.0
$ docker container run -d -p 8501:8501 gpt_pdf_server:1.0
```
