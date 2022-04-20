# pythonFlask

Flask is good when you want to create web applications that have no dynamic web pages. The easiest task for Flask, which can be completed in 10-15 minutes, is a one-page business card site that presents a company or a person. Sounds great, doesn't it?

## routes

the routes connect the application's URL paths to functions that contain the content for these paths. For example, when users access /about/, we may want to execute the render_about() function to show the particular content. Similarly, when they type in /products/, we would like to run render_products().

> To bind a URL with a view function, Flask uses decorators. Here's how we can create a route:|

        @app.route('/')
        def hello_world():
            return 'Hello World!'

### Passing parameters

In the example with employees, we would need to designate the variable name variable in the route and pass it to the function as a parameter:


        @app.route('/employee/<name>/')
        def show_profile(name):
            return "Employee Name: " + name

In the example above, the value inside the <> brackets indicates a variable that allows us to declare route rules. In this case, the rule is that the show_profile function will handle every request matching the /employee/<name>/ template.

### Passing several parameters

To pass them, use the following pattern:

        @app.route('/movies/<genre>/<title>/')
        def render_movie(genre, title):
            return "There will be a " + genre+ " movie "

### Type conversion

A URL is a string, so the data obtained from it is passed to the function in the form of a string.

However, we don't always need a string. Flask allows us to change the immediate type of a variable:

        @app.route('/movies/<int:movies_id>/')

        @app.route('/movies/<float:movies_id>/')

### Processing requests

Firstly, we need to import Flask as well as request, a new object we will work with:

        from flask import Flask
        from flask import request

we route the page using the familiar decorator. Note that this time, we add the methods parameter to show Flask which requests our app will accept:

        @app.route('/', methods=['POST', 'GET'])

Flask route only answers to GET requests by default. To make the route able to handle other types of requests, you shall pass them in to the methods list when defining the decorator.

            def login():
                if request.method == 'GET':
                    template = """
                     <form method='POST'>
                    <input type='text' placeholder='Username...'>
                    <input type='password' placeholder='Password...'>
                     <input type='submit' value='Auth'>
                    </form>
                    """
                    return template

                elif request.method == 'POST':
                    return 'Wow! Great, you logged in!'
### Responses

Response class. It allows us to set up special properties such as adding headers to an ordinary web page (or rather to the response that returns it), specify the language that is used for the web page, list the allowed methods, like POST, PUT, GET, and many more.

        from flask import make_response

### The jsonify method
 The jsonify method helps us to create a proper response object from JSON output. Let's start with the import:

            @app.route('/')
            def no_data():
            response = jsonify({'message': 'Hello there!', 'info': 'Using jsonify...', 'status': 200})
            return response

### Common error codes

- 404 Not found : indicates that the client was able to communicate with the server, but the server cannot find the data as per request.

- 403 Forbidden: means that you have limited or no access to the content on the page you are trying to reach.

- Internal server error 500:  usually occurs due to programming errors or when the server is overloaded. 


### Error handlers
The error handler is a function that returns a response when an error type occurs. It is quite similar to how a view function returns a response when it matches a request URL. To register an error handler, we need to pass an instance of the error to a built-in


rom flask import render_template

@app.errorhandler(404)
def page_not_found(e):  # error instance is automatically passed to the function
    return render_template('404.html')


from flask import jsonify

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404

# The abort() function

The abort helper wraps errors into a HTTPException so they can behave properly. You can try the following:

        from flask import abort
        abort(400, 'My custom message') 

# Flask-RESTful
Let's start with a Flask extension called Flask-RESTful. It is a Python module that allows us to build a RESTful API with Flask. Before we go further, we should note that all API endpoints (routes) will look like the default view functions.

        from flask import Flask
        from flask_restful import Resource, Api

        app = Flask('main')
        api = Api(app)

The second thing we need is Resource. It's a class that provides an easy way to create API functions: we can write classes that inherit Resource and use its architecture to create an API. In the example below, we create the HelloWorld class that inherits Resource with a GET method. This view class will be an API endpoint:

        class HelloWorld(Resource):
            def get(self):
                return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

## Parsing arguments
Flask allows us to get data from the request body easily, but we should also parse arguments from a URL for our API. The reqparse interface can help us with this! It's a built-in flask_restful feature that works similarly to the argparse module.

parser = reqparse.RequestParser()
parser.add_argument('Writing', type=str, help='This is what You will see on The Wall')

We've created the RequestParser object and specified an argument with the name of writing, type is str, a description is provided in the help argument. The next step is to create a resource that requires data from a URL:

class HelloArgs(Resource):
    def get(self):
       data = parser.parse_args()  
       return {'data_from_url': data}

The final move — create a route to our resource using the add_resource method:

api.add_resource(HelloArgs, '/')