# capstone

##Overview
Codecademy Headquarters is located in the beautiful South of Houston (SoHo) neighborhood of New York City. This neighborhood has a lot to offer — especially the restaurants! In this project, you will use your knowledge of data structures to build an autocomplete search program that returns a list of restaurants in SoHo and their information (please note that the data is fake for the purposes of this project). The final product should have a similar user experience to the following:


Erwartetes Ergebnis als Video/Demo :
https://youtu.be/0Ks9GNpJYf0




Unlike the data structures projects you've encountered so far, this project allows you to choose which data structures to use — we are confident that you will choose wisely! All of your code (unless you choose the Trie implementation mentioned below) will be written in script.py.
The data is stored in data.py and imported into script.py so you can properly access the data. You also have access to various data structures. If these data structures don't fit your needs for the project, feel free to make up your own variations! We just ask that you do NOT utilize Python's built-in list class to handle your data.
This project consists of main two parts:
⦁	Implementing an autocomplete for food types that returns a list of possible food types based on the beginning of a word. You'll use the data stored in food_types, which is a list of all the different types of food the user can select from. It is up to you how to properly store and retrieve the data. Some possible options are listed under the Part 1 section.
⦁	Retrieving and displaying all of the restaurant data. This data is stored in restaurant_data, which is currently a list of lists. The first value in each list is the food type, the second value is the restaurant name, the third value is the price, the fourth value is the rating, and the fifth value is the address. It is up to you how to properly store and retrieve the data. Some possible options are listed under the Part 2 section.

Part 1: Choosing a Data Structure to Search for Food Types
The first step is to implement the search-by-word-beginning functionality demoed below

https://youtu.be/pZuNTOjbhf8

Linked List of Words
In this option, create a linked list of all the different food types:
 
Traverse the linked list to see if any of the food types start with the string that the the user entered. If any do, create a new linked list that stores the matches and return data from that linked list to the user. If that linked list has a size that is greater than one, then the user will need to input additional letters until there is only one option.
Hash Map of First Character to Words
In this option, create a hash map of linked lists where:
⦁	the key is the first letter
⦁	the value is a linked list of words that start with that first letter
 
Retrieve the linked list that corresponds with the first letter that the user inputted. If that linked list has a size that is greater than one, then the user should keep inputting letters until there is only one option.
Trie
Tries are tree-like data structures. You can read about them here. They could be visualized as such:
 

Tries are extremely efficient for searching for words through strings. Although you haven’t implemented the data structure yourself, we’re suggesting this option as a challenge for you to use a new data structure (feel free to search the web for example implementations). The functionality of the user experience should remain the same as the linked list and the hash map. We have created the file trie.py for you to implement your Trie class in. If you are up for the challenge, go for it!
Part 2: Choosing a Data Structure to Retrieve Restaurant Data
The second step is to implement retrieving the restaurant data as demoed:
https://youtu.be/kV6CJgtxPxc

Here are a few possible pathways to complete the task:
Linked List of Data
Create a linked list of linked lists to represent the restaurant data as shown below:
 

After retrieving the food type from the user, access and traverse the corresponding linked list to find the restaurants for that food type. After retrieving the data, display the data for each restaurant of that food type in a user-friendly manner.
Map Food Types to Linked Lists of Restaurant Data (also Stored in Hash Maps)
Create a hash map that maps each food type to a linked list. Each linked list would chain hash maps to store restaurant data as shown below.
 
After retrieving the food type from the user, retrieve the linked list of hash maps from the corresponding food type. You can traverse that list to retrieve all of the restaurant data. After retrieving the data, display the data of all the different restaurants of that food type in a user friendly way!
Presentation
After using your knowledge of data structures to create this project, submit your code and a presentation for review against this rubric. Your presentation should address the following:
⦁	Which data structure(s) did you use for part 1? Why did you select these data structures?
⦁	What is the runtime (in asymptotic notation) of searching for a food type? Do you think there is a more efficient runtime?
⦁	Which data structures did you use for part 2? Why did you select these data structures?
⦁	What is the runtime (in asymptotic notation) of retrieving the restaurant data? Do you think there is a more efficient runtime?
⦁	Outside of this project, what are other innovative ways you can utilize data structures?

Get Started


Backup: 
https://www.codecademy.com/articles/github-issues-cheatsheet
Demo:
https://s3.amazonaws.com/codecademy-content/programs/cs-path/data+structures+capstone/Data+Structures+Capstone+Demo.mp4