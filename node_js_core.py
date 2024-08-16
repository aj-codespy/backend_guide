import streamlit as st

def show():
    # Title
    st.title("Node.js Core: In-depth Exploration")

    # 1. Setting up a Node.js Project (package.json)
    st.header("1. Setting up a Node.js Project (package.json)")
    st.subheader("Explanation:")
    st.write("""
    `package.json` is the heart of any Node.js project. It holds metadata about the project, including dependencies, scripts, and versioning.

    **Metadata**: Project name, version, description, author, license.  
    **Dependencies**: Lists of libraries your project needs to function (npm install automatically adds these to package.json).  
    **Scripts**: Custom commands to automate tasks like starting the server, running tests, or building your application.
    """)

    st.subheader("Example:")
    st.code("""
    {
      "name": "my-node-project",
      "version": "1.0.0",
      "description": "A simple Node.js project",
      "main": "index.js",
      "scripts": {
        "start": "node index.js",
        "test": "echo 'Error: no test specified' && exit 1"
      },
      "dependencies": {
        "express": "^4.17.1"
      }
    }
    """, language='json')

    st.subheader("Practical Use Case:")
    st.write("`package.json` allows for streamlined project management, ensuring all developers have the same dependencies and project setup.")

    st.subheader("Assignment:")
    st.write("Create a basic Node.js project and initialize it with `npm init`. Add at least one dependency (like Express) and create a script to start your server.")

    # 2. Modules and the require/import System
    st.header("2. Modules and the require/import System")
    st.subheader("Explanation:")
    st.write("""
    Modules in Node.js allow you to organize your code into reusable blocks. Node.js uses the CommonJS module system, where `require()` is used to import modules.

    - **Built-in Modules**: Like fs, http, and path.  
    - **Third-party Modules**: Installed via npm, like express or mongoose.  
    - **User-created Modules**: Custom code split into separate files.
    """)

    st.subheader("Example:")
    st.code("""
// Exporting a module (math.js)
module.exports.add = (a, b) => a + b;

// Importing a module (app.js)
const math = require('./math');
console.log(math.add(2, 3)); // Output: 5
""", language='javascript')

    st.subheader("Practical Use Case:")
    st.write("Modularizing code improves maintainability, testability, and reusability.")

    st.subheader("Assignment:")
    st.write("Create a small module that exports multiple functions (like math operations), then import and use it in another file.")

    # 3. File System (fs module)
    st.header("3. File System (fs module)")
    st.subheader("Explanation:")
    st.write("""
    The `fs` module allows you to interact with the file system, such as reading, writing, and deleting files.

    - **Synchronous Methods**: Block the execution of subsequent code until the file operation completes.  
    - **Asynchronous Methods**: Use callbacks or promises to handle file operations without blocking.
    """)

    st.subheader("Example:")
    st.code("""
    const fs = require('fs');

    // Asynchronous file reading
    fs.readFile('example.txt', 'utf8', (err, data) => {
      if (err) throw err;
      console.log(data);
    });

    // Synchronous file reading
    const dataSync = fs.readFileSync('example.txt', 'utf8');
    console.log(dataSync);
    """, language='javascript')

    st.subheader("Practical Use Case:")
    st.write("The `fs` module is essential for tasks like reading configuration files, logging, and storing/retrieving data.")

    st.subheader("Assignment:")
    st.write("Write a program that reads a file asynchronously, then appends some content to it, and finally reads the updated file synchronously.")

    # 4. Event-driven Architecture
    st.header("4. Event-driven Architecture")
    st.subheader("Explanation:")
    st.write("""
    Node.js is designed to be event-driven, meaning actions are triggered by events (e.g., HTTP requests, file changes). The `EventEmitter` class allows you to create and handle custom events.
    """)

    st.subheader("Example:")
    st.code("""
    const EventEmitter = require('events');

    class MyEmitter extends EventEmitter {}

    const myEmitter = new MyEmitter();
    myEmitter.on('event', () => {
      console.log('An event occurred!');
    });

    myEmitter.emit('event');
    """, language='javascript')

    st.subheader("Practical Use Case:")
    st.write("Event-driven architecture is fundamental to building efficient, non-blocking applications like servers that respond to HTTP requests.")

    st.subheader("Assignment:")
    st.write("Create a custom event emitter that emits different types of events (like success or error) and handles them accordingly.")

    # 5. Streams and Buffers
    st.header("5. Streams and Buffers")
    st.subheader("Explanation:")
    st.write("""
    Streams are used to handle reading or writing data piece by piece, rather than all at once. Buffers are temporary memory chunks that hold binary data before it's processed.

    - **Readable Streams**: Read data (e.g., file, HTTP request).  
    - **Writable Streams**: Write data (e.g., file, HTTP response).  
    - **Duplex/Transform Streams**: Both read and write data (e.g., zipping data).
    """)

    st.subheader("Example:")
    st.code("""
    const fs = require('fs');
    const readStream = fs.createReadStream('largefile.txt', 'utf8');
    const writeStream = fs.createWriteStream('output.txt');

    readStream.on('data', (chunk) => {
      console.log('Chunk received:', chunk);
      writeStream.write(chunk);
    });
    """, language='javascript')

    st.subheader("Practical Use Case:")
    st.write("Streams are essential for handling large amounts of data, such as files or network data, without overwhelming the memory.")

    st.subheader("Assignment:")
    st.write("Use streams to read a large text file, process each chunk, and write it to another file.")

    # Theoretical Questions
    st.header("Theoretical Questions")
    st.write("""
    1. What are the key differences between synchronous and asynchronous methods in Node.js, particularly when working with the file system?  
    2. Explain the concept of event-driven architecture and how it relates to Node.js.  
    3. What is the purpose of package.json, and how does it help manage Node.js projects?  
    4. Why are streams beneficial when dealing with large files or data?  
    5. How does the CommonJS module system (require) work, and what are its key components?
    """)
