# Django Workshop Exercise 2

In this exercise we will go through the process of creating a model for the database, adding objects of the model into the database, then finally dynamically displaying these objects on a webpage based on the path specified.  
<br/><br/>
## Prepare for the coding environment  

SSH into the test machine. The password is 123456.
```sh
ssh your_upi@130.216.39.213
```
Once you are in, activate the python virtual environment and cd into the project folder
```sh
workon dj && cd mysite
```
<br/><br/>
## Create a new model
- The model should be called "Transportation"
- The model should have a many to one relationship with "ToDoList"
- the model should contain one string attribute called "type"

To start with, open the file with the name "models.py". Have a look at the model class called "Item",  your new model should be definied in a very similar manner.

<br/><br/>
## Migrate the new model
Once you are done with models.py, save it and go back to command line. Now we need to tell Django database about the existence of the new model. First we create a migration file:

```sh
python manage.py makemigrations main
```

Then we apply the migration

```sh
python manage.py migrate
```
If no error appears then the model has been successfully added.


<br/><br/>
## Add new objects to the model in the database
We will use python shell for adding objects. 
```sh
python manage.py shell
```
The first thing you want do is tell the shell about the model we want to interact with.
```sh
>>> from main.models import ToDoList, Transportation, Item
```

We will create a new "ToDoList" called "Alice's List"
```sh
>>> t = ToDoList(name="Alice's List")
>>> t.save()
```

Then we will add in a bunch of new "Transportation" objects to Alice's List
```sh
>>> t.transportation_set.create(type="bus")
<Transportation: bus>
>>> t.transportation_set.create(type="ferry")
<Transportation: ferry>
```

Now you have created a list of "Transportation" objects for Alice's List. If you query all the "Transportation" objects in Alice's List, it should return all the objects you just added.

```sh
>>> t.transportation_set.all()
<QuerySet [<Transportation: bus>, <Transportation: ferry>]>
```

Optional: If you have extra time, also create a list of "Item" objects for Alice's List

<br/><br/>
## Show "Transportation" objects on the webpage
Now we are done using the python shell.
```sh
>>> exit()
```

Open the file with the name "views.py". First modify the "Import lines" to import the "Transportation" object. 

Then, take a look at how the variable "items" are generated. Create another variable called "transportations" in a similar manner, so it contains all the types of the transportations that were added to Alice's List. 

Finally, modify the return statement so webpage will output the transportations belong to Alice's List.


<br/><br/>
## Start the server and test the website
Go back to the command line and start the server
```sh
./runproject
```

Copy the url from the output and paste it in your browser, followed by the path "Alice's List". When you execute this url, the website should show something similar to the following:

![alt text](https://github.com/phu004/django_part_two/blob/main/exercise2.png)





