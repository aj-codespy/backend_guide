import streamlit as st

def show():
    # Title
    st.title("JavaScript Fundamentals: In-depth Exploration")

    # 1. Understanding Promises
    st.header("1. Understanding Promises")
    st.subheader("Explanation:")
    st.write("""
    Promises are objects that represent the eventual completion (or failure) of an asynchronous operation. 
    They allow you to write asynchronous code that is easier to read and maintain compared to callbacks.

    **States of a Promise:**
    - **Pending**: The initial state, neither fulfilled nor rejected.
    - **Fulfilled**: The operation was completed successfully.
    - **Rejected**: The operation failed.
    """)

    st.subheader("Example:")
    st.code("""
    let promise = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Success!");
        }, 2000);
    });

    // Consuming the promise
    promise
      .then((message) => {
        console.log(message); // Success!
      })
      .catch((error) => {
        console.error(error);
      });
    """, language='javascript')

    st.subheader("Practical Use Case:")
    st.write("Use promises for tasks like reading a file, fetching data from an API, or waiting for user input in a web application.")

    st.subheader("Assignment:")
    st.write("Create a promise that simulates a network request. It should resolve if the request is successful and reject if there is an error.")

    # 2. Async/Await
    st.header("2. Async/Await")
    st.subheader("Explanation:")
    st.write("""
    Async/await is syntactic sugar built on top of Promises. It allows you to write asynchronous code in a synchronous-looking fashion. 
    An async function returns a promise, and `await` pauses the execution of the function until the promise is resolved or rejected.
    """)

    st.subheader("Example:")
    st.code("""
    async function fetchData() {
      try {
        let response = await fetch('https://api.example.com/data');
        let data = await response.json();
        console.log(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }

    fetchData();
    """, language='javascript')

    st.subheader("Practical Use Case:")
    st.write("Async/await makes handling asynchronous tasks in sequence much more readable, like fetching data from an API and processing it immediately.")

    st.subheader("Assignment:")
    st.write("Convert a promise-based function (like reading a file) to use async/await. Handle both success and error cases.")

    # 3. Event Loop
    st.header("3. Event Loop")
    st.subheader("Explanation:")
    st.write("""
    The Event Loop allows JavaScript to perform non-blocking operations, despite being single-threaded. 
    It continuously checks the call stack and the callback queue to determine what to execute.
    """)

    st.subheader("Example:")
    st.code("""
    console.log('Start');

    setTimeout(() => {
      console.log('Callback');
    }, 2000);

    console.log('End');
    """, language='javascript')

    st.subheader("Practical Use Case:")
    st.write("Understanding the event loop is crucial for writing performant and non-blocking applications, particularly when dealing with I/O operations.")

    st.subheader("Assignment:")
    st.write("Write code that uses setTimeout and explain why the event loop causes certain operations to happen in the order they do. Draw a flowchart of the process.")

    # 4. Callbacks
    st.header("4. Callbacks")
    st.subheader("Explanation:")
    st.write("""
    Callbacks are functions passed as arguments to other functions. They are executed after the completion of some asynchronous operation.
    """)

    st.subheader("Example:")
    st.code("""
    function fetchData(callback) {
      setTimeout(() => {
        callback('Data fetched');
      }, 2000);
    }

    function printData(data) {
      console.log(data);
    }

    fetchData(printData);
    """, language='javascript')

    st.subheader("Practical Use Case:")
    st.write("Callbacks were the traditional way of handling asynchronous operations before Promises and async/await.")

    st.subheader("Assignment:")
    st.write("Write a function that performs a calculation after 2 seconds and uses a callback to return the result. Chain multiple callbacks together to simulate a multi-step process.")

    # Theoretical Questions
    st.header("Theoretical Questions")
    st.write("""
    1. Explain the difference between a promise and a callback.
    2. Why do we use async/await instead of promises?
    3. Describe the event loop and how it manages asynchronous operations in JavaScript.
    4. What is the difference between synchronous and asynchronous code?
    5. How does the event loop handle promises vs. callbacks?
    """)
