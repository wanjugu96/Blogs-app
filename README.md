# Blog post  App

## Author

[Wanjugu-Mung'au](https://github.com/wanjugu96)

# Description
This is an application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

## Live Demo

Click [Link](https://pitches-application.herokuapp.com/) to visit the site


## User Story
1. As a user, I would like to view the blog posts on the site
2. As a user, I would like to comment on blog posts
3. As a user, I would like to view the most recent posts
4. As a user, I would like to an email alert when a new post is made by joining a subscription.
5. As a user, I would like to see random quotes on the site
6. As a writer, I would like to sign in to the blog.
7. As a writer, I would also like to create a blog from the application.
8. As a writer, I would like to delete comments that I find insulting or degrading.
9. As a writer, I would like to update or delete blogs I have created.
## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  git clone https://github.com/wanjugu96/Blogs-app.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd pitches App
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
    export SECRET_KEY=<your key>
    
  ```
4. Running the application by :
  ```bash
  python3.6 manage.py server
  ```
  OR run the application by :
  ```bash
  bash start.sh on your terminal
  ```

5. Testing the application
  ```bash
  python3.6 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [shellmithwanjjugu98@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2019 **Wanjugu Mung'au**