from app.app import create_app

app = create_app()

if __name__ == '__main__': #makes sure the server is only started if the run.py file is executed directly and not executed whenever we access the file by e.g. importing it
    app.run() #run our app as a web server