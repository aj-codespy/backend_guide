import streamlit as st

def show():
    # Title and Introduction
    st.title('Deployment and CI/CD: In-depth Exploration')
    st.write("This guide provides an in-depth exploration of deployment and CI/CD (Continuous Integration and Continuous Deployment).")

    # 1. Deployment
    st.header('1. Deployment')
    st.write("""
    Deployment involves releasing your application into a production environment where it can be accessed by users. It includes tasks like setting up servers, configuring environments, and managing application releases.

    **Deployment Strategies**:
    - **Blue-Green Deployment**: Maintain two environments (blue and green). One is live (blue), and the other is idle (green). Deploy the new version to the idle environment and switch traffic to it once the deployment is successful.
    - **Rolling Deployment**: Gradually update instances of your application. This approach minimizes downtime and allows you to roll back if issues arise.
    - **Canary Deployment**: Release the new version to a small subset of users first, then gradually roll it out to the rest of the users.

    **Example: Deploying a Node.js app using PM2 and Nginx**

    1. **Install PM2**:
    ```bash
    npm install pm2 -g
    ```
    2. **Start your application with PM2**:
    ```bash
    pm2 start app.js --name "my-app"
    ```
    3. **Install and configure Nginx**:
    ```bash
    sudo apt update
    sudo apt install nginx
    ```
    4. **Configure Nginx**:
    ```nginx
    server {
        listen 80;
        server_name yourdomain.com;
        location / {
            proxy_pass http://localhost:3000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    ```
    5. **Reload Nginx**:
    ```bash
    sudo systemctl reload nginx
    ```
    """)

    st.subheader('Practical Use Case')
    st.write("""
    Proper deployment ensures that your application is available and functional for end-users. Deployment strategies help manage releases and minimize downtime.
    """)

    st.subheader('Assignment')
    st.write("""
    - Deploy a Node.js application using PM2 and Nginx. Implement a deployment strategy (e.g., blue-green or rolling deployment) and test it.
    """)

    # 2. Continuous Integration (CI)
    st.header('2. Continuous Integration (CI)')
    st.write("""
    Continuous Integration (CI) involves automatically building and testing your code every time changes are made. It helps detect issues early and ensures that new code integrates smoothly with existing code.

    **CI Tools**: Use tools like **Jenkins**, **Travis CI**, **CircleCI**, or **GitHub Actions**.

    **CI Workflow**:
    1. Code is pushed to the repository.
    2. CI server detects changes and triggers a build.
    3. Tests are run to verify the code.
    4. Build artifacts are created and stored.

    **Example with GitHub Actions**

    1. **Create a `.github/workflows/ci.yml` file**:
    ```yaml
    name: Node.js CI

    on:
      push:
        branches: [main]

    jobs:
      build:

        runs-on: ubuntu-latest

        steps:
        - name: Checkout code
          uses: actions/checkout@v2

        - name: Set up Node.js
          uses: actions/setup-node@v2
          with:
            node-version: '14'

        - name: Install dependencies
          run: npm install

        - name: Run tests
          run: npm test
    ```
    2. **Push the changes to GitHub**:
    ```bash
    git add .github/workflows/ci.yml
    git commit -m "Add CI workflow"
    git push
    """
    )

    st.subheader('Practical Use Case')
    st.write("""
    CI ensures that code changes are continuously tested, helping to identify integration issues early and maintain code quality.
    """)

    st.subheader('Assignment')
    st.write("""
    - Set up a CI workflow using GitHub Actions (or another CI tool). Configure it to build and test your Node.js application on each push to the repository.
    """)

    # 3. Continuous Deployment (CD)
    st.header('3. Continuous Deployment (CD)')
    st.write("""
    Continuous Deployment (CD) extends CI by automatically deploying code changes to production after passing tests. It allows for frequent releases and ensures that updates are delivered to users quickly.

    **CD Tools**: Use tools like **Jenkins**, **GitLab CI/CD**, **AWS CodePipeline**, or **Azure DevOps**.

    **CD Workflow**:
    1. Code changes pass CI tests.
    2. Changes are automatically deployed to staging or production environments.
    3. Monitoring and rollback mechanisms are in place to handle issues.

    **Example with GitHub Actions and Heroku**

    1. **Create a `.github/workflows/deploy.yml` file**:
    ```yaml
    name: Deploy to Heroku

    on:
      push:
        branches: [main]

    jobs:
      deploy:

        runs-on: ubuntu-latest

        steps:
        - name: Checkout code
          uses: actions/checkout@v2

        - name: Set up Node.js
          uses: actions/setup-node@v2
          with:
            node-version: '14'

        - name: Install dependencies
          run: npm install

        - name: Deploy to Heroku
          uses: akshnz/heroku-deploy-action@v2
          with:
            api-key: ${{ secrets.HEROKU_API_KEY }}
            app-name: your-heroku-app-name
    ```
    2. **Add Heroku API key to GitHub secrets**.
    3. **Push the changes to GitHub**:
    ```bash
    git add .github/workflows/deploy.yml
    git commit -m "Add CD workflow"
    git push
    """
    )

    st.subheader('Practical Use Case')
    st.write("""
    CD automates the deployment process, allowing you to release updates quickly and frequently while minimizing manual intervention.
    """)

    st.subheader('Assignment')
    st.write("""
    - Set up a CD workflow using GitHub Actions (or another CD tool) to deploy your Node.js application to a cloud platform like Heroku. Ensure that the deployment is triggered automatically after successful tests.
    """)

    # 4. Infrastructure as Code (IaC)
    st.header('4. Infrastructure as Code (IaC)')
    st.write("""
    Infrastructure as Code (IaC) involves managing and provisioning infrastructure through code, enabling automation and consistency in environment setup.

    **IaC Tools**: Use tools like **Terraform**, **AWS CloudFormation**, or **Ansible**.

    **Benefits**: IaC ensures reproducibility, reduces configuration drift, and simplifies infrastructure management.

    **Example with Terraform**

    1. **Create a `main.tf` file**:
    ```hcl
    provider "aws" {
      region = "us-west-2"
    }

    resource "aws_instance" "example" {
      ami           = "ami-0c55b159cbfafe1f0"
      instance_type = "t2.micro"
    }
    ```
    2. **Initialize and apply Terraform configuration**:
    ```bash
    terraform init
    terraform apply
    """
    )

    st.subheader('Practical Use Case')
    st.write("""
    IaC allows you to manage infrastructure through code, making it easier to deploy, update, and maintain your infrastructure consistently.
    """)

    st.subheader('Assignment')
    st.write("""
    - Create an IaC configuration using Terraform (or another IaC tool) to provision a simple AWS EC2 instance. Test the deployment and management of the instance through your IaC scripts.
    """)

    # 5. Monitoring and Logging
    st.header('5. Monitoring and Logging')
    st.write("""
    Monitoring and logging are essential for tracking the performance and health of your application. They help detect issues, understand user behavior, and ensure application stability.

    **Monitoring Tools**: Use tools like **Prometheus**, **Grafana**, or **New Relic**.
    **Logging Tools**: Use tools like **Loggly**, **ELK Stack (Elasticsearch, Logstash, Kibana)**, or **Winston**.

    **Example with Winston**

    1. **Install Winston**:
    ```bash
    npm install winston
    ```
    2. **Configure Winston logging**:
    ```javascript
    const winston = require('winston');

    const logger = winston.createLogger({
      level: 'info',
      format: winston.format.json(),
      transports: [
        new winston.transports.Console(),
        new winston.transports.File({ filename: 'app.log' })
      ],
    });

    // Usage
    logger.info('Application started');
    """
    )

    st.subheader('Practical Use Case')
    st.write("""
    Monitoring and logging provide insights into your application's performance and behavior, helping you maintain its health and quickly address issues.
    """)

    st.subheader('Assignment')
    st.write("""
    - Set up monitoring and logging for your Node.js application using Winston or another logging tool. Implement monitoring to track key metrics and set up alerts for potential issues.
    """)

    # Theoretical Questions
    st.header('Theoretical Questions')
    st.write("""
    1. What are the different deployment strategies, and when would you use each?
    2. Describe the purpose of Continuous Integration (CI) and how it benefits the development process.
    3. How does Continuous Deployment (CD) extend CI, and what are its advantages?
    4. Explain the concept of Infrastructure as Code (IaC) and its benefits for managing infrastructure.
    5. Why is monitoring and logging important, and how do they contribute to application stability?
    """)

# To display the content, call the show function
if __name__ == "__main__":
    show()
