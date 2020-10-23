# Deathfret Guitar

## Milestone Project 4 - Full Stack Frameworks with Django

The final project as part of [Code Institute](https://codeinstitute.net)'s full stack software development course ties together all aspects of full stack developemnt
in one comprehensive application. Using the Django full stack framework, the goal is to create an online service app that will be able to handle user authenticaation as well
as a payment system for a product and/or service.

As a guitarist with over 20 years experience playing, recording and touring, I have always dreamt of creating a community of up and coming players, in which the more prevalant
who have anything to teach will be able to do so for a subscribing user. Specifically I have been a part of the extreme metal niche of the industry for many years and have noticed that
such a platform does not currently exist for this particular genre.

The site will be a subscription based site, where a member will be able to access lessons and masterclasses of talented guitarists for a small monthly, or yearly fee. The idea will be
for the site owner(s) to source players who would be willing to write and record a lesson series, which will then be available for paying members in their very own members area. At the time of writing however, this collaborative content has not yet been created, so while the project is being built, only example lesson plans by sourced players will be used. The structure of the site
will be the same.

The site will also feature a webstore of branded merchandise that a subscribing user or shopper will be able to purchase.

![]( "")

***

## Contents

1. [UX](https://github.com/vdgvzr/milestone-project-4#ux)
    - [Goals](https://github.com/vdgvzr/milestone-project-4#goals)
    - [Developer Goals](https://github.com/vdgvzr/milestone-project-4#developer-goals)
    - [User Stories](https://github.com/vdgvzr/milestone-project-4#user-stories)
    - [Design](https://github.com/vdgvzr/milestone-project-4#design)
        - [Frameworks](https://github.com/vdgvzr/milestone-project-4#frameworks)
        - [Colours Used](https://github.com/vdgvzr/milestone-project-4#colours-used)
        - [Fonts](https://github.com/vdgvzr/milestone-project-4#fonts)
        - [Icons](https://github.com/vdgvzr/milestone-project-4#icons)
        - [Wireframes](https://github.com/vdgvzr/milestone-project-4#wireframes)
2. [Features](https://github.com/vdgvzr/milestone-project-4#features)
    - [Existing Features](https://github.com/vdgvzr/milestone-project-4#existing-features)
    - [Features Left to Implement](https://github.com/vdgvzr/milestone-project-4#features-left-to-implement)
3. [Testing](https://github.com/vdgvzr/milestone-project-4#testing)
4. [Validation](https://github.com/vdgvzr/milestone-project-4#validation)
    - [HTML](https://github.com/vdgvzr/milestone-project-4#html)
    - [CSS](https://github.com/vdgvzr/milestone-project-4#css)
    - [JavaScript](https://github.com/vdgvzr/milestone-project-4#javascript)
    - [Python](https://github.com/vdgvzr/milestone-project-4#python)
    - [Compatibility](https://github.com/vdgvzr/milestone-project-4#compatibility)
5. [Deployment](https://github.com/vdgvzr/milestone-project-4#deployment)
    - [Deploying The Site](https://github.com/vdgvzr/milestone-project-4#deploying-the-site)
    - [Deploying Locally](https://github.com/vdgvzr/milestone-project-4#deploying-locally)
6. [Technologies Used](https://github.com/vdgvzr/milestone-project-4#technologies-used)
7. [Credits](https://github.com/vdgvzr/milestone-project-4#credits)
    - [Content](https://github.com/vdgvzr/milestone-project-4#content)
    - [Media](https://github.com/vdgvzr/milestone-project-4#media)
    - [Code](https://github.com/vdgvzr/milestone-project-4#code)
    - [Acknowledements](https://github.com/vdgvzr/milestone-project-4#acknowledgements)

***

## UX

### Goals



### Developer Goals



### User Stories

As a user, I would like to be able to:

* Viewing and Navigation

- [x] View a list of artist masterclasses so that I can make a decision to subscribe based on whether or not the lessons will be valuable to me.
- [x] View a list of products so that I can select some to purchase.
- [x] View individual product details so I can see the price, detail, size and stock availibility of the selected product.
- [x] View the total of my purchases at any time so I can keep track of my spending.

* Registration and user accounts

- [x] Register for an account so that I can have access to the content provided.
- [x] Easily login or logout so I can access my personal account information.
- [x] Recover my password in case I forget it.
- [x] Recieve and email confirmation after registering so that I can see that my registration was successful.
- [x] Be able to view a personalised user profile so that I can keep track of my subscription status and personal details.

* Searching

- [x] Search for a lesson by artist name or description so that I can quickly find the content I need.

* Purchasing and checkout

- [x] Easily select which subscription method is best for me so that I can leep track of my spending.
- [x] Easily select the size and quantity of a prouct, if available, and view at checkout so that I can ensure a correct selction was made before purchase.

***

### Design



#### Frameworks

* []()
    - 

#### Colours Used



Colours:

- ![]() ``

Materialize Colors:

- ![]() ``

#### Fonts

![]( "")



#### Icons

[]()

#### Wireframes

The initial wireframing design was created using [Balsamiq](https://balsamiq.cloud/).

High quality wireframes of the site can be found [here](deathfret-wireframe.pdf "Wireframes").

***

## Features

### Existing Features

#### 

* 

### Features Left to Implement

* 

***

## Testing

### 



### Other Bugs and Problems

*  

***

## Validation

### HTML

* []()

### Compatibility

* 
    - 

***

## Deployment

### Deploying The Site

To deploy the app on Heroku, the following steps have been followed:

1. Log into Heroku, and create new app by providing app name and nearest location of deployment.

2. Under the resources tab, provision the Heroku Postgres database as a new Add-on. This will be used as the deployment database.

3. To use Heroku Postgres, in the terminal, install `dj_database_url` and `psycopg2-binary`.

4. Freeze all app requirements to and create a requirements.txt file. This tells Heroku which requirements to use for deployment.

    - `pip3 freeze > requirements.txt`

5. To set up the new Postgres database, `import dj_database_url` in the project level settings.py file and set the new database default to the Heroku database config variable. Once in place, run migrations.

6. Once the migration has occurred, revert the default database setting to the original and set up a conditional so that if the DATABASE_URL exists in the Heroku environment, use Postgres, otherwise, use local database.

7. Install `gunicorn` as project web server and freeze to requirements.txt.

8. Create the Heroku Procfile (`touch Procfile`) which will run gunicorn as server for the app.

    - `web: gunicorn <app_name>.wsgi:application`

9. Log into Heroku in the terminal (`heroku login -i`), and disable the app's collect static so that Heroku will not collect the static files.

    - `heroku config:set DISABLE_COLLECTSTATIC=1 --app <app_name>`

10. Add `<app_name>.herokuapp.com` to ALLOWED_HOSTS in settings.py.

11. Finally, set the git remote and push the repository to deploy to Heroku:

    - `heroku git:remote -a <app_name>`
    - `git push heroku master`

### Deploying Locally

1. 

***

## Technologies Used

* [Github](https://www.github.com/) - Used for hosting and version control.
* [GitPod](https://www.gitpod.io/) - Online code editor.

***

## Credits

### Content

- https://www.get-youtube-thumbnail.com/

### Media:

- 

### Code

- https://www.ordinarycoders.com/blog/article/django-stripe-monthly-subscription

### Acknowledgements

