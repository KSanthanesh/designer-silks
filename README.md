# DESIGNER SILKS
<img src="static/images/desktop-1.PNG" align="left" width="300" height="200">
<img src="static/images/desktop-2.PNG" align="center" width="300" height="200">

Types of Content
- [Introduction](#introduction)
    - [Home](#home)
    - [Sarees](#sarees)
        - [Chiffon-Sarees](#chiffon-sarees)
        - [Cotton-Sarees](#cotton-sarees)
        - [Silk-Sarees](#silk-sarees)
        - [All-Sarees](#all-sarees)
    - [All-Products](#all-products)
        - [By-Price](#by-price)
        - [By-Rating](#by-rating)
        - [By-Category](#by-category)
        - [All-Products](#all-products)
    - [About-Us](#about-us)
    - [Search-bar](#search-bar)
    - [My-Account](#my-account)
        - [Register](#register)
        - [Login](#login)
        - [Logout](#logout)
        - [Product-Management](#product-management)
        - [My-Profile](#my-profile)
        - [My-Orders](#my-orders)
        - [Wishlist](#wishlist)
    - [Cart](#cart)
    - [CheckOut](#checkout)
    - [Checkout-Success](#checkout-success)

- [Strategy](#strategy)
    - [UX](#ux)
    - [Business-Vision](#business-vision)
    - [Purpose of Website](#purpose-of-website)
- [Skeleton](#skeleton)
- [Scope](#scope "Goto Scope")
   - [Features](#features)
   - [Future Features](#future-features)
- [Structure](#structure "Goto Structure")
  - [Wireframes](#wireframes)
  - [Database Schema](#database-schema)
  - [Colours](#colours)
  - [Typography](#typography)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Automation Testing](#automation-testing)
  - [Code Validation](#code-validation)
  - [Features Testing](#features-testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Acknowledgement](#acknowledgement)





## Introduction
- This project will cover Saree collections, which is one of the Indian Traditional Culture. 
- This webpage is categorised into Four main sections,such as Home, Sarees, All Products and Contact. In other two additional navigations available in the header, Which are My account and Cart.
- When the User choose Sarees Navigation option dropdown menu appears and shows four options to choose, such as Chiffon Sarees, Cotton Sarees, Silk Sarees and All Sarees.
- When the User choose All Products Navigation option, dropdown menu appears and shows four options to choose, such as By Price, By Rating, By Category and All Products.
- Finally Thanks message is displayed after submitting the Enquiry Contact form.
- when the User Choose My account Navigation option, dropdown menu appears and show Two options, such as Register and Login.
- Once the User Login in to  My Account option then the dropdown menu change to four different Categories, Such as My Profile, My Orders, My Wishlist and Logout.
- If the User is admin then an additional option is available which is Product Management. The Product Management option will allow the following options such as add the product, edit the product and delete the product.
- When the User Checkout from the Cart, it will move to Checkout Page. Success Message will appear Once the payment will be successfully completed.

<!-- - Success checkout message will appear in completion of the purchase Process. -->
- The website covers all the screen types, such as Pc,Laptop,Tablet and Mobile.

### Home
The Home Page covers the foloowing sections:
- Header, Navigation Menus and Shipping details.
- Hero Image
- Shop Now button is available in the main page. Clicking this button move the user to All Products Page.
- The Following options are availabele in the Footer:
  - Contact Details
  - 
  -
- Header and Footer will appear in all pages through Navigations. 


### Sarees
- When the User choose Sarees Navigation option dropdown menu appears and shows four options to choose, such as:
#### Chiffon Sarees
#### Cotton Sarees
#### Silk Sarees
#### All Sarees
- Total number of Sarees available in each Sarees category is displayed for the User.
- Sorting Options are available for the User in each Sarees Category, Such as
  - Price (low to high) and Price (high to low)
  - Rating (low to high) and Rating (high to low)
  - Name (A-Z) and Name (Z-A)
  - Category (A-Z) and Category (Z-A)




### All Products
- When the User choose All Products option dropdown menu appears and shows four options to choose, such as 
#### By Price
#### By Rating
#### By Category
#### All Products
- Total number of Sarees available in each Sarees category is displayed for the User.
- Sorting Options are available for the User in each Sarees Category, Such as
  - Price (low to high) and Price (high to low)
  - Rating (low to high) and Rating (high to low)
  - Name (A-Z) and Name (Z-A)
  - Category (A-Z) and Category (Z-A)
-

### Contact
- In the Contact form option, the user has to fillup all the parameters in the form. 
- There is a Newsletter option where the user has a choice to subscribe or not to subscribe the newsletter.

### Search bar
- The Search bar will help the user to narrow down the relevant products and display the products as per search description.

### My Account
- when the User Choose My account Navigation option, dropdown menu appears and show Two options, such as Register and Login.
- Once the User Login in to  My Account option then the dropdown menu change to four different Categories, Such as My Profile, My Orders, My Wishlist and Logout.
- If the User is admin then an additional option is available which is Product Management. The Product Management option will allow the following options such as add the product, edit the product and delete the product.
#### Register
- The User can use the Register option to fillup his information to register.<br>
Registration page contains:
    - Header and Footer
    - Email
    - Email confirmation
    - Username (It is not case sensitive)
    - Password (It is not case sensitive)
    - Confirm password
    - Back to Login button
    - Signup button
  After Registration mail send for confirmation message, and confirmation email send their email address to confirm for registration.
#### Login
- Only Registered User is able to use login option to login in to the website.<br>
Login Page contains:
    - Header and Footer
    - Username
    - Password
    - Remember me with checkbox
    - Home Button
    - Sign in button
    - Forget Password?

After Login the success login message will appear on the rightside of the Page.

#### Logout
- The User should logout from the website after using the website.<br>
Logout Page Contains:
    - Header and Footer
    - Cancel button
    - Sign out button
After Logout the success logout message will appear on the rightside of the Page.
    

#### Product Management
- The Product Management option will allow the following options such as add the product, edit the product and delete the product for the admin. 
#### My Profile
- Login user can update or store their Delivery information.
#### My Orders
- Order history and information about the products will be stored in the database.
#### Wishlist
- user can add favourite items into the wishlist and shortlist what to buy later.

### Product Details
- Product Details options contains: SKU (Product id),Fabric (Material Type), Description,length, Shipping and Returns.
- Quantity option is available for User to select the number of products of the same product.
- The cart will be update the section.

### Cart
- Shopping Cart page contains: 



### Checkout

### Checkout Success

## Strategy
### UX

#### UserStory using Kanban feature in Agile Methodology
  These are the steps for UX<br>
1. Click Projects in the dosa palace repositary and Create a Project name.
2. Then select, Project Template => Basic Kanban => create Project.
3. In the ToDo column, there will be three cards, delete those cards.
4. In the Todo column click three dots, then click =>  manage automation => click newly added box => update automation.
5. Then click => issues => new issues => Get started.
6. Then start to write Title and UX.<br>

    - As a Site User I can view the service options available in the Designer Silks Home page so that I can select the service that is required.
    - As a Site User I can view a paginated Navbar so that easily view that page.
    - As a Site User I can View all the Sarees in the product page So that I know how many collections are there in the website.
     - As a Site User I can Click the Saree image So that I can View the details of the product.
     - As a Site User I can write and read a Review So that I should know about the product.
    - As a Site user I can view the product by price, rating, name and category so that I can easily find the products.
    - As a Shopper or User I can View a specific category of product So that I can quickly find the products by Category.
    - As a User or Shopper I can Search the name of the product So that I can easily find the product what I want.
    - As a Site User I can Register for an account So that I can Have a personal account and can able to view my Profile.
    - As a Site User I can Easily Login my account So that I can Access my personnal account information.
    - As a Site User I can Easily Logout so that I can Logout safely from the website.
    - As a Site Owner I can Edit or Update the Product details So that I can Change Products details such as name,price,description, images or any discount available of the Product.
    - As a Shop Owner I can Add a Product So that I can Add new products in the website.
    - As a Site Owner I can Delete a Product So that I can Delete the Product if there is not available.
    - As a Site User I can have my personal profile So that I can view my personal details, order details, order confirmation and Payment information.
    - As a Site User I can Receive a email confirmation from the shopper after checkout So that I can Confirm the product quantity and payment is done correctly.
    - As a Site User I can Adjust or Remove the product in the cart So that I can easily changes in my purchases before checkout page.
    - As a Site User or Shopper I can view my cart to be purchased So that I can view total cost and qunatity of my purchase.
    - As a Site user I can view the shopping cart So that I can view the item ordered in the cart.
    - As a Site User I can easily select quantity of a product So that I can decide how many quantity to buy.
    - As a Site User I can view on order confirmation So that I can view what purchase i made.
    - As a Site User I can easily enter my payment option So that there is no issues in the payment process.
    - As a Site User I can provide my personal and payment details are safe and secure So that I can trust the purchase Site.
    - As a User I can write a Review about the product So that It will help for others.
    - As a Site User I can add favourite Products in to the Wishlist So that I can decide what to buy during the purchase.
    - As a Site User I can Delete the products from the wishlist So that I can shortlist what to buy.
    - As a Site User I can use Contact form to send enquiry So that I can enquire information regarding products and services.
    - As a Site User I can subscribe option for Newsletter So that I can get the information regarding the products regularly.
    
    
### Business Vision
### Purpose of Website

## Skeleton
There are approximately 34 products and 3 categories in the designer silks website.
## Scope
### Features
- A page with an overview of all the products which can be sort by name, rating, price and category
- A contact form where customers can ask questions.
- Newsletter subscription for Further details.
- Social Media page for New updates.
- A Registration Page
- Login Page
- A page for when the customer forgot their password
- Logout page for after using the website
- viewing the order history page
- viewing the wishlist page
- A profile page to adjust the user's details.
- An order sytem, to order the products
- Secure Stripe Payment
- Review the about the products.
- Shipping estimation days and Return policy
- privacy policy

### Future Features

## Structure
The site will be structured as clear as possible, with a logic workflow and it should be easy to navigate the site on all screen sizes.
### Wireframes
Balsamiq Wireframes used for this website.
<details>
<summary>Home</summary>
<img src="static/wireframes/home-page.png" width="500">
</details>
<details>
<summary>Cotton Sarees</summary>
<img src="static/wireframes/cotton_sarees.png" width="500">
</details>
<details>
<summary>Silk Sarees</summary>
<img src="static/wireframes/silk_sarees.png" width="500">
</details>
<details>
<summary>Saree Details</summary>
<img src="static/wireframes/product_detail.png" width="500">
</details>
<details>
<summary>Shopping Cart</summary>
<img src="static/wireframes/cart.png" width="500">
</details>
<details>
<summary>Checkout</summary>
<img src="static/wireframes/checkout.png" width="500">
</details>
<details>
<summary>Checkout Success Message</summary>
<img src="static/wireframes/checkout_success.png" width="500">
</details>
<details>
<summary>Product Management</summary>
<img src="static/wireframes/product_management.png" width="500">
</details>
<details>
<summary>Register</summary>
<img src="static/wireframes/register.png" width="500">
</details>
<details>
<summary>Login</summary>
<img src="static/wireframes/login.png" width="500">
</details>
<details>
<summary>Logout</summary>
<img src="static/wireframes/logout.png" width="500">
</details>
<details>
<summary>My Profiles</summary>
<img src="static/wireframes/user_profile.png" width="500">
</details>
<details>
<summary>My Orders</summary>
<img src="static/wireframes/my_orders.png" width="500">
</details>
<details>
<summary>My Wishlists</summary>
<img src="static/wireframes/my_wishlist.png" width="500">
</details>
<details>
<summary>Contact Page</summary>
<img src="static/wireframes/contact.png" width="500">
</details>

### Database Schema
### Colours
I have used warm light and dark colours to create pleasant experience for those people to viewing this website. Bootstrap colour also used for this website.
colours used:
 - Bootstrap bg and text colours used throughout the project.
 - #000
 - #fff 
 - #222 
 - rgb(235, 29, 63)
 - #aab7c4
 - rgb(24, 136, 241)
 - #dc3545
 - rgb(208, 225, 247)
 - rgb(161, 204, 248)
 - rgb(170, 183, 196)
 - rgb(173, 227, 245)





### Typography
I have used Open Sans, cursive and 'Raleway', sans-serif to create this website.

## Technologies Used

### Libraries & Frameworks
- Django Web Application Framework
- Bootstrap - for responsive website
- Font Awesome - icons used throughout the site. Responsive design - To generate the mockup image.
- Google font -used for the website looks more beautiful,fast and great typography.
- stripe -for payment
- 

#### Tools
- Gitpod - is an open source platform for automated and ready-to-code.
- Github - to save the project code and host the live project.
- Python Tutor - to check how the Java Script code behaves in each line.
- Dev tools -For inspecting and editing the web code.
- Heroku - To Deploy the Project.
- allauth - for site user Signup, login and logout of account.
- Cloudinary - To save images from admin page.
- favicon - https://www.favicon-generator.org/ -Favicon icon created using this website.
- Am I responsive - to check  the responsive pages.
- Balsamiq - to create wireframes.
- dbdiagram.io - to create database schema
- Random Secret Key Generator - https://miniwebtool.com/django-secret-key-generator/
## Testing
### Automation Testing
### Code Validation
### Features Testing

## Bugs

## Deployment
First we need to go to github website to create a new repositary using code Institute Template. Followed by giving a new name of the website.Then need to click the create repositary button. After click the button it will bring us to go to another page, which contains the green button labelled as Gitpod.Click the Gitpod button will bring us to the Gitpod Workspace for coding screen.

### gitpod
  Used Gitpod Workspace for coding. To preview the browser window need to type <b>python3 manage.py runserver</b> in the terminal window at the bottom.Afterthat, have to do git add for add files or remove files and do git commit for reasoning and do the git push for git hub repositary website.
### Procedure for Deployment

  1. Install the Django and gunicorn in the terminal => pip3 install django gunicorn (Gunicon is the server that we're going to use to run Django on Heroku.)<br>
    next install supporting libraries:
  2. Then Install ==> pip3 install dj_database_url psycopg2
  3. Create Requirement.txt file in the terminal.<br>
       ==> pip3 freeze --local > requirements.txt
  4. Create a new project name:<br>
    ==>django-admin startproject designer_silks .<br>
  5. Create a new app name:<br>
    ==> python3 manage.py startapp home
    ==> python3 manage.py startapp product
    ==> python3 manage.py startapp cart
    ==>python3 manage.py startapp checkout
    ==> python3 manage.py startapp profile
    ==> python3 manage.py startapp contact

    Then enter the app name("home","product", "cart", "checout", "profile", "contact") in to the INSTALLED_APPS in settings.py
  Set up your database by running the following command in your terminal:<br>
    ==> python3 manage.py makemigrations<br>
    ==> python3 manage.py migrate<br>
    Then run the server:<br>
    python3 manage.py runserver (we can see the installation work successfully in the browser).<br>
    6. Now create a superuser to get access to the Django admin, use the following command:<br>
     ==>python3 manage.py createsuperuser.<br>
  7. Allauth Setup<br>
     Install ==> pip3 install django-allauth==0.41.0<br>
    Add the allauth folder in to root templates.<br>
  8. mkdir static folder (for css,js and image files)<br>
       mkdir media folder (for products images)<br>
  9. Now we need to add the required fixtures data into the database in the following order by using the following commands:<br>
      ==> python3 manage.py loaddata categories<br>
      ==> python3 manage.py loaddata products.<br>

#### Heroku

    1. Create new app name and select europe.
    Then Click => Resources Tab => Addons enter=> Postgres, then select => Heroku postgres => Hobby dev.
    Then select the settings tab, click Reveal Config Vars and then copy the Database Value.
    2. And Add some more key values in the Heroku settings

      - SECRET_KEY	          -your_SECRET_KEY
      - STRIPE_PUBLIC_KEY	    -your_STRIPE_PUBLIC_KEY
      - STRIPE_SECRET_KEY	    -your_STRIPE_SECRET_KEY
      - AWS_ACCESS_KEY_ID     -from AWS
      - AWS_SECRET_ACCESS_KEY -from AWS
      - EMAIL_HOST_PASS       -from Gmail
      - EMAIL_HOST_USER       -Gmail
      - SECRET_KEY            -Random Key Generator
      - USE_AWS
#### In the Terminal








## Acknowledgement

