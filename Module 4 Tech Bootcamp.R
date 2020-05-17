#Exercise 1: Print the Time
Sys.time()

#Exercise 2: Make a Simple Stopwatch
timerun <- function(x){
  x=Sys.time()

##The instructions say "record" and not "print", but noting that print(x) before this line helped with testing
print(x-Sys.time())}

timerun(x)

#Exercise 3: Print a Word Provided by the User
##In R, it seems like the word has to be entered in the console first, so this can't be run altogether?
print(b <- readline(prompt= "Type something here:"))

#Exercise 4: Validate User Input
#For this I used the library hunspell for the en_US dictionary
install.packages("hunspell") 
library(hunspell)
#Initialize i for while
i=0
#I tried to use recursion here.
runit <- while(i=0)
  {print(d<-readline(prompt="Type a word here:"))
 while(hunspell_check(d)==FALSE){
   d<-readline(prompt="Please type an English word:")
   print(d)
   runit}
    i<-i+1
  }

#Exercise 5: Record and Print a List
#The user is required to define the size of the list first
x <-readline(prompt=("Enter # of items in your list"))
y <- vector(mode="list",x)
i=1

#After the size of the vector is defined, we ask user to add until we reach the last space
while(i<=(x)){
  g <- readline(prompt="Enter item")
y[[i]] <- g
i<-i+1
print(y)}