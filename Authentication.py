import streamlit as st

# Function to display all authentication concepts
def show():
    # Function to display Session-based Authentication
    def display_session_based_authentication():
        st.header("Session-based Authentication")
        st.write("""
        **Explanation:**
        Session-based authentication involves creating a session on the server side once a user logs in. 
        The server stores session data (e.g., user ID) and sends a session identifier (session ID) to the client 
        as a cookie. On subsequent requests, the client sends this cookie to the server, which uses it to retrieve session data.

        **Example Code:**
        ```javascript
        const express = require('express');
        const session = require('express-session');
        const app = express();

        // Configure session middleware
        app.use(session({
          secret: 'your_secret_key',
          resave: false,
          saveUninitialized: true,
          cookie: { secure: false } // Set to true in production with HTTPS
        }));

        app.post('/login', (req, res) => {
          // Authenticate user and store user ID in session
          req.session.userId = user.id;
          res.send('Logged in');
        });

        app.get('/profile', (req, res) => {
          if (req.session.userId) {
            res.send(`User profile for user ID ${req.session.userId}`);
          } else {
            res.status(401).send('Not authenticated');
          }
        });

        app.listen(3000, () => {
          console.log('Server running on port 3000');
        });
        ```
        **Practical Use Case:**
        Session-based authentication is commonly used for web applications to maintain user login states across multiple requests.

        **Assignment:**
        Implement a login system with session-based authentication in Express.js. Include routes for logging in, accessing a protected resource, and logging out.
        """)

    # Function to display Token-based Authentication
    def display_token_based_authentication():
        st.header("Token-based Authentication")
        st.write("""
        **Explanation:**
        Token-based authentication involves issuing a token (usually JWT—JSON Web Token) after user authentication. 
        The token is sent to the client and included in the headers of subsequent requests. The server verifies the token 
        and grants access accordingly.

        **Example Code:**
        ```javascript
        const express = require('express');
        const jwt = require('jsonwebtoken');
        const app = express();

        const SECRET_KEY = 'your_secret_key';

        // Middleware to check JWT
        function authenticateToken(req, res, next) {
          const authHeader = req.headers['authorization'];
          const token = authHeader && authHeader.split(' ')[1];

          if (token == null) return res.sendStatus(401);

          jwt.verify(token, SECRET_KEY, (err, user) => {
            if (err) return res.sendStatus(403);
            req.user = user;
            next();
          });
        }

        app.post('/login', (req, res) => {
          // Authenticate user and create a JWT
          const user = { id: 1, name: 'John Doe' }; // Example user
          const token = jwt.sign(user, SECRET_KEY);
          res.json({ token });
        });

        app.get('/profile', authenticateToken, (req, res) => {
          res.send(`User profile for ${req.user.name}`);
        });

        app.listen(3000, () => {
          console.log('Server running on port 3000');
        });
        ```
        **Practical Use Case:**
        Token-based authentication is suitable for APIs and stateless authentication, where you don't need to store session data on the server.

        **Assignment:**
        Create an Express.js application with token-based authentication using JWT. Implement routes for logging in, accessing a protected resource, and token validation.
        """)

    # Function to display OAuth
    def display_oauth():
        st.header("OAuth")
        st.write("""
        **Explanation:**
        OAuth is an open standard for authorization that allows applications to access resources on behalf of a user 
        without exposing their credentials. It’s commonly used for integrating third-party authentication providers (e.g., Google, Facebook).

        **OAuth 2.0:** The most commonly used version, which involves getting an access token from the authorization server 
        and using it to access protected resources.

        **Example Code:**
        ```javascript
        const express = require('express');
        const passport = require('passport');
        const GoogleStrategy = require('passport-google-oauth20').Strategy;
        const app = express();

        // Configure Passport.js with Google OAuth strategy
        passport.use(new GoogleStrategy({
            clientID: 'YOUR_GOOGLE_CLIENT_ID',
            clientSecret: 'YOUR_GOOGLE_CLIENT_SECRET',
            callbackURL: 'http://localhost:3000/auth/google/callback'
          },
          (accessToken, refreshToken, profile, done) => {
            // Use profile information (e.g., user ID) here
            return done(null, profile);
          }
        ));

        app.use(passport.initialize());

        // Route for initiating OAuth flow
        app.get('/auth/google', passport.authenticate('google', { scope: ['profile'] }));

        // Callback route
        app.get('/auth/google/callback', passport.authenticate('google', { session: false }), (req, res) => {
          res.send(`Hello, ${req.user.displayName}`);
        });

        app.listen(3000, () => {
          console.log('Server running on port 3000');
        });
        ```
        **Practical Use Case:**
        OAuth is ideal for applications that need to access user data from third-party services without managing user credentials.

        **Assignment:**
        Implement OAuth authentication in an Express.js application using a third-party provider like Google. Create routes for initiating authentication and handling callbacks.
        """)

    # Function to display Password Hashing
    def display_password_hashing():
        st.header("Password Hashing")
        st.write("""
        **Explanation:**
        Password hashing is a security practice that involves converting a plain text password into a hashed value 
        using a hashing algorithm. This ensures that even if the database is compromised, passwords remain secure.

        **Hashing Libraries:** Libraries like bcrypt provide robust hashing and salting mechanisms.

        **Example Code:**
        ```javascript
        const bcrypt = require('bcrypt');
        const saltRounds = 10;

        // Hashing a password
        bcrypt.hash('myPassword123', saltRounds, (err, hash) => {
          if (err) throw err;
          console.log('Hashed password:', hash);

          // Verifying a password
          bcrypt.compare('myPassword123', hash, (err, result) => {
            if (err) throw err;
            console.log('Password match:', result); // true if passwords match
          });
        });
        ```
        **Practical Use Case:**
        Hashing passwords is essential for securely storing user passwords and protecting them from unauthorized access.

        **Assignment:**
        Implement password hashing in a Node.js application using bcrypt. Create a function to hash passwords during user registration and another to verify passwords during login.
        """)

    # Function to display Security Best Practices
    def display_security_best_practices():
        st.header("Security Best Practices")
        st.write("""
        **Explanation:**
        Ensuring the security of your authentication system is critical. This involves implementing best practices 
        to prevent common vulnerabilities.

        - **Secure Cookies:** Use HTTPS and set secure and httpOnly flags on cookies.
        - **Rate Limiting:** Protect endpoints from brute-force attacks by limiting the number of requests.
        - **Input Validation:** Validate and sanitize all user inputs to prevent injection attacks.
        - **Use HTTPS:** Encrypt data transmitted between the client and server.

        **Example Code:**
        ```javascript
        const express = require('express');
        const rateLimit = require('express-rate-limit');
        const helmet = require('helmet');
        const app = express();

        // Rate limiting middleware
        const limiter = rateLimit({
          windowMs: 15 * 60 * 1000, // 15 minutes
          max: 100 // Limit each IP to 100 requests per windowMs
        });
        app.use(limiter);

        // Security headers
        app.use(helmet());

        // Secure cookies (set in production)
        app.use(session({
          secret: 'your_secret_key',
          resave: false,
          saveUninitialized: true,
          cookie: { secure: true, httpOnly: true }
        }));

        app.listen(3000, () => {
          console.log('Server running on port 3000');
        });
        ```
        **Practical Use Case:**
        Implementing security best practices ensures that your authentication system is robust against common threats and vulnerabilities.

        **Assignment:**
        Apply security best practices to your authentication system. Implement rate limiting, secure cookies, and HTTPS. Test your application for common vulnerabilities.
        """)

    # Streamlit app content
    st.title("Authentication Methods Exploration")

    st.sidebar.title("Select an Authentication Method")
    option = st.sidebar.selectbox(
        "Choose an option:",
        ["Session-based Authentication", "Token-based Authentication", "OAuth", "Password Hashing",
         "Security Best Practices"]
    )

    if option == "Session-based Authentication":
        display_session_based_authentication()
    elif option == "Token-based Authentication":
        display_token_based_authentication()
    elif option == "OAuth":
        display_oauth()
    elif option == "Password Hashing":
        display_password_hash
