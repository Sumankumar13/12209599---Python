import random
when = ['Yesterday morning ', 'Yesterday', 'Last night', 'Morning','Yesterday night']
who = ['Aman', 'Anand', 'Saurabh', 'Akash','Sushant']
residence = ['Bihar','Uttar Pradesh', 'Jharkhand', 'Banaras', 'Delhi']
went = ['park', 'university','seminar', 'school', 'Home']
happened = ['make a lots of fun','dance with friends', 'Enjoyed whole day', 'studied with Aman', 'wrote a book']
After = ['return back to the home','sleep','feel tired','not happy','feel bored']
print(random.choice(when) , ', ' , random.choice(who) , ' that lived in ' , random.choice(residence) , ', went to the ' , random.choice(went) ,' and ' , random.choice(happened), ',',' after that' ' ' ,random.choice(After),".",sep="")