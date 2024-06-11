import os

logged_in_user = os.getlogin()


"""

Setting the structure of my JSON file up. 
I'm taking a non-relational database approach, without the 
overhead of a MongoDB running. Just simply templating 
into a JSON file of my own making. 

We probably need a 

"""

# template is strictly for
user_template = {
    "datetime": "",  # To be populated with the logged-in username.
    "mood_score": ""
}



