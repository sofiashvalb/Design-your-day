# Design your Day
#### Video Demo:  https://youtu.be/qaoZ3I1CrKg
#### Description:
My project is a web-based application for controlling your daily tasks.
I am using HTML, CSS and JavaScript for front-end and python with flask and jinja for back-end. 
In the final-project folder you will find two sqlite files, app.py, static folder and a templates folder. In this README file I will go through every folder and explain what each file does.

The tasks.db sqlite file contains a database table of tasks with the inserted tasks by the users. Every task gets its own id, time text which is optional and an importance status which is might/must.
The quotes.db database table is a table of quotes, with phrases, an author for each quote and its id. 

The static folder consists of five jpeg/jpg files that I used for inserting images in my HTML files. It has and images of the sunflower which is my logo, and four other pictures that I use in the suggest.html file fot my "suggestions" tab. Also there is a style.css file where I wrote all my styling designs. I've used "Bootstrap" link and W3schools" for some basic CSS styling and focus my personal additions in the style.css. In the slyle.css file you will find not only the use of different fonts and colors, border-radiuses and paddings. You will also see the reference to a smaller screens and different scalings. I did asked for suggestions from the cs50.ai duck which was very helpful.
Though I could've use a Javascript file on his on, I decided to use <script> tags inside my HTMLs instead. 

The templates folder contains all my HTMLs. You can see the layout.html as my main template for the other files. It has the building blocks of the navigation bar and the side-bars which are showing throughout the web-application. The layout.html file has the Bootstrap and the stylesheet links to connect to within the whole project. It has a <meta> tag for the different languages and page scales. 
Also you can see the navigation bar built in the header of the file, body and footer.
The body has a special grid that devides the page to three coloumns. The ledt and right ones are permanent while the centered one is the chaging part, using flask {% block body %}{% endblock %}. These brackets are basically the "placeholder" for the other HTML files to insert there content into.

The home.html has jinja {{ }} to contain the different quotes that are rundomely chosen from quotes.db. Each time you refresh, a new phrase will apear. Going forward you can see a task table that is updating threw the task.db database, deppending on the users input. It shows some of the same elements of the table in the task.db. The task name, time and importance. It also has a status change option. By using JavaScript function, the user gets to pick the status of the task (done, in progress, to do) and it gets saved in the local storage. You will also see a DELETE button on the right as an "X". This will DELETE from the tasks.db table the spesific row the user is finished with.

The tasks.html file inserts in the layout flask "placeholder" a form, where the user can isnert his tasks with <input> tags. Basically inserting input into the task.db file. After clicking sumbmit, there's a JavaScript onclick alert function that will show that the task has been added. Now it will appear in the main page in the table, and also in the task.db database. 

The suggest.html file has four images for the user to enjoy as tips for a better life.
It has a grid of 2 rows and 2 coloumns just as a design choice.

Going back to the main folder, you'll find the app.py file, which is the main and the most important one. The easy thing for me would be to import CS50 library with it's SQL, but I decided to import sqlite3 instead. I've imported flask libraries and random.
The import random is for the random quotes in the main page. 
app.py consists of different routes that wait for the users input (method "POST") to render the templates and update the databases. You can see how if there is an input, the code detectes the veriables in the different databases (As explained before) and UPDATES\INSERTES\DELETES\SELECTES the correct information from the sqlite databases and then returns back the new tables for show. 

As you can see, my final CS50 project contains many elements with the use of the many coding languages i've learn, like python, flask, jinja, HTML, CSS, JavaScript. 