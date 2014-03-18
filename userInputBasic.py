name = raw_input('What is your name?\n')
cats = raw_input('How many cats do you have?\n')
dogs = raw_input('How many dogs do you have?\n')
other = raw_input('How many other animals do you have?\n')

#convert raw input to int
numberCats = int(cats)
numberDogs = int(dogs)
numberOther = int(other)

pets = numberCats + numberDogs + numberOther

print 'Hi, %s. ' % name 
print 'You have %s ' % pets +'pets'
