import streamlit as st

def show():
    # RESTful API Design Principles
    st.header("RESTful API Design Principles")
    st.write("""
    **Explanation:**
    RESTful API design principles are crucial for creating APIs that are efficient, scalable, and easy to use. REST (Representational State Transfer) is an architectural style that leverages standard HTTP methods and status codes.

    - **Statelessness**: Each request from a client contains all the information needed to process the request. The server does not store client context between requests.
    - **Resource-Based URLs**: Use nouns to represent resources (e.g., `/users`, `/orders`), and actions are performed using HTTP methods (e.g., `GET`, `POST`, `PUT`, `DELETE`).
    - **HTTP Methods**: Use standard HTTP methods to perform CRUD operations:
      - `GET` - Retrieve data
      - `POST` - Create new data
      - `PUT` - Update existing data
      - `DELETE` - Remove data
    - **Status Codes**: Use HTTP status codes to indicate the result of a request (e.g., `200 OK`, `201 Created`, `404 Not Found`, `500 Internal Server Error`).

    **Example Code:**
    ```javascript
    // Express.js routes for a RESTful API
    app.get('/api/users', (req, res) => {
      // Retrieve and return a list of users
    });

    app.post('/api/users', (req, res) => {
      // Create a new user and return it
    });

    app.put('/api/users/:id', (req, res) => {
      // Update user information by ID and return the updated user
    });

    app.delete('/api/users/:id', (req, res) => {
      // Delete a user by ID
    });
    ```
    **Practical Use Case:**
    RESTful API design ensures that APIs are consistent, easy to understand, and can be consumed by different clients (e.g., web, mobile).

    **Assignment:**
    - Design and implement a RESTful API for managing a resource (e.g., books, users) in Express.js. Use appropriate HTTP methods and status codes, and ensure your API follows REST principles.
    """)

    # API Documentation
    st.header("API Documentation")
    st.write("""
    **Explanation:**
    API documentation provides clear and comprehensive information about how to use your API. Good documentation includes endpoints, request/response formats, status codes, and examples.

    - **Swagger/OpenAPI**: A popular tool for designing and documenting APIs. It provides a way to define API endpoints, request parameters, response formats, and more.

    **Example Code:**
    **OpenAPI Specification (Swagger)**
    ```yaml
    openapi: 3.0.0
    info:
      title: User API
      version: 1.0.0
    paths:
      /users:
        get:
          summary: Retrieve a list of users
          responses:
            '200':
              description: A list of users
              content:
                application/json:
                  schema:
                    type: array
                    items:
                      $ref: '#/components/schemas/User'
      /users/{id}:
        get:
          summary: Retrieve a user by ID
          parameters:
            - in: path
              name: id
              required: true
              schema:
                type: string
          responses:
            '200':
              description: A single user
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/User'
    components:
      schemas:
        User:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
            email:
              type: string
    ```
    **Practical Use Case:**
    Well-documented APIs make it easier for developers to understand and use your API, leading to better adoption and fewer errors.

    **Assignment:**
    - Create an OpenAPI (Swagger) documentation file for your API. Use Swagger Editor or Swagger UI to visualize and test the API documentation.
    """)

    # Versioning
    st.header("Versioning")
    st.write("""
    **Explanation:**
    API versioning ensures that changes to the API do not break existing clients. It allows developers to make updates and improvements while maintaining backward compatibility.

    - **URL Versioning**: Include the version in the URL path (e.g., `/api/v1/users`).
    - **Header Versioning**: Specify the version in request headers (e.g., `Accept: application/vnd.myapi.v1+json`).
    - **Query Parameter Versioning**: Include the version as a query parameter (e.g., `/api/users?version=1`).

    **Example Code:**
    ```javascript
    // URL versioning example
    app.get('/api/v1/users', (req, res) => {
      // Handle version 1 of the users endpoint
    });

    app.get('/api/v2/users', (req, res) => {
      // Handle version 2 of the users endpoint
    });
    ```
    **Practical Use Case:**
    Versioning helps manage changes in the API and ensures that clients using older versions are not affected by updates.

    **Assignment:**
    - Implement API versioning in your Express.js application. Create multiple versions of an endpoint and ensure that each version works independently.
    """)

    # Rate Limiting
    st.header("Rate Limiting")
    st.write("""
    **Explanation:**
    Rate limiting controls the number of requests a client can make to your API within a specified time period. It prevents abuse and ensures fair usage.

    - **Token Bucket Algorithm**: Allows for bursts of traffic but enforces a limit over time.
    - **Leaky Bucket Algorithm**: Processes requests at a constant rate and queues excess requests.

    **Example Code:**
    ```javascript
    const rateLimit = require('express-rate-limit');

    // Create a rate limiter
    const limiter = rateLimit({
      windowMs: 15 * 60 * 1000, // 15 minutes
      max: 100 // Limit each IP to 100 requests per windowMs
    });

    // Apply rate limiting to all routes
    app.use(limiter);
    ```
    **Practical Use Case:**
    Rate limiting protects your API from being overwhelmed by too many requests, ensuring it remains available and responsive.

    **Assignment:**
    - Implement rate limiting in your Express.js application. Test the rate limiter to ensure it restricts the number of requests as configured.
    """)

    # API Security
    st.header("API Security")
    st.write("""
    **Explanation:**
    Securing your API is essential to prevent unauthorized access and protect sensitive data.

    - **Authentication and Authorization**: Ensure that users are who they say they are and that they have permission to access resources.
    - **Input Validation**: Validate and sanitize inputs to prevent injection attacks.
    - **HTTPS**: Use HTTPS to encrypt data transmitted between the client and server.
    - **CORS**: Configure Cross-Origin Resource Sharing (CORS) to control which domains can access your API.

    **Example Code:**
    ```javascript
    const cors = require('cors');

    // Enable CORS for specific origins
    app.use(cors({
      origin: 'https://example.com',
      methods: 'GET,POST,PUT,DELETE'
    }));

    // Secure API with HTTPS (in production)
    const https = require('https');
    const fs = require('fs');

    const options = {
      key: fs.readFileSync('path/to/your/private.key'),
      cert: fs.readFileSync('path/to/your/certificate.crt')
    };

    https.createServer(options, app).listen(443, () => {
      console.log('Server running on port 443');
    });
    ```
    **Practical Use Case:**
    API security measures ensure that your API is protected against unauthorized access and attacks, safeguarding user data and application integrity.

    **Assignment:**
    - Implement security features in your API, including HTTPS, input validation, CORS, and proper authentication/authorization. Test your API for security vulnerabilities.
    """)

def main():
    st.title("API Design and Documentation Exploration")
    show()

if __name__ == "__main__":
    main()
