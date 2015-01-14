General:
    It's nice that you broke up the database-related functions and the 
    API-related functions; compartmentalization is something that I 
    think a lot of us neglect.

app.py: 62
    I'm not sure why you have to create a new variable and loop 
    through the old one. Perhaps you could just use the old 
    variable?

tvmaze.py: 51
    Flask??? The flask makes your application crash and I don't 
    know what it's for.

tvmaze.py: 48
    Put a "pass" in the body of a function you'll write later; it
    makes things easier to read.

mongo.py: 14, 22
    The loop you set up is strange.  Since you'd be returning after
    the first iteration of a for loop, I don't know if the for loop
    is necessary to begin with; an "if" statement might suffice here.
    The for loop is misleading because it appears as if there could
    be multiple users with a certain account name, but only the first
    one found would be used.

geo.py:
    It seems you want to do geolocation-related things eventually,
    but is it necessary?  I'm not sure how your project would use it.
