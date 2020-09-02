# Lapland in Sweden

## The site address: https://lapland-in-sweden.herokuapp.com/

The country where I live in Sweden has various cultures by county. Currently, I live in Kiruna, where is the north part (Norrbotten county), and many hikers visit the county for climbing and many tourists who want to see the Northern Lights in the winter or enjoy winter activities. On the one hand, Kiruna is also a city famous for mining, so you can also take a guided tour of the mines.

I want to introduce you to the activities you can do in the area through several tour products, while also selling tour products that will help tourists travel efficiently.

## UX

### Preview
- Desktop

- Tablet

- Mobile

### User Scenario

![userstories](https://user-images.githubusercontent.com/53374745/91954225-cf7c4700-ed01-11ea-8619-808d1bede4a9.JPG)

### Wireframes


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
1. category

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


## Testing

### Manual Testing

### Testing history

## deployment

### My Milestone4 page address: https://lapland-in-sweden.herokuapp.com/

### To deploy this page to GitHub Pages from its GitHub repository (https://github.com/ss00831/milestone4) :

### How to run this project locally

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
1. Code Institute: Boutique Ado project video was helpful for this project.
2. Slack community: I can find many solutions.
3. Django Admin Url : https://stackoverflow.com/questions/44130643/django-admin-urls
4. Sending email : https://docs.djangoproject.com/en/3.1/topics/email/
5. ChoiceField – Django Forms : https://www.geeksforgeeks.org/choicefield-django-forms/
6. Django form always shows error “This field is required”: https://stackoverflow.com/questions/5806059/django-form-always-shows-error-this-field-is-required