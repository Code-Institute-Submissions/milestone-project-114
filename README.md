# Deathfret Guitar

## Milestone Project 4 - Full Stack Frameworks with Django

The final project as part of [Code Institute](https://codeinstitute.net)'s full stack software development course ties together all aspects of full stack developemnt
in one comprehensive application. Using the Django full stack framework, the goal is to create an online service app that will be able to handle user authenticaation as well
as a payment system for a product and/or service.

As a guitarist with over 20 years experience playing, recording and touring, I have always dreamt of creating a community of up and coming players, in which the more prevalant
who have anything to teach will be able to do so for a subscribing user. Specifically I have been a part of the extreme metal niche of the industry for many years and have observed a gap in this market, and that such a platform does not currently exist for this particular genre.

The django app will be a subscription based site, where a member will be able to access lessons and masterclasses of talented guitarists for a small monthly, or yearly fee. The idea will be
for the site owner(s) to source players who would be willing to write and record a lesson series, which will then be available for paying members in their very own members area. At the time of writing however, this collaborative content has not yet been created, so while the project is being built, only example lesson plans by sourced (Youtube, with permission) players will be used. The structure of the site will however, remain the same.

The site will also feature a webstore of branded merchandise that a subscribing user or anaonymous shopper will be able to purchase. An extra incentive for subscribership is a subscriber's 10% discount to be used on all branded merchandise.

![DeathfretResponsive](static/deathfret-responsive.png "DeathfretResponsive")

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

As part of the Full Stack Developer course directed by [Code Institute](https://codeinstitute.net/), this project was designed to fulfill the scope of creating an ecommerce or SaaS app using the [Django](https://www.djangoproject.com/) full stack framework.

The goal is to create not only a site where users can access to valuable lesson series' offered by the talents of the music scene, but eventually to create a community of like-minded players who share a passion to share and devlop ideas artistically. The demographic is open to any guitarist who is interested in learning from the featured artists, but those specifically who are fans of the genre or are interested in learning from it.

The long term goal is to take this project beyond the scope of the course, and after completion, to launch this as my first online business.

### Developer Goals

As a developer, the main goal is to build a subscription model based on a signup and paid for tier of subscription. The paid tier will be divided into monthly or yearly payments. If the user opts for the yearly payment option, this will work out cheaper for them annually, rather than paying on a monthly basis.

The side goal for this project is to strengthen the knowledge of creating an eccommerce store and the system of one off payments for goods using [Stripe](https://stripe.com/gb).

Both will strengthen knowledge and skills of the Django framework, and provide the development of advanced JavaScript and Python functionality.

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

The layout and navigation design elements of the site has been achieved using the Bootstrap design framework. As much consideration as possible has gone into the implementing the components and altering the styles of each to best suit the overall visual design.

The UX design of the site has been designed as a simple, and easy to use payment flow for both subscription and goods payments. The featured artist and lesson series have been presented to the user in an easy-to-follow style of use, where leassons are laid out in an interactive, self-explanatory way.

#### Frameworks

* [Django](https://www.djangoproject.com/)
    - The Django framework has provided an excellent, intuitive framework to build this project upon. Offering the ability to easily create data models and to display the data back on the front-end with the use of Django's template tags.

* [Bootstrap 4.5.2](https://getbootstrap.com/)
    - Bootstrap has been chosen as the design framework over others, such as Materialize or Tailwind. Materialize was used in a previous project and resulted in some limitations with compatibility of other features that were implemented. To keep things simple, Bootstrap provided the ease of use and implememntation necessary for the scope of the project.

* [JQuery 3.5.1](https://jquery.com/)
    - Although JQuery has not been a major factor for the use of JavaScript logic in the project, it has played an important role in connecting the front-end interactivity to the back-end functionality. 

#### Colours Used

The colour scheme and brand logo have been designed to reflect the imagery and primary colours that are used throughout most of this genre's visual design work:
    - The logo as a 'band logo' style brand.
    - The use of black, red and white as primary colours observed throughout most extreme metal's visual design work.

Colours:

- ![#000000](https://placehold.it/15/000000/000000?text=+) `#000000 - black, base colour`
- ![#FFFFFF](https://placehold.it/15/FFFFFF/000000?text=+) `#FFFFFF - white, base colour`
- ![#DC3545](https://placehold.it/15/DC3545/000000?text=+) `#DC3545 - red (bootstrap 'danger'), primary colour`
- ![#6C757D](https://placehold.it/15/6C757D/000000?text=+) `#6C757D - dark grey (bootstrap 'secondary'), secondary colour`

#### Fonts

Many fonts have been experimented with in order to fit the design of the project, including Google Fonts' "Metal" - which ended up leaving an impression of "tackiness". A cleaner, lighter and smarter font has been chosen, in order to give the site an air of sophistication and professionalism despite the nature of the genre in which is is based.

![FontsExample](static/deathfret-fonts.png "Fonts")

Montserrat from [Google Fonts](https://fonts.google.com) has been chosen to reflect the design aesthetic.

#### Icons

[FontAwesome](https://fontawesome.com/) has been used to deliver the icons used throughout the project, as they are the more convenient option to implement alongside Bootstrap.

#### Wireframes

The initial wireframing design was created using [Balsamiq](https://balsamiq.cloud/).

High quality wireframes of the site can be found [here](deathfret-wireframe.pdf "Wireframes").

***

## Features

### Existing Features

#### 

* Subscription tier page with easy UX flow for taking card payments.

* Merch webstore with easy UK flow for taking card payments.

* User profile comtaining surrent subscription status, default delivery information and order history.

* Lesson sets laid out in a Bootstrap accordion.

### Features Left to Implement

* Instagram feed for local feature wall - something that was implemented during the project but made redundant due to the nature of instagrams API being changed.

* A news blog related to the community that will be built by app users.

* Downloadable course content (music sheets and backing tracks) in PDF and mp3 format.

***

## Testing

### 



### Responsiveness

Using boostrap simplified the responsiveness process thanks to the grid system and responsive based text classes. I have utilised this system with minimal use of media queries.

To test responsiveness, Google Chrome developer tools has been used to ensure the site works across all screeen sizes, from desktop computers down to mobile.

### Other Bugs and Problems

*  

***

## Validation

### HTML

* [HTMLValidator](https://validator.w3.org/)
    - All HTML passes through the validator without any problems. The only errors present are raised for the Django template tags:

![HtmlValidator](static/deathfret-guitar-html-validator.png "HTMLValidator")

### CSS

* [CSSValidator](https://jigsaw.w3.org/css-validator/)
    - All static CSS files pass through the validator with no errors.

### JS

* [JavaSciptValidator](https://esprima.org/demo/validate.html)
    - All static JS files pass through the validator with no errors.

### Python

* [PythonCodeChecker](https://extendsclass.com/python-tester.html)
    - All Python code passes through the code checker with no major errors. The only errors present here and on flake8 are things not worth changing, eg. line length.

### Compatibility

* To test the site based on different platforms, I used [Cross Browser Platforms](https://app.crossbrowsertesting.com/) to view the look and feel of the site on multiple platforms.
    - The site was tested throughout development using Google Chrome.
    - No other issues with emements appear present. Functionality works fine.

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

12. To complete deployment, connect the git repository to Heroku to allow git to push to Gitpod and Heroku simultaneously. Add new environment variables for SECRET_KEY and DEVELOPMENT and add those into settings.py.

### Deploying Locally

1. Ensure the following components are present:

    - [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
    - [pip](https://pip.pypa.io/en/stable/installing/)
    - [Python3](https://www.python.org/downloads/)
    - [Django](https://www.djangoproject.com/)

2. Download the .zip file from the repository in GitHub. The following command can also be used to clone the repository:

    - `git clone https://github.com/vdgvzr/milestone-project-4`

3. In the workspace environment, ensure that all Django config variables are set.

4. Install the project requirements from the requirements.txt file:

    - `pip3 install -r requirements.txt`

5. Run the manage.py file to run the server:

    - `pip3 manage.py runserver`

***

## Technologies Used

* [Github](https://www.github.com/) - Used for hosting and version control.
* [GitPod](https://www.gitpod.io/) - Online code editor.
* [Django](https://www.djangoproject.com/) - Web framework used.
* [Heroku](https://www.heroku.com/) - Used for app deployment.
* [HTML5](https://en.wikipedia.org/wiki/HTML5) - Used for the templates.
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - For adding styles to html elements.
* [Javascript](https://en.wikipedia.org/wiki/JavaScript) - Used to write functions for site interactivity.
* [Python](https://www.python.org/download/releases/3.0/) - Used for writing app functions and to communicate with mongoDB using pymongo.
* [JQuery](https://jquery.com/) - Ussed to access elements between languages.
* [Bootstrap4](https://getbootstrap.com/) - Design framework.
* [Balsamiq](https://www.balsamiq.com/) - Used for wireframe design.
* [HTMLValidator](https://validator.w3.org/) - For testing html code validity.
* [CSSValidator](https://jigsaw.w3.org/css-validator/) - For testing css code validity.
* [JavaScriptValidator](https://esprima.org/demo/validate.html) - For testing js code.
* [PythonCodeChecker](https://extendsclass.com/python-tester.html) - For testing python code.
* [Favicon](https://www.favicon-generator.org/) - For creating site favicon.
* [GoogleFonts](https://fonts.google.com/) - For providing fonts for the site.
* [AmIResponsive?](http://ami.responsivedesign.is/) - To test site responsiveness.
* [Stripe](https://stripe.com/gb) - To process payments.
* [YouTube](https://www.youtube.com) - For embedded lesson videos.
* [Instagram](https://www.instagram.com) - For embedded features. `(now redundant)`

***

## Credits

### Content

- https://www.get-youtube-thumbnail.com/

### Media:

- 

### Code

- https://www.ordinarycoders.com/blog/article/django-stripe-monthly-subscription

### Acknowledgements

