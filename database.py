import pyrebase

# Initialize Firebase
config = {
    "apiKey": "AIzaSyDDWjmjfLtBIjkXp3z_6dYXeX3mdiyHnS8",
    "authDomain": "rika-snake.firebaseapp.com",
    "databaseURL": "https://rika-snake.firebaseio.com",
    "projectId": "rika-snake",
    "storageBucket": "rika-snake.appspot.com",
    "messagingSenderId": "868414796418"
}

firebase = pyrebase.initialize_app(config)