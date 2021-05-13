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


### View as Another User

### Automated Messages

### Admin Reports

## Want to Know More?
This project was organized user Azure DevOps. If you would like to see our users stories, progress metrics, or just more information on the project reach out to me at sheldonmatt517@gmail.com and I can send you an invite to the DevOps project.
