### Nesting

print '=== 1 ==='

# 1: dictionaries in dictionaries (challenge)
# This may helpful for part 2 (depending how you do it)
# Recall that a dictionary's value can be any type of object -- even dictionaries.
# so, we might have:
#dinosaurs = {"carnivores":{"Velociraptor":3,"Coelophysis":1,"Tyranosaurus Rex":2},"herbivores":{"Avaceratops":3,"Brachiosaurus":1,"Diplodocus":2,"Stegosaurus":1}}
#
#
# for that dictionary, we can access our count of velociraptors with the following:
# raptorcount = dinosaurs['carnivores']['Velociraptor']
# or print it:
#print "raptors: "+str(dinosaurs['carnivores']['Velociraptor'])
#
# the first time we saw a Carnivore, we could have created a blank dictionary for
# for its value with the following:
#dinosuars['carnivores'] = {}
# or, instead, a dictionary with keys and zero values for raptors and Tyranosaurs,
# our favorite carnivorous dinosaurs, for the value with the following:
#dinosaurs['carnivores'] = {'Velociraptor':0,'Tyranosaurus Rex':0}

dinolist = [("carnivores","Velociraptor"),("herbivores","Diplodocus"),("carnivores","Coelophysis"),("herbivores","Avaceratops"),("carnivores","Velociraptor"),("carnivores","Velociraptor"),("carnivores","Tyranosaurus Rex"),("herbivores","Avaceratops"),("carnivores","Tyranosaurus Rex"),("herbivores","Avaceratops"),("herbivores","Brachiosaurus"),("herbivores","Stegosaurus")]
dinosaurs= {}
#
# dinolist contains a list of tuples -- immutable lists, indicated in the () -- where each 
# represents a dinosaur type and whether it is a herbivore or carnivore. You can index items 
# in a tuple just like you would with a list.
#
# iterate over the tuples in dinolist (above) to build the above dictionary
#
# You may assume that every dinosaur is a carnivore or herbivore, but for an extra challenge
# try to do this without that assumption. 
#
# put your code here

for dino in dinolist:
    if dino[0] not in dinosaurs:
        dinosaurs[dino[0]] = {}
    dinosaurs[dino[0]][dino[1]] = dinosaurs[dino[0]].get(dino[1],0)+1

print dinosaurs

### Objects

print '=== 2 ==='

# In these exercises, you will define a class for Book. This will be roughly based
# on the book dictionary from the lecture slides on dictionaries, but by adding
# methods, we will see why objects can be much more powerful.

print '=== 2a ==='

# define a class Book, whose constructor takes and assigns
# the following parameters:
#     title (string)
#     author (string)
#     year (integer)
#     publisher (string)

# Title and author should be *required* parameters. Year and publisher should
# not be required and their default values should be None. 
# HINT: in methods, you can create default parameters, just like with functions.

# uncomment the next line define your Book class there
class Book():
    def __init__(self,title,author,year=None,publisher=None):
        self.author = author
        self.title = title
        self.year = year
        self.publisher = publisher
    def cite(self):
        return "%s. (%d). %s. %s."%(self.author,self.year,self.title,self.publisher)        

# you can uncomment the following lines to see if this works
# you can compare the output with the output in the PDF
nudge = Book(title="Nudge",author="Thaler & Sunstein")
print nudge.title
print nudge.author
print nudge.year
print nudge.publisher

nudge = Book(title="Nudge",author="Thaler & Sunstein",year=2008,publisher="Penguin")
print nudge.title
print nudge.author
print nudge.year
print nudge.publisher

print '=== 2b ==='
# Now we will add a method to generate the citation. The method should be called "cite".
# It should return a string in the format: "Author. (Year). Title. Publisher."

# Note: You will have to define the method above, in your class definition.

# Then, uncomment the next line to test. This should print the citation if you
# have properly defined the Book.cite() method.
print nudge.cite()


### JSON 
print '=== 3 ==='
import json

#hw4example.json
# used http://www.deanclatworthy.com/imdb/?q=movie+title+here to generate data
# though it now seems to be down?

print "--- 3a ---"
##1. load the JSON file 'hw4example.json', and convert it from a string to JSON.
# Print its contents. It's a list of metadata about movies.
## after you are done, comment out the print statement (so it no longer prints)

import json
moviedata = json.load(open('hw4example.json'))
#print moviedata

print "--- 3b ---"
##2. print the first element of the JSON file. it's metadata about a movie.
## after you are done, comment out this exercise (so it no longer prints)

#print moviedata[0]

print "--- 3c ---"
##3. print the keys and values in the format key: value of the first element of the json file 
#   (so the attributes of the first movie get printed).
#   e.g., Title: Little Miss Sunshine
#   Order does not matter

for field in moviedata[0]:
    print "%s: %s"%(field,moviedata[0][field])

print "--- 3d ---"
##4. write a *function* to print only the title, genres, and IMDB rating, and Metascore for a movie
### It should print these details in that order.
###
### Caution: Depending how you print title, you may get a unicode error when you get to Amelie.
#   You should be able to work  around this by using the template format of output we talked about (%s)

def printDetails(m):
    for f in ['Title', 'Genre', 'imdbRating', 'Metascore']:
        print "%s: %s"%(f,m[f].encode('utf-8'))

print "--- 3e ---"
##5. use the function from (3d) to print the data for each movie

for m in moviedata:
    printDetails(m)

print "--- 3facebook ---"
#Now, we're going to switch to hw4fbpost.json. This file contains just one post and related comments from
#the class facebook feed.
#
#Load the contents of hw4fbpost.json, convert it to a dictionary, and print the keys

postdata = json.load(open('hw4fbpost.json'))
print postdata.keys()

#
print "--- 3g ---"
# Print the URL for the picture in the message. 

print postdata['picture']

print "--- 3h ---"
# Write code to determine the total number of comments on the post and print it. 
# Pay attention to types and the level of nesting in here.

print "Comments: %d"%len(postdata['comments']['data'])