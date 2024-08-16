import streamlit as st

def show():
    # Title
    st.title("Express.js: In-depth Exploration")

    # 1. Routing
    st.header("1. Routing")
    st.subheader("Explanation:")
    st.write("""
    Routing refers to how an application responds to a client request at a particular endpoint (URI) and HTTP method (GET, POST, PUT, DELETE). 
    Express.js provides a simple and flexible routing mechanism.
    """)

    st.subheader("Example:")
    st.code("""
    const express = require('express');
    const app = express();

    app.get('/', (req, res) => {
      res.send('Hello World!');
    });

    app.post('/submit', (req, res) => {
      res.send('Form submitted');
    });

    app.put('/update/:id', (req, res) => {
      res.send(`Updating item with ID: ${req.params.id}`);
    });

    app.delete('/delete/:id', (req, res) => {
      res.send(`Deleting item with ID: ${req.params.id}`);
    });

    app.listen(3000, () => {
      console.log('Server is running on port 3000');
    });
    """, language='javascript')

    st.subheader("Practical Use Case:")
    st.write("Routing allows you to define how your backend server responds to various HTTP requests. It’s the backbone of any RESTful API.")

    st.subheader("Assignment:")
    st.write("Build an Express.js app with routes for GET, POST, PUT, and DELETE to manage a simple CRUD application for tasks (e.g., a To-Do List).")

    # 2. Middleware Functions
    st.header("2. Middleware Functions")
    st.subheader("Explanation:")
    st.write("""
    Middleware functions are functions that have access to the request object (req), the response object (res), and the next middleware function in the application’s request-response cycle.

    - **Built-in Middleware**: express.json(), express.static()  
    - **Third-party Middleware**: morgan for logging, helmet for security headers  
    - **Custom Middleware**: Middleware that performs specific tasks like logging or authorization
    """)

    st.subheader("Example:")
    st.code("""
    const express = require('express');
    const app = express();

    // Custom middleware to log requests
    app.use((req, res, next) => {
      console.log(`${req.method} ${req.url}`);
      next();
    });

    app.get('/', (req, res) => {
      res.send('Hello World');
    });

    app.listen(3000, () => {
      console.log('Server running on port 3000');
    });
    """, language='javascript')

    st.subheader("Practical Use Case:")
    st.write("Middleware is essential for tasks like logging requests, handling authentication, serving static files, and managing error handling.")

    st.subheader("Assignment:")
    st.write("Create custom middleware that logs request details (method, URL, timestamp), checks for user authentication, and serves static files.")

    # 3. Request and Response Handling
    st.header("3. Request and Response Handling")
    st.subheader("Explanation:")
    st.write("""
    Handling the request and response in Express.js allows you to interact with data sent by the client (via the req object) and send back the appropriate data or status codes (via the res object).

    - **req**: Contains information about the HTTP request (URL parameters, query strings, body data, etc.)  
    - **res**: Methods to send data back to the client (res.send(), res.json(), res.status())
    """)

    st.subheader("Example:")
    st.code("""
    app.post('/user', (req, res) => {
      const userName = req.body.name;
      res.status(201).json({ message: `User ${userName} created!` });
    });
    """, language='javascript')

    st.subheader("Practical Use Case:")
    st.write("You'll use request and response handling to process incoming data (e.g., form submissions, JSON payloads) and respond with the appropriate success or error messages.")

    st.subheader("Assignment:")
    st.write("Create an endpoint that accepts user data via POST request, processes it, and sends a JSON response with a status code.")

    # 4. Error Handling
    st.header("4. Error Handling")
    st.subheader("Explanation:")
    st.write("""
    Error handling in Express.js ensures that errors are caught and handled properly, preventing them from crashing the server.

    - **Basic Error Handling**: Using try/catch blocks or returning error responses  
    - **Custom Error Handlers**: Middleware that captures and processes errors
    """)

    st.subheader("Example:")
    st.code("""
    app.get('/', (req, res, next) => {
      try {
        // Simulating an error
        throw new Error('Something went wrong!');
      } catch (err) {
        next(err); // Forward error to the custom error handler
      }
    });

    // Custom error handler
    app.use((err, req, res, next) => {
      console.error(err.stack);
      res.status(500).send('Internal Server Error');
    });
    """, language='javascript')

    st.subheader("Practical Use Case:")
    st.write("Error handling is crucial for maintaining a reliable server and ensuring that errors are logged and proper responses are sent to the client.")

    st.subheader("Assignment:")
    st.write("Implement error handling in your CRUD application that sends appropriate HTTP status codes and error messages when operations fail.")

    # 5. Serving Static Files
    st.header("5. Serving Static Files")
    st.subheader("Explanation:")
    st.write("""
    Express.js provides a built-in middleware express.static() to serve static assets such as HTML, CSS, images, and client-side JavaScript files.
    """)

    st.subheader("Example:")
    st.code("""
    app.use(express.static('public')); // Serve files from the 'public' directory

    // Now the client can access files via http://localhost:3000/filename
    """, language='javascript')

    st.subheader("Practical Use Case:")
    st.write("You’ll often need to serve static files when building web applications, such as serving the client-side part of a single-page application or assets like images and stylesheets.")

    st.subheader("Assignment:")
    st.write("Create a simple static site using Express.js that serves HTML, CSS, and JavaScript files from a public directory.")

    # 6. REST API Design Principles
    st.header("6. REST API Design Principles")
    st.subheader("Explanation:")
    st.write("""
    REST (Representational State Transfer) is an architectural style that defines a set of constraints for creating scalable web services. RESTful APIs rely on HTTP methods and status codes for communication.

    - **Statelessness**: Each request should contain all the information the server needs to fulfill it  
    - **HTTP Methods**: GET, POST, PUT, DELETE, etc.  
    - **Resource-based URLs**: Use nouns in endpoints (/users, /posts), not actions
    """)

    st.subheader("Example:")
    st.code("""
    app.get('/posts', (req, res) => { /* return list of posts */ });
    app.post('/posts', (req, res) => { /* create a new post */ });
    app.put('/posts/:id', (req, res) => { /* update a post by ID */ });
    app.delete('/posts/:id', (req, res) => { /* delete a post by ID */ });
    """, language='javascript')

    st.subheader("Practical Use Case:")
    st.write("Building RESTful APIs helps create a standard interface for communicating with client applications (mobile apps, front-end web apps, etc.).")

    st.subheader("Assignment:")
    st.write("Design and build a RESTful API for managing a collection of resources (e.g., books, users, products) using Express.js.")

    # Theoretical Questions
    st.header("Theoretical Questions")
    st.write("""
    1. Explain how middleware functions work in Express.js and describe their role in the request-response lifecycle.  
    2. What is the difference between a route handler and a middleware function in Express.js?  
    3. Why is it important to follow RESTful principles when designing APIs?  
    4. What are the benefits of using middleware for handling errors in Express.js?  
    5. How does Express.js serve static files, and why is it essential for many web applications?
    """)
