import streamlit as st

def show():
    # Title of the app
    st.title("Database Basics: In-depth Exploration")

    # Section 1: Connecting to a Database
    st.header("1. Connecting to a Database")
    st.subheader("Explanation")
    st.write("""
    Connecting to a database is the first step in enabling your Node.js application to persist data. Depending on your project requirements, 
    you might choose either a relational database (SQL) or a NoSQL database.
    """)
    st.write("""
    - **Relational Databases (SQL)**: Examples include MySQL and PostgreSQL. These databases use structured data stored in tables with defined relationships between them.
    - **NoSQL Databases**: Examples include MongoDB. These databases are more flexible and store unstructured or semi-structured data in formats like documents, key-value pairs, or graphs.
    """)

    # Display code snippets for MySQL and MongoDB connection examples
    st.subheader("Example: MySQL Connection")
    st.code("""
    const mysql = require('mysql');

    // Create connection
    const connection = mysql.createConnection({
      host: 'localhost',
      user: 'root',
      password: '',
      database: 'my_database'
    });

    // Connect to the database
    connection.connect((err) => {
      if (err) throw err;
      console.log('Connected to the MySQL database');
    });
    """, language="javascript")

    st.subheader("Example: MongoDB Connection")
    st.code("""
    const mongoose = require('mongoose');

    // Connect to the MongoDB database
    mongoose.connect('mongodb://localhost/my_database', {
      useNewUrlParser: true,
      useUnifiedTopology: true
    }).then(() => {
      console.log('Connected to MongoDB');
    }).catch(err => {
      console.error('Connection failed', err);
    });
    """, language="javascript")

    st.subheader("Practical Use Case")
    st.write("You'll need to connect to a database for most applications, whether you're saving user data, orders, posts, or any other type of information.")

    st.subheader("Assignment")
    st.write("Set up a connection to either a MySQL or MongoDB database in a Node.js project. Write a basic function that inserts a record into the database and retrieves it.")

    # Divider for separation
    st.markdown("---")

    # Section 2: Basic CRUD Operations
    st.header("2. Basic CRUD Operations")
    st.subheader("Explanation")
    st.write("""
    CRUD stands for **Create**, **Read**, **Update**, and **Delete**. These are the fundamental operations for interacting with a database.
    """)

    # Display code snippets for SQL and MongoDB CRUD operations
    st.subheader("Example: SQL CRUD Operations")
    st.code("""
    const mysql = require('mysql');
    const connection = mysql.createConnection({ /* config */ });

    // Create a new record
    connection.query('INSERT INTO users (name, age) VALUES (?, ?)', ['John', 30], (err, result) => {
      if (err) throw err;
      console.log('User added');
    });

    // Read records
    connection.query('SELECT * FROM users', (err, results) => {
      if (err) throw err;
      console.log(results);
    });

    // Update a record
    connection.query('UPDATE users SET age = ? WHERE id = ?', [35, 1], (err, result) => {
      if (err) throw err;
      console.log('User updated');
    });

    // Delete a record
    connection.query('DELETE FROM users WHERE id = ?', [1], (err, result) => {
      if (err) throw err;
      console.log('User deleted');
    });
    """, language="javascript")

    st.subheader("Example: MongoDB CRUD Operations")
    st.code("""
    const mongoose = require('mongoose');

    // Define a User model
    const User = mongoose.model('User', new mongoose.Schema({
      name: String,
      age: Number
    }));

    // Create a new user
    const user = new User({ name: 'John', age: 30 });
    user.save().then(() => console.log('User added'));

    // Read users
    User.find().then(users => console.log(users));

    // Update a user
    User.updateOne({ name: 'John' }, { age: 35 }).then(() => console.log('User updated'));

    // Delete a user
    User.deleteOne({ name: 'John' }).then(() => console.log('User deleted'));
    """, language="javascript")

    st.subheader("Practical Use Case")
    st.write("CRUD operations allow your application to interact with the database by creating new records, retrieving them for display, updating them, or removing them as needed.")

    st.subheader("Assignment")
    st.write("Implement full CRUD functionality in your Node.js app for a simple resource (e.g., users, products) using either MySQL or MongoDB. Build routes in Express.js to perform these operations via HTTP methods.")

    # More sections for querying data, indexing, and data modeling...

    # Theoretical Questions
    st.header("Theoretical Questions")
    st.write("""
    1. Compare SQL and NoSQL databases. What are the advantages and disadvantages of each?
    2. Explain the purpose of indexing in databases and how it can improve query performance.
    3. What are the key differences between CRUD operations in SQL and NoSQL databases?
    4. Why is data modeling important, and how does it differ between SQL and NoSQL?
    5. What are the trade-offs of using an unstructured data model in MongoDB versus a structured model in MySQL?
    """)
