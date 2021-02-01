from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)

# This option will cause Jinja to throw UndefinedErrors if a value hasn't
# been defined (so it more closely mimics Python's behavior)
app.jinja_env.undefined = StrictUndefined

# This option will cause Jinja to automatically reload templates if they've been
# changed. This is a resource-intensive operation though, so it should only be
# set while debugging.
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = 'ABC'

MOST_LOVED_MELONS = {
    'cren': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
        'name': 'Crenshaw',
        'num_loves': 584,
    },
    'jubi': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg',
        'name': 'Jubilee Watermelon',
        'num_loves': 601,
    },
    'sugb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg',
        'name': 'Sugar Baby Watermelon',
        'num_loves': 587,
    },
    'texb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg',
        'name': 'Texas Golden Watermelon',
        'num_loves': 598,
    },
}


# MY ROUTES START HERE
@app.route('/')
def start_here():
    """Return homepage."""
    
### MUCH EXPLANATION HERE ###
    # this get request is for a session labeled 'username'
    # it calls up input from the html that has been assigned to 'userinput' 
    # this code makes {name: userinput} available to all functions
    # think of 'session' as data-in-this-session
    
    # And saying it another way: 
    # the userinput called up is stored in a session called 'username'
    # session is at whatever_name_I_write, and
    # the get is for what I listed as 'name' = (get the thing) in the referenced html file 
    # session["username"] = request.args.get("user_input")

    # writing this explicitly for clarity; 
    # normal syntax is 
    # session[username] = request.args.get(')
    # and adding a line here to regularize the
    # syntax of output by capitalizing
### END EXPLANATION HERE ###

    user = session.get('username', None)
    if user != None:   
        return redirect ('/top-melons')
    return render_template('homepage.html')

@app.route('/get-name')
def get_name():
    """Get the user's name and send to top-melons."""
    
    # if userinput in session:
    #     return render_template
    
    input_from_user = request.args.get('userinput')  
    session['username'] = input_from_user
    
    return redirect('/top-melons')                   


@app.route('/top-melons')
def show_top_melons():
    """Display the most-loved melons."""
    top_Melons = MOST_LOVED_MELONS

    # if username is a key in the collection "session", 
    # show topmelons.html
    # else 
    # redirect to HomePage

    user = session.get('username', None)
    if user != None:
 #   if 'username' in session and session['username'] != None:

        return render_template('top-melons.html',                   
                                #userinput=session['username'], 
                                top_melons=MOST_LOVED_MELONS)
        
    else:
         return redirect('/') # go to the beginning


if __name__ == '__main__':
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')
