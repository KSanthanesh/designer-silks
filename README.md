# <span style="color:green;">DESIGNER SILKS</span>
<img src="static/images/desktop-1.PNG" align="left" width="300" height="200">
<img src="static/images/desktop-2.PNG" align="center" width="300" height="200">

### <span style="color:green;">Types of Content</span>
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
    - [Contact](#contact)
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
  - [Amazon Web Services](#amazon-web-services)
- [Acknowledgement](#acknowledgement)





## <span style="color:green;">Introduction</span>
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

### <span style="color:green;">Home</span>
The Home Page covers the foloowing sections:
- Header, Navigation Menus and Shipping details.
- Hero Image
- Shop Now button is available in the main page. Clicking this button move the user to All Products Page.
- The Following options are availabele in the Footer:
  - Contact Details
  - 
  -
- Header and Footer will appear in all pages through Navigations. 


### <span style="color:green;">Sarees</span>
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




### <span style="color:green;">All Products</span>
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

### <span style="color:green;">Contact</span>
- In the Contact form option, the user has to fillup all the parameters in the form. 
- There is a Newsletter option where the user has a choice to subscribe or not to subscribe the newsletter.

### <span style="color:green;">Search bar</span>
- The Search bar will help the user to narrow down the relevant products and display the products as per search description.

### <span style="color:green;">My Account</span>
- when the User Choose My account Navigation option, dropdown menu appears and show Two options, such as Register and Login.
- Once the User Login in to  My Account option then the dropdown menu change to four different Categories, Such as My Profile, My Orders, My Wishlist and Logout.
- If the User is admin then an additional option is available which is Product Management. The Product Management option will allow the following options such as add the product, edit the product and delete the product.
#### <span style="color:green;">Register</span>
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
#### <span style="color:green;">Login</span>
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

#### <span style="color:green;">Logout</span>
- The User should logout from the website after using the website.<br>
Logout Page Contains:
    - Header and Footer
    - Cancel button
    - Sign out button
After Logout the success logout message will appear on the rightside of the Page.
    

#### <span style="color:green;">Product Management</span>
- The Product Management option will allow the following options such as add the product, edit the product and delete the product for the admin. 
#### <span style="color:green;">My Profile</span>
- Login user can update or store their Delivery information.
#### <span style="color:green;">My Orders</span>
- Order history and information about the products will be stored in the database.
#### <span style="color:green;">Wishlist</span>
- user can add favourite items into the wishlist and shortlist what to buy later.

### <span style="color:green;">Product Details</span>
- Product Details options contains: SKU (Product id),Fabric (Material Type), Description,length, Shipping and Returns.
- Quantity option is available for User to select the number of products of the same product.
- The cart will be update the section.

### <span style="color:green;">Cart</span>
- Shopping Cart page contains: 



### <span style="color:green;">Checkout</span>

### <span style="color:green;">Checkout Success</span>

## <span style="color:green;">Strategy</span>
### <span style="color:green;">UX</span>

#### <span style="color:green;">UserStory using Kanban feature in Agile Methodology</span>
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
    
    
### <span style="color:green;">Business Vision</span>
To create a truly global brand that provides growth opportunities for the company, whilst achieving its goal of becoming the number one value fashion retailer across the globe.
To become a globally prominent online retailer and be ranked amongst the top online retailer in the world in terms of quality, service standards and ultimately customer satisfaction.

### <span style="color:green;">Purpose of Website</span>


## <span style="color:green;">Skeleton</span>
There are approximately 34 products and 3 categories in the designer silks website.
## <span style="color:green;">Scope</span>
### <span style="color:green;">Features</span>
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

### <span style="color:green;">Future Features</span>

## <span style="color:green;">Structure</span>
The site will be structured as clear as possible, with a logic workflow and it should be easy to navigate the site on all screen sizes.
### <span style="color:green;">Wireframes</span>
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

### <span style="color:green;">Database Schema</span>
db diagram used for this website.
<details>
<summary>DB Diagram</summary>
<img src="static/images/db_diagram.PNG" width="500">
</details>

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





### <span style="color:green;">Typography</span>
I have used Open Sans, cursive and 'Raleway', sans-serif to create this website.

## <span style="color:green;">Technologies Used</span>

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
- Amazon Web Servvices -to save media and static folder -https://aws.amazon.com/
- SEO  -https://www.xml-sitemaps.com/
- Privacy policy Generator -https://www.privacypolicygenerator.info/
- For images -https://pixabay.com/
- Testing Real Send Mail -https://temp-mail.org/

## <span style="color:green;">Testing</span>
### <span style="color:green;">Automation Testing</span>
### <span style="color:green;">Code Validation</span>
### <span style="color:green;">Features Testing</span>
#### <span style="text-decoration: underline">Home Page Testing</span>
There are 25 testCases in Home Page.<br>
There are 20 testcases in  header section  which are Designer Silks, Home, Chiffon Sarees, Cotton Sarees, Silk Sarees, All Sarees, By Price, By Rating, By Category, All Products, Contact, search bar, Product Management, My Profile, My Orders, My Wishlist, Register, Login, Logout and Cart Navigation.<br>
Designer Silks heading and Home Navigation are designed to bring the user back to the home page.Testing also proves that these options worked as per design. The other navigations are designed to bring the user to the website.Testing proves that these options worked as per designs.
- [Header-Testing](static/images/home-testing.PNG)
<br>
- There is 1 Testcase in middle of the Hero image. If the user click the Shop Now Button it will navigate to All Products Page. Testing proves that this option worked as per design.
- [Shop-Now-Button-Testing](static/images/home-testing-2.PNG)
<br>

- There are 3 Testcases in the Footer Page.
  1. There is one Social media Facebook link attached in all other pages.When click the Facebook button it brings to the Facebook page.
  2. Privacy Policy for Designer Silks.
  3. Newsletter Subscription
All the three testcases worked as per design requirements.
- [Footer-Testing](static/images/home-footer.PNG)
#### <span style="text-decoration: underline">All Products page Testing</span>
There are 5 testcases in Chiffon Sarees, Cotton Sarees, Silk Sarees, All Sarees, By Price, By Rating, By Category and All Products Page. There are two tescase for  toggle icon for Add Wishlist and Remove Wishlist for login user and if the user not logged in it says that login . And there are two buttons for Edit and Delete the products button for Admin. If the User clicks these buttons it shows that Sorry, Only store owners can do that. Testing proves that these option worked as per design.
- [Product-Page_Testing](static/images/product-page-testing.PNG)

- [Error Message-When the normal user clicks Edit/Delete Button ](static/images/error-msg-testing.PNG)
- [Success Added Wishlist Message ](static/images/add-wishlist-testing.PNG)
- [Removed from Wishlist Message](static/images/remove-wishlist-testing.PNG)

#### <span style="text-decoration: underline">Product_details Page Testing</span>
- There are 7 new testcases in Product detail page such as Quantity increment and decrement button,Keep shopping button, Add to cart button, Proceed to cheekout button and Reviews Post, Edit and Delete button for login User and success and alert messages will display on top of the page. Testing proves that these options, success message and alert messages are worked as per design.<br>
  - Quantity increment decrement button can add 1 to 99 products. cannot add letters or decimal point in that box. 
  - Keep shopping button goes to All product page. Testing proves that this option worked as per design.Testing proves that these options worked as per design.
    - [Quantity Increment, Decrement button and Keep Shopping Button](static/images/quantity_shopping_testing.PNG)
  - When I click Add to Cart button, cart details toast message will appear.  There is Proceed to checkout button for cart page. Testing proves that these options worked as per design.
    - [Add to Cart button and Proceed to checkout button](static/images/add-to-cart-testing.PNG)
  - There are three buttons in Write a Review section in the product detail page. Such Post, Edit and Delete buttons. Post buttons will only appear for any login users.If the user is not login they Cannot see the Post button and ask them to login the page. Edit and Delete buttons are only visible for particular user. 
    - [Post, Edit and Delete Buttons in the Review section ](static/images/post-edit-delete-testing.PNG)
    - if they want to write a review they must enter the comments and must select the rating, otherwise it will give error message.
      - [ Write a Review Form Validation](static/images/review-validation1-testing.PNG)
      - [ Error Message for not entering Review Rating ](static/images/review-rate-validation-testing.PNG)
    - once they submit the post successfully added a review message will appear.
      - [ Success Message for Add Reviews ](static/images/review-success-msg-testing.PNG)
    - if they Edit the button and once they updated the Review then successfully updated message will appear.
      - [ Success Message for Update Reviews ](static/images/review-success-update-msg.PNG)
    - If they press the Delete button Reviews will deleted from Reviews and Deleted alert will display.
      - [ Success Alert Message for Deleted Reviews ](static/images/review-delete-msg-testing.PNG)

- And There are 5 testcases same like All Products page(such as Wishlist add, remove button and Please login tooltip and Edit/Delete the product page.)

#### <span style="text-decoration: underline">Cart Page Testing</span>
- There are 4 Testcases in Cart page. Such as Update, Remove, Keep Shopping and Secure Checkout Buttons.
1. Update Button - User can update the quantity add or minus the number and if they press update button it will update the quantiy and automatically correct the amount of subtotal according to the quantity selected. They can update 0 to 99, Cant enter letter and decimal points. If they updated the quantity then success message will appear. Testing Proved.
  - [ Success Message for Updated the Product quantity ](static/images/update-qty-testing.PNG)
2. Remove Button - User Click the Remove the Button the products will removed and it will open a newpage. It will say that Your Cart is empty. And successfully removed message also appear. There is one button for Return to shop. If the user Press that Button it will redirect to Products page.Testing Proved.
  - [ Product Removed from the Cart message ](static/images/delete-qty-testing.PNG)
3. Keep Shopping - User click the Keep shopping button it will redirect to Product page. Testing Proved.
4. Secure checkout Button - User clicks this button it will go to Check out page. Testing Proved.
  - [ Keep Shopping and Secure Checkout Button ](static/images/secure-checkout-testing.PNG)

#### <span style="text-decoration: underline">Checout Page Testing</span>
There are Two cases in the Check out page. such as Adjust Bag and Complete order Button. And Required form validation Tested in this page. Testing proves that these options worked as per design.
  - Adjust Bag button - It will Redirect to Cart Page if the user want to update or remove the product.Testing Proved.
    - [ Adjust Bag Button ](static/images/adjust-bag-testing.PNG)
  - Complete Order Button - It will goes to Checkout Success Page if they enter all the required Criteria fields.Testing Proved.
  Two Credit Card Details will approve this payment:
    - 4242 4242 4242 4242
    - 4000 0025 0000 3155
    -  [ Complete Order Button ](static/images/adjust-bag-testing.PNG)
  - Forms Validationin the Checkout page
    - [ Validation for Name Field ](static/images/name-field-testing.PNG)
    - Email Field Automatically stored from Login user
    - [ Validation for Email Field ](static/images/phone-field-testing.PNG)
    - [ Validation for Phone Field ](static/images/phone-field-testing.PNG)
    - [ Validation for Address Line1 ](static/images/street-name-testing.PNG)
    - Address Line 2 (street name optional) is a optional one. So there is no validation for this.
    - [ Validation for County or City ](static/images/county-field-testing.PNG)
    - Postcode is a optional one. So there is no validation for this.
    - [ Validation for Country ](static/images/country-field-testing.PNG)
    - [ Validation for Credit Card ](static/images/card-field-testing.PNG)
      - Two Credit Card Details will approve this payment:
      - 4242 4242 4242 4242
      - 4000 0025 0000 3155
    - [ Validation for Incorrect Credit Card ](static/images/incorrect-card-testing.PNG)
    - [ Validation for Incomplete Credit Card ](static/images/incomplete-card-testing.PNG)
    - Once the User entered their shipping address and if they click Save the information to my Profile, it will stored in the Profile page. For next Purchase they dont need to enter the shipping details again. if they want to send for another address then they can edit the address in the same page itself. Testing proves.
    - [ Validation for Save the Information to the Profile Page Checkbox ](static/images/save-info-testing.PNG)
  - If they unclick the Save information when the purchase order done, then it wont stored in the Profile page. Testing Proved.
    - [ Validation for Unclick the checkbox for Save the Information to the Profile](static/images/unclick-checkbox-testing.PNG)

#### <span style="text-decoration: underline">Checkout Success Page Testing</span>
There is one Testcase in the checkout success page which is Go to the HomePage. It will redirect to home page. Testing Proved.
  - [ Go to the Home Page button](static/images/checkout-success-testing.PNG)


## Bugs
1. I try to create new app for wishlist and reviews and add into the products page and product_detail page. But i donot know how to connect these apps to product app. Then i decided to add new model for wishlist and Review in the product app and connect the data into the products templates. Within limited time period i couldnot able to do that, but after this course sure i will learn it.
2. When I complete the payment system i received duplicate order number in the order history and admin page. I resolved this problem with Tutor support.
3. When I do the Real send mail section i didnot received a confirmation message in my email. This problem also solved with Tutor Support.


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
    ==>django-admin startproject designer_silks .
  5. Create a new apps  in the designer-silks project:<br>
      - python3 manage.py startapp home
      - python3 manage.py startapp product
      -  python3 manage.py startapp cart
      - python3 manage.py startapp checkout
      -  python3 manage.py startapp profile
      -  python3 manage.py startapp contact

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
  8. mkdir static folder (for css,js,images and wireframes folder)<br>
       mkdir media folder (for products images)<br>
  9. Now we need to add the required fixtures data into the database in the following order by using the following commands:<br>
      ==> python3 manage.py loaddata categories<br>
      ==> python3 manage.py loaddata products.<br>
  10. Run in the terminal ==>mkdir/templates/includes<br>
  - toast (for using successful, error, warning and info messages throughout the webpage)
  - footer.html
  - main-nav.html
  - mobile-top-header.html
  11. In cart app needs to create contexts.py file.<br>
  IN SETTINGS.PY last line under MEDIA_ROOT
  - FREE_SHIPPING_THRESHOLD = 80
  - STANDARD_SHIPPING_PERCENTAGE = 12
  12. for caluculating the price and howmany quantity
      create new folder in the cart app <br>
      - templatetags(inside the templatetags folder) create 2 files  
        -  __init__.py
        - bag_tools.py
  13. For checkout app:<br>
    - pip3 install django-crispy-forms
    - settings.py => INSTALLED_APPS ==> #other apps
                                      'crispy_forms'<br>
    - under ROOT_URLCONF ==>   CRISPY_TEMPLATE_PACK = 'bootstrap4'
    - OPTIONS  ==>   'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
    - In the terminal  ==> pip3 freeze > requirements.txt
  14. For Media file working
     - in settings.py ==> OPTIONS( below 'django.contrib.messages.context_processors.messages',) ==> 'django.template.context_processors.media',.

#### Stripe payment
1. in the base template add script tag for stripe<br>  <script src="https://js.stripe.com/v3/"></script>
2. in the checkout.html <br>
    {% block postloadjs %}<br>
    {{ block.super }}<br>
    {{ stripe_public_keyjson_script:"id_stripe_public_key" }}<br>
    {{ client_secret|json_script:"id_client_secret" }}
{% endblock %}

  3. pip3 install stripe
  4. in settings.py ==> # Stripe<br>
    FREE_SHIPPING_THRESHOLD = 80<br>
    STANDARD_SHIPPING_PERCENTAGE = 12<br>
    STRIPE_CURRENCY = 'eur'<br>
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')<br>
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')

  5. in the terminal ==> export STRIPE_PUBLIC_KEY and export STRIPE_SECRET_KEY

  6. Create webhook.py
  7. Create webhook_handler.py
  8. In the stripe website ==> Goto Developer then go to webhooks and Add an endpoint for https://designer-silks.herokuapp.com/checkout/wh/


 

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
- Add Procfile and run requirements comment
- Then connect the heroku login in the terminal <br>
heroku login -i(enter username and password) <br>
- python3 manage.py createsuperuser(enter same username, email and password for admin page)
- git add, git commit and git push for heroku main.
- then again go to Heroku Deploy tab connect the github and click deploy for automatic Deployment or manual Deployment.

## Amazon Web Services 
https://aws.amazon.com/ 
- Register in AWS website
1. AWS Management Console, in the search menu ==> type s3 and select Scalable storage in the cloud
  - click ==> create Bucket
  -  bucket name ==> designer-silks
  -  region  ==> AWS Ireland
  -  remove blue tick from ==> Block all public access
  -  tick ==> i acknowledge
  -  then click ==> create bucket
  - then click the bucket name ==> designer-silks
2. Then click ==> properties tab 
    - click edit button in ==> static website hosting ==> click Enable button
    - then index document ==> index.html, error document ==> error.html then click ==> save

3.  Then go to Permission tab (3 changes)

    - cors configuration
			  
			  edit the button for cors configuration and paste the following  ==> 
            [
			{
				"AllowedHeaders": [
				"Authorization"
				  ],
				  "AllowedMethods": [
					  "GET"
				  ],
				  "AllowedOrigins": [
					  "*"
				  ],
				  "ExposeHeaders": []
			  }
			]
			
		- Bucket Policy
			
			- click edit button ==> click policy generator ==> new window will open ==> policy type click: s3 bucket policy ==> principle : * ==> Action: GetObject
			==> copy the ARN number from Bucket Policy and paste ARN : arn:aws:s3:::designer-silks   ==> click: Add Statement  ==> click: Generate Policy
			
			==>then copy the code and paste in Bucket policy box (then add  /* next to designer-silks/* because need to allow access to all resources in this bucket.)
			==> then save
			
			- Access control list (ACL)
			==>click: edit button ==> click Everyone (public access) ==> list (only)
			
4. then click ==> IAM (in the search box)
   - click ==> User groups (left hand side)  ==> create new group ==> name: manage-designer-silks ==> click create group
   - click ==> policies(left hand side) ==> create new policy ==> click JSON ==> click: Import managed policy (right hand side) ==> search box enter: s3 ==> click Amazon s3 Full access
      ==> then click; Import.
	  ==> copy the ARN number from  s3 Bucket policy and paste in JSON code Resources like this 
	  ==> "Resource": [
                "arn:aws:s3:::designer-silks",
                "arn:aws:s3:::designer-silks/*"
            ]  ==> then click: Review Policy ==> name: designer-silks-policy  ==> Description: Access to S3 bucket for Designer Silks static files
			==> then click: create policy
	5.  then again goto User groups ==> click: manage-designer-silks ==> goto: permission ==> click: Add permissions ==> then click: Attach policies
	   ==> then search designer-silks-policy ==> click: Attach policy
	   
	6.  then click ==> Users (left hand side) ==> Add Users ==>name: designer-silks-staticfiles-user ==> click: programmatic access ==>next permission
	   ==>click: manage-boutique-ado ==> just click: next tag ==>just click: next review ==>just click: create user ==> Download Csv (Save it properly cannot take it again).

  7. Then again in the workspace terminal:
    - pip3 install boto3
    - pip3 install django-storages
    - pip3 freeze > requirements.txt
    - then in settings.py enter ==> settings.py INSTALLED APPS ==> OTHER APPS(below crispy form) ==>'storages',
    - under the MEDIA URL
       - if 'USE_AWS' in os.environ:
       - then add:<br>
      Cache control, Bucket Config, Static and media files, Override static and media URLs in production.
      - check the heroku settings <br>
        - AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, USE_AWS.
  - then create new file in the root ==> custom_storages.py<br>
    from django.conf import settings<br>
    from storages.backends.s3boto3 import S3Boto3Storage<br>

class StaticStorage(S3Boto3Storage):<br>
    location = settings.STATICFILES_LOCATION<br>

class MediaStorage(S3Boto3Storage):<br>
    location = settings.MEDIAFILES_LOCATION<br>
    Then do git push.
8. Media files in S3
  - Then again goto amazon s3 ==> designer-silks ==> create folder ==> name: media ==> save it 
  - then upload file all the images (control+shift) ==> permission Grant public-read access ==> then confirm ==> then upload.

### <span style="color:green;">Sending Real Mails</span>

- connect the gmail for sending mails.
- go to gmail account ==> settings ==> see all settings ==> accounts and Import ==> other Google account settings ==> security tab ==> 2 step verification
   ==> Get started ==> password then enter ==> click show more options ==> text message ==> enter 6 digit no from phone ==> turn on 
- then again goto ==> Security ==> App password ==> select app: mail ==> select device: other ==> then write: Django ==> click: generate ==> copy the app password
- Then go to Heroku SETTINGS enter  ==>    EMAIL_HOST_PASS, EMAIL_HOST_USER 
4. in settings.py
at the end ==>
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'kavithasanthanesh@gmail.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
  - git add . ==> git commit -m "sending real emails"

  - to check the email ==> temp email.com ==> copy the email address ==> register in the app using temp email.==> we can receive emails to temp email page. if we click that
    there is a url for confirm the verification ==> copy the url and paste in the browser and confirm it. then again sign in for the app.

  
## <span style="color:green;">SEO</span>

https://www.xml-sitemaps.com/
- Enter Heroku URL to create a sitemap
- Download you XML SITEMAP
- Then create sitemap.xml in the gitpod workspace and paste XML SITEMAP
- Then Create robots.txt, inside it enter the following details:
  - User-agent: *
  - Disallow: /accounts/
  - Disallow: /cart/
  - Sitemap: https://designer-silks.herokuapp.com//sitemap.xml
- Then add the meta tag in the base template head. Some inportant keywords for user. 

## <span style="color:green;">Web Marketing</span>
### Facebook account


## <span style="color:green;">Email Marketing</span>
### MailChimp- Newsletter Subscription
- Register for MailChimp account for designer silks email address. And create Signup embeded form, and take only Newsletter column for user newsletter subscription.

## <span style="color:green;">General Data Protection Regulation(GDPR)</span>
### Privacy policy Generator
https://www.privacypolicygenerator.info/ 
- Enter Company Name, website name, Herokku Url followed by Country,State and email then click generate private policy. Copy the link clipboard and Paste in the base template footer.

## <span style="color:green;">Final deployment:</span>

After finish the project then need to do the following steps:

  - Debug= False in settings.py
  - git add . git commit -m "deployment commit" git push
  - Then Deploy and can view the App in Heroku.


## <span style="color:green;">Acknowledgement</span>
  - I would like to thank my mentor Rohit Sharma and my tutors Kasia for their helpfulness, constructive feedback and guidance when needed.
  - I would like to thank the staff, all the tutor supporters, students and my peers of Code Institute for their help.
  -I also like to thank Slack Community for sharing the open discussion from various students.
  - I search lots of information from Google, W3 School and Youtube for this project.
  - I follow the base structure in Boutique ado walkthrough. It will help me a lot for this project.
  - The images on this site have been taken from https://pixabay.com/, and used only for education purpose to complete this project.
  - Thanks for reading my README.md file.


