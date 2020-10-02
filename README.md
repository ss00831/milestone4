# Lapland in Sweden

## The site address: https://lapland-in-sweden.herokuapp.com/

Sweden has various cultures by county. Currently, I live in Kiruna, the north part (Norrbotten county). Many hikers visit the county for climbing and many tourists who want to see the Northern Lights in the winter or enjoy winter activities. On the one hand, Kiruna is also a city famous for mining, so you can also take a guided tour of the mines.

I want to introduce you to the activities you can do in the area through several tour products, while also selling tour products to help tourists travel efficiently.

## UX

### Preview
![Web-Showcase-Project-Presentation](https://user-images.githubusercontent.com/53374745/92158705-9b517500-ee2c-11ea-9d26-575c4ea2f3d1.png)

### User Scenario

![userstories](https://user-images.githubusercontent.com/53374745/91954225-cf7c4700-ed01-11ea-8619-808d1bede4a9.JPG)

### Wireframes

- Desktop: [ms4-desktop.pdf](https://github.com/ss00831/milestone4/files/5170012/ms4-desktop.pdf)
- Tablet: [ms4-tablet.pdf](https://github.com/ss00831/milestone4/files/5170011/ms4-tablet.pdf)
- Mobile: [ms4-mobile.pdf](https://github.com/ss00831/milestone4/files/5170010/ms4-mobile.pdf)


## Features

### Existing Features
1. templates app
- Show menu
- Feature of search (with search box)
- Toast messages: Show a message depend on a situation
2. home app: show index page (index.html) 
3. tourprograms app
- tourprograms.html
    - Show tour programs list: All tour programs / By category 
    - Sort tour programs by price/rating/name/category and A-Z/Z-A
- tourprogram_detail.html
    - Detail of tour program: Show the tour information and has the select date and number of people form
4. cart app: Save the selected items (cart.html)
5. checkout app: Feature of payment (checkout.html & checkout_success.html)
6. profiles app (profile.html)
- Save the registered user information
- Show the booking history
7. contact app: Send a mail to the site owner (contact.html & contact_success.html)


### Features Left to Implement
1. tourprograms app - tourprogram_detail.html: Make the number of child input box
2. Feature of real time chatting

## Information Architecture

### Menu structure
1. All tours 
- By Price
- By Season
- By Region
- By rating
- All Tours

2. Summer tours 
- Tracking
- Attraction
- Sightseeing
- All Summer Tours

3. Summer tours 
- Aurora Tour
- Attraction
- Sightseeing
- With Wild Animal
- All Winter Tours

4. Special Offer
- wilderness Meal

5. Contact us - Message form - Message success page

6. My Account
- Admin mode (Only for admin user)
- My profile: Profile form / Booking history
- Login / Logout

7. Cart - Your cart - Checkour page - Checkout success page

### Database
1. categories

| Field Name    | data type |
|---------------|-----------|
| pk            | Char      |
| model         | Char      |
| name          | Char      |
| friendly_name | Char      |

2. tourprograms

| Field Name      | data type  |
|-----------------|------------|
| pk              | CharField  |
| model           | CharField  |
| category        | ForeignKey |
| name            | CharField  |
| sku             | CharField  |
| region          | CharField  |
| maximum         | IntegerField|
| date            | CharField  |
| priceadult      | IntegerField|
| pricechild      | IntegerField|
| departure_data  | CharField  |
| estimated_times | CharField   |
| description     | TextField  |
| rating          | DecimalField|
| included        | CharField  |
| not_included    | CharField  |
| meeting_place   | CharField  |
| note            | TextField  |
| image_url       | URLField   |
| image           | ImageField |

## Technologies Used

### Language

- HTML5
- CSS3
- JavaScript
- Python 3.8.3

### Tools & Libraries

- Gitpod (https://www.gitpod.io/): To develop and write code
- Github (https://github.com/)
- Heroku (https://www.heroku.com/): For deployment
- Amazon AWS (https://aws.amazon.com/?nc1=h_ls): To store contents (images and json) and static files (css)
- Django 3.1 (https://www.djangoproject.com/)
- JQuery 3.5.1 (https://jquery.com)
- Bootstrap 4.5.2 (https://getbootstrap.com/)
- Fontawesome 5.14.0 (https://fontawesome.com/)
- Google font (https://fonts.google.com/)
- Stripe (https://stripe.com/)
- Boto3 (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- Responsive Web Design Showcase Mockup (https://www.mockupworld.co/free/responsive-web-design-showcase-mockup/)

## Testing
0. Device / Browser spec
- For Usability testing

|              |            Device 1            |               Device 2               |     Device 3     |                 Device 4                 |         Device 5        |
|:------------:|:------------------------------:|:------------------------------------:|:----------------:|:----------------------------------------:|:-----------------------:|
| Device Model |         Macbook Air 13"        |           Samsung NT900X5W           |   iPhone XS Max  |                iPad Air 2                |    LG V30S (LG-H930)    |
|      OS      |     macOS Catalina 10.15.6     |      Windows 10 Home 10.0.19041      |    iOS 13.6.1    |                iOS 13.6.1                |        Android 9        |
|      CPU     | Intel core i5 1.6GHz Dual-Core | Intel core i5-7200 2.50GHz Dual core | Apple A12 Bionic | 1.5GHz tri-core 64-bit ARMv8-A "Typhoon" | Qualcomm Snapdragon 835 |
|      RAM     |               4GB              |                  8GB                 |        4GB       |                    2GB                   |           6GB           |
|    Graphic   |     Intel HD Graphics 6000     |         Intel HD Graphics 620        |    APPLE G11P    |              PowerVR GXA6850             |   Qualcomm Adreno 540   |
|    Browser   |   Safari 13.1.2 (15609.3.5.1.3)|          Chrome 85.0.4183.83         |      Safari      |                  Safari                  |   Chrome 85.0.4183.81   |


### Code validation
- html (https://validator.w3.org/): No error, mainly javascript warnings
- CSS (https://jigsaw.w3.org/css-validator/, Validate by direct input)
    - base.css: No error
    - checkout.css: No error
    - profile.css: No error
- JS (https://jshint.com/) 
    - stripe_elements.js: 3 warnings
    - countryfield.js: 2 warnings
    - people_input_script.html: 5 warnings
- Python 
    1. python3 -m flake
    - Common Errors
        1. DJ01 Avoid using null=True on string-based fields such CharField
        1. F401 'xxxxxx' imported but unused
        1. F841 local variable 'e' is assigned to but never used: checkout\webhook.py
        1. E501 line too long (92 > 79 characters): checkout\views.py
        1. E501 line too long - AUTH_PASSWORD_VALIDATORS: lapland_in_sweden\settings.py
    2. http://pep8online.com/: 1 error - checkout\views.py, 4 error (AUTH_PASSWORD_VALIDATORS) - lapland_in_sweden\settings.py

### Manual Testing

#### Manual testing test sheet & the result: [rev08_testcases_20200927.xlsx](https://github.com/ss00831/milestone4/files/5288878/rev08_testcases_20200927.xlsx)

1. Usability Test
- All functional test cases (91 items): All pass
- All input data cases (53 items) + card number test (36 cases): All pass
- All authenticated status test cases (9 items): All pass

2. Responsive and browser test

- Responsive test

| Browser\Resolution | >= 992 px | >= 768 px (Tablet size) | >= 576 px | >= 414 px (iPhone Plus) |>= 320 px (iPhone 5/SE)|
|:-------:|:-------:|:-----------------:|:--:|:--: |:--: |
| Safari        | Pass       |  Pass    | Pass   | Pass | Pass |
| Chrome        | Pass       |  Pass    | Pass   | Pass | Pass |
| Firefox       | Pass       |  Pass    | Pass   | Pass | Pass |
| Internet Explorer   | Pass       |  Pass    | Pass   | Pass | Pass |
| Edge          | Pass       |  Pass    | Pass   | Pass | Pass |

- IE warning message window test

| Browser\Test Item | Alert? | Expect result | Warning box? | Expect result |Result|
|:-------:|:-------:|:-----------------:|:--:|:--: |:--: |
| Safari        | No       |  No    | No   | No | Pass |
| Chrome        | No       |  No    | No   | No | Pass |
| Firefox       | No       |  No    | No   | No | Pass |
| Internet Explorer   | Yes       |  Yes    | Yes   | Yes | Pass |
| Edge          | No       |  No    | No   | No | Pass |

3. The detailed result : Please refer the test sheet as below.

[rev08_testcases_20200927.xlsx](https://github.com/ss00831/milestone4/files/5288878/rev08_testcases_20200927.xlsx)

4. Bugs
- Internet Explorer 11
    - Not able to select a date in tourprogram_detail.html
    - Not able to input card number and if I don't input any card number and just click complete order, the order is succeeded.
  +) Added notice about IE 11: We don't support IE fully. (09/18/2020 - fixed)

### Testing history
1. 09/04/2020: Created the test cases for functional, responsive & browser testing and Functional Test
1. 09/05/2020: Usability Test
1. 09/06/2020: Card number test - 36 cases
1. 09/12/2020: Bug testing
1. 09/13/2020: Full testing
1. 09/18/2020: Bug testing
1. 09/24/2020: Internet Explorer testing
1. 09/27/2020: Full testing

### Automated Testing
- I used TestCase(a suite in Django), and I created test_models.py, test_forms.py and test_views.py.
* If you want to run the test codes, you need to turn on debug mode and test server.
1. Run the tests
```
python3 manage.py test
```

2. Check the coverage report
```
coverage report
```


## deployment

#### My Milestone4 page address: https://lapland-in-sweden.herokuapp.com/

#### GitHub repository (https://github.com/ss00831/milestone4) :

### Heroku deployment
1. Create "requirements.txt" file
```
pip3 freeze > requirements.txt
```
2. Create "Procfile" file
```
web: gunicorn lapland_in_sweden.wsgi:application
```
3. Login heroku
4. Setting Config Vars : Heroku homepage - Select "lapland-in-sweden" project - Setting - Click "Reveal Config Vars" - Create Config Vars as below and save
![setting_heroku](https://user-images.githubusercontent.com/53374745/92122129-5fea8280-edfb-11ea-8942-1d732091678c.JPG)
 1) AWS_ACCESS_KEYID, AWS_SECRET_ACCESS_KEY: You can get a csv file which includes the key information when you create staticfiles-user. Find the keys and copy and paste on the fields.
 2) DATABASE_URL
 - The value will be created when you create a new Postgres database.
 3) EMAIL_HOST_PASS 
 - You can get the value in app password generator in Gmail. The value is 16 character.
 4) EMAIL_HOST_USER
 - Your gmail address
 5) SECRET_KEY 
 - Go to https://miniwebtool.com/django-secret-key-generator/ and click "Generate Django Secret Key"
 - The generated Django Secret Key length is 50 character. Use this value.
 6) STRIPE_PUBLIC_KEY 
 - Go to Stripe.com and login -> Dashboard -> Developers -> API Keys -> Copy "Publishable key"
 7) STRIPE_SECRET_KEY 
 - Go to Stripe.com and login -> Dashboard -> Developers -> API Keys -> Copy "Secret key"
 8) STRIPE_WH_SECRET 
 - Go to Stripe.com and login -> Dashboard -> Developers -> Webhook -> Click URL -> Copy "Signing secret"

5. Type commands as below for git add / commit / git push
```
git add
```
```
git commit -m "commit message" 
```
```
git push
```
6. Type commands as below for git remote 
```
git remote add heroku https://git.heroku.com/lapland-in-sweden
```
```
git push -u heroku master
```
```
git remote -v
```

7. Run the webpage
- Click "Open app" button on the Heroku dashboard page or write https://lapland-in-sweden.herokuapp.com/ on your web browser.

#### AWS Amazon: Store static files and media files. 

### How to run this project locally

To clone this project from GitHub :
1. Click [Code] - [Download ZIP] on the repository page.
2. Unzip the milestone4-master.zip file.
3. Open milestone4-master - milestone4-master - lapland_in_sweden - setting.py: Open with Notepad program or any other code edit program
4. Added this code as below.
```
import os
import dj_database_url

# Type this code (2 lines) under "import dj_database_url"
if os.path.exists('env.py'):
    import env
```
5. Open Git Bash on your local IDE.
6. (Optional) Change the current working directory to the location where you want the cloned directory to be made.
7. Move to the milestone3-master folder
8. Install the requirement files as below.
```
pip3 install -r requirements.txt
```
* If you need, update pip.
```
python -m pip install --upgrade pip
```
9. Make "env.py" file and write as below in the file.
```
import os

os.environ["AWS_ACCESS_KEYID"] = "YOUR VALUE"
os.environ["AWS_SECRET_ACCESS_KEY"] = "YOUR VALUE"
os.environ["DATABASE_URL"] = "YOUR VALUE"
os.environ["EMAIL_HOST_PASS"] = "YOUR VALUE"
os.environ["EMAIL_HOST_USER"] = "YOUR VALUE"
os.environ["SECRET_KEY"] = "YOUR VALUE"
os.environ["STRIPE_PUBLIC_KEY"] = "YOUR VALUE"
os.environ["STRIPE_SECRET_KEY"] = "YOUR VALUE"
os.environ["STRIPE_WH_SECRET"] = "YOUR VALUE"
os.environ["USE_AWS"] = "True"
```
10. Add "env.py" in .gitignore file.
11. Migrate models into database.
```
python manage.py migrate
```
12. Create a superuser
```
python manage.py createsuperuser
```
13. Run the server
```
python manage.py runserver
```

## Credits

### Contents & Media
1. Main index image: https://pixabay.com/photos/northern-lights-sweden-lapland-225454/
2. Tour programs images and contents
- Summer
    1. Tracking
    -https://www.kirunalapland.se/en/see-do/hiking-with-guide-in-north/
    -https://www.kirunalapland.se/en/see-do/nature-guide-feel-good-hike/
    2. Attraction
    - https://www.kirunalapland.se/en/see-do/midnight-sun-tour-horse/
    - https://www.kirunalapland.se/en/see-do/sleddog-kennel-visit-and-short-cart-ride/
    3. Sightseeing
    -https://www.kirunalapland.se/en/see-do/entrance-to-icehotel-with-guided-tour/
    -https://www.kirunalapland.se/en/see-do/a-city-in-motion-the-guided-tour/
- Winter
    1. Aurora tour
    -https://www.kirunalapland.se/en/see-do/nightly-aurora-photo-tour-in-abisko-national-park/
    -https://www.kirunalapland.se/en/see-do/guovssahasat-reindeer-northern-lights/
    2. Attraction
    -https://www.kirunalapland.se/en/see-do/high-mountain-overnight-tour-with-snowmobile/
    -https://www.kirunalapland.se/en/see-do/ski-school-at-luossavaara-ski-hill/
    3. Sightseeing
    - https://www.kirunalapland.se/en/see-do/guided-tour-icehotel-jukkasjarvi/
    - https://www.kirunalapland.se/en/see-do/using-the-five-senses-to-experience-sami-life/
- WILD animal
    -https://www.kirunalapland.se/en/see-do/wake-up-husky-tour/
    -https://www.kirunalapland.se/en/see-do/ecotours-wilderness-tour/
    -https://www.kirunalapland.se/en/see-do/raidu-encounter-with-reindeer/
- Meal
    - https://www.kirunalapland.se/en/see-do/traditional-sami-cooking/
    - https://www.kirunalapland.se/en/see-do/dog-team-tour-with-coffee-or-lunch/
    - https://www.kirunalapland.se/en/see-do/a-taste-of-swedish-lapland/


### Acknowledgements

* Inspiration: https://www.kirunalapland.se/en/

1. Code Institute: Boutique Ado project video was helpful for this project.
2. Slack community: I have found many solutions.
3. Django Admin Url : https://stackoverflow.com/questions/44130643/django-admin-urls
4. Sending email : https://docs.djangoproject.com/en/3.1/topics/email/
5. ChoiceField – Django Forms : https://www.geeksforgeeks.org/choicefield-django-forms/
6. Django form always shows error “This field is required”: https://stackoverflow.com/questions/5806059/django-form-always-shows-error-this-field-is-required
7. How to keep your footer where it belongs?: https://www.freecodecamp.org/news/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c/
8. Check if browser is Internet Explorer: https://jsfiddle.net/alvaroAV/svvz7tkn/ 
9. Stop to support Internet Explorer - Microsoft’s services will drop support for IE11 in a year: https://www.theverge.com/2020/8/17/21372487/microsoft-internet-explorer-11-support-end-365-legacy-edge