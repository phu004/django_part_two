# Django Workshop Exercise 2
![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)


In this exercise we will go through the process of creating a model for the database, adding objects of the model into the database, then finally dynamically displaying these objects on a webpage based on the path specified.  


\
\
\


## Prepare for the coding environment  

SSH into the test machine. The password is 123456.
```sh
ssh your_upi@130.216.39.213
```
Once you are in, activate the python virtual environment and cd into the project folder
```sh
workon dj && cd mysite
```

## Create a new model
- The model should be called "Transportation"
- The model should have a many to one relation ship with ToDoList
- the model should contain one string attribute called "type"

To start with, open the file with the name "models.py". Have a look at the model class called "Item",  your new model should be definied in a very similar manner.

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

You can create as many "Transportation" objects as you want. When you query all the "Transportation" objects in Alice's List, it should return all the objects you just added.

```sh
>>> t.transportation_set.all()
<QuerySet [<Transportation: bus>, <Transportation: ferry>]>
```


## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

## Docker

Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd dillinger
docker build -t <youruser>/dillinger:${package.json.version} .
```

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```




