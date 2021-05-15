# Truck Driver Rewards
by Zach Amend, Devon Gilliard, and Matt Sheldon

## Introduction
This is the source code for our Driver Rewards website. The 3 of us worked in an agile development setting across 10 week long sprints. We started the first sprint off with creating just over 200 user stories that we would work to accomplish throughout the 10 sprints. We had a meeting every week to show our progress to eachother and a class TA who acted similar to a SCRUM leader. The purpose of the website is to  create a place where companies can reward drivers good driving habits with the ability to buy products from a company catalog. 

## User Types
We had 3 different types of users on our websites drivers, sponsors, and admins. Each user had acess to different priviledges and features. Driver users had the least privileges then the sponsors and admins had full privileges. 

## Features
### Account Creation and Management
We have implemented a standard login page that all users interact with  when they first get to the website. On the login page we have a password recovery feature where users can reset their password if they forget. Upon logging in we use the database to determine what type of user they are because different users have different features and privileges and therefore have different interfaces on the website. Once users are logged in they are all able to update their account information through our account management page. From this account management page users are also able to delete their account if they so choose. Admins also have the ability to go in and change user information of drivers and sponsors as well as the ability to delete driver and sponsor accounts.

### Point System
The drivers are not given cash as their reward they are given points that can be used to redeem items from their company catalog. Each company is control of how many points a driver has and can add or remove points manually at any time. Sponsors also have the ability to control how much thier companies points are worth in terms of USD. For example one company may want 100 points to be a single dollar and some companies may want 100 points to be 100 dollars or any where inbetween. The sponsors are able to assign points any dollar amount based on their needs.

### Company Catalogs
Sponsors also control the items on the company catalog so that drivers can not buy any item they want. There are filters that sponsors can use but the main way we control what items are on the catalog is by keyword. The sponsors use keywords to find items they want on the catalog and we use the eBay API to find items matching the keyword(s). If a specific item is not one a sponsor likes that sponsor can go in and remove specific items. All users can see the compnay catalog but only sponsors and admins can edit the catalog. If necessary sponsors and admins have the ability to purchase items for specific drivers.

### Point and Purchase Histories
Users have the ability to view their purchase history at anytime to see which items from the catalog they have purchased as well as information about the item they purchased. If they user has purchased the item recently there is an option to cancel the purcahse which will refund the user their points and remove the item. Similarly there is also a points history page. This allows users to keep track of there earned points, removed points, and point purchases as well as information such as when the points were given or taken and which sponsor or admin gave or took away the drivers points. This allows all users to be confident that they are being treated fairly.

### View as Another User
Because different users have different interfaces due to their privelege levels we gave sponsors and admins the ability to view pages from a different users perspective. Of course this is only an option for view a user of lower privilege so that sponsors are unable to see admin pages. When viewing the website as another users sponsors and admins are able to do everything that a user of that type is able to do and they are given unlimited dummy points so that they can test out any features to their hearts content.

### Automated Messages
Anytime a user completes a task they are given feedback on their homepage in the form of messages. Users can filter and delete messages if they want to decluyter but the messages do not go away until the user chooses to remove them. Some examples of messages are confirmation messages that lets a user know that something was done succesfully. For example a sponsor has added you to their company, that you successfully purchased an item, that you succesffully canceled an item. that you changed your account information, etc. There are also error messages such as unable to purchase product, could not update account, etc. Finally there are messages that keep you updated about changes to your account by others. This could include account information being changed, points being updated, products being purchased, sponsors removing you from the company, etc.

### Admin Reports
Finally we implemented automated monthly reports that are sent to admins for each company that summarize all purchase information of that month so that admins and sponsors can get a better sense of how the drivers are responding to the website.

## Want to Know More?
This project was organized user Azure DevOps. If you would like to see our users stories, progress metrics, or just more information on the project reach out to me at sheldonmatt517@gmail.com and I can send you an invite to the DevOps project.
