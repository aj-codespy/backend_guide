import streamlit as st

def show():
    # Function to display Unit Testing
    def display_unit_testing():
        st.header("Unit Testing")
        st.write("""
        **Explanation:**
        Unit testing involves testing individual units of code (e.g., functions, methods) in isolation to ensure they work as expected. It's crucial for catching bugs early and ensuring code quality.

        - **Testing Libraries**: Use libraries like `Mocha` and `Jest` for writing and running unit tests.
        - **Assertions**: Check if the code produces expected results using assertion libraries like `Chai`.

        **Example Code with Mocha and Chai:**
        1. **Install dependencies:**
            ```bash
            npm install mocha chai --save-dev
            ```
        2. **Create a simple function to test:**
            ```javascript
            // math.js
            function add(a, b) {
              return a + b;
            }
            module.exports = add;
            ```
        3. **Write unit tests:**
            ```javascript
            // test/math.test.js
            const add = require('../math');
            const { expect } = require('chai');

            describe('Add function', () => {
              it('should add two numbers correctly', () => {
                expect(add(2, 3)).to.equal(5);
                expect(add(-1, 1)).to.equal(0);
              });
            });
            ```
        4. **Run tests:**
            ```bash
            npx mocha
            ```
        **Practical Use Case:**
        Unit tests are used to verify that individual components of your application work correctly. They are essential for ensuring that code changes do not introduce new bugs.

        **Assignment:**
        - Write unit tests for several functions in your Node.js application. Use Mocha and Chai to ensure that your functions produce the correct output for various inputs.
        """)

    # Function to display Integration Testing
    def display_integration_testing():
        st.header("Integration Testing")
        st.write("""
        **Explanation:**
        Integration testing involves testing how different parts of your application work together. It ensures that the components or services interact correctly and that integrated features work as intended.

        - **Testing Libraries**: Use libraries like `Mocha`, `Jest`, and `Supertest` for integration testing.
        - **Database Testing**: You may need to use a test database or mock the database interactions.

        **Example Code with Mocha and Supertest:**
        1. **Install dependencies:**
            ```bash
            npm install supertest --save-dev
            ```
        2. **Write integration tests:**
            ```javascript
            // test/app.test.js
            const request = require('supertest');
            const app = require('../app'); // Your Express app

            describe('GET /api/users', () => {
              it('should return a list of users', async () => {
                const response = await request(app).get('/api/users');
                expect(response.status).to.equal(200);
                expect(response.body).to.be.an('array');
              });
            });
            ```
        **Practical Use Case:**
        Integration tests ensure that your application's components work together correctly. They are essential for catching issues that might arise when different parts of the application interact.

        **Assignment:**
        - Write integration tests for your Express.js application. Test the API endpoints to ensure they interact with the database and other components as expected.
        """)

    # Function to display End-to-End (E2E) Testing
    def display_e2e_testing():
        st.header("End-to-End (E2E) Testing")
        st.write("""
        **Explanation:**
        End-to-end testing involves testing the complete flow of your application from the user’s perspective. It simulates user interactions with the application and ensures that all components work together as expected.

        - **Testing Libraries**: Use libraries like `Cypress` and `Puppeteer` for end-to-end testing.
        - **Test Scenarios**: Test common user scenarios, such as logging in, creating content, and navigating through the application.

        **Example Code with Cypress:**
        1. **Install Cypress:**
            ```bash
            npm install cypress --save-dev
            ```
        2. **Write end-to-end tests:**
            ```javascript
            // cypress/integration/login.spec.js
            describe('Login Page', () => {
              it('should log in successfully', () => {
                cy.visit('/login');
                cy.get('input[name="username"]').type('testuser');
                cy.get('input[name="password"]').type('password');
                cy.get('button[type="submit"]').click();
                cy.url().should('include', '/dashboard');
              });
            });
            ```
        3. **Run tests:**
            ```bash
            npx cypress open
            ```
        **Practical Use Case:**
        End-to-end tests ensure that your application behaves correctly from a user's perspective. They are crucial for verifying that the entire system works as intended.

        **Assignment:**
        - Write end-to-end tests for your application using Cypress. Test user flows such as registration, login, and content creation.
        """)

    # Function to display Mocking and Stubbing
    def display_mocking_stubbing():
        st.header("Mocking and Stubbing")
        st.write("""
        **Explanation:**
        Mocking and stubbing involve replacing parts of your application with mock objects or functions to isolate the unit being tested. This allows you to test code without relying on external services or complex dependencies.

        - **Mocking Libraries**: Use libraries like `sinon` for mocking and stubbing functions or services.

        **Example Code with Sinon:**
        1. **Install Sinon:**
            ```bash
            npm install sinon --save-dev
            ```
        2. **Write tests with mocks:**
            ```javascript
            // test/service.test.js
            const sinon = require('sinon');
            const { expect } = require('chai');
            const service = require('../service'); // Your service module

            describe('Service', () => {
              it('should call external API', () => {
                const apiStub = sinon.stub(service, 'fetchData').resolves('mock data');
                service.getData().then((data) => {
                  expect(data).to.equal('mock data');
                  apiStub.restore();
                });
              });
            });
            ```
        **Practical Use Case:**
        Mocking and stubbing are useful for isolating parts of your application during testing and avoiding dependencies on external systems.

        **Assignment:**
        - Use Sinon to mock external API calls or database interactions in your tests. Write tests to ensure that your application behaves correctly when interacting with these mocked components.
        """)

    # Function to display Test-Driven Development (TDD)
    def display_tdd():
        st.header("Test-Driven Development (TDD)")
        st.write("""
        **Explanation:**
        Test-Driven Development (TDD) is a development approach where tests are written before the code. This approach helps in designing the application incrementally and ensures that each piece of functionality is tested thoroughly.

        - **TDD Cycle**:
          1. Write a test for the new functionality.
          2. Write code to pass the test.
          3. Refactor the code and tests as needed.
          4. Repeat the process.

        **Example Code:**
        1. **Write a test:**
            ```javascript
            // test/add.test.js
            const add = require('../add');

            describe('Add function', () => {
              it('should return the sum of two numbers', () => {
                expect(add(1, 2)).to.equal(3);
              });
            });
            ```
        2. **Write code to pass the test:**
            ```javascript
            // add.js
            function add(a, b) {
              return a + b;
            }
            module.exports = add;
            ```
        3. **Refactor code if needed**.
        **Practical Use Case:**
        TDD ensures that code is written with a clear understanding of its requirements and is thoroughly tested, leading to higher quality and more maintainable code.

        **Assignment:**
        - Practice TDD by developing a small feature or module. Write tests first, implement the functionality, and refactor as necessary.
        """)

    # Streamlit app content
    st.title("Testing Concepts Exploration")

    st.sidebar.title("Select a Topic")
    option = st.sidebar.selectbox(
        "Choose an option:",
        ["Unit Testing", "Integration Testing", "End-to-End (E2E) Testing", "Mocking and Stubbing",
         "Test-Driven Development (TDD)"]
    )

    if option == "Unit Testing":
        display_unit_testing()
    elif option == "Integration Testing":
        display_integration_testing()
    elif option == "End-to-End (E2E) Testing":
        display_e2e_testing()
    elif option == "Mocking and Stubbing":
        display_mocking_stubbing()
    elif option == "Test-Driven Development (TDD)":
        display_tdd()
