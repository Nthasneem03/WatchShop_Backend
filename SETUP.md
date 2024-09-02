# Setup Instructions
  To set up and run the WatchShop backend locally, follow these steps:
  
1. **Clone the Repository**
     Clone the WatchShop backend repository to your local machine:
     ```bash
     git clone https://github.com/Nthasneem03/WatchShop_Backend.git
     ````
  
2. **Navigate to the Project Directory**
      Go to the directory where you have cloned the project:
      ```bash
     cd WatchShop_Backend
      ```
  
  
3. **Create a Virtual Environment**
      Set up a virtual environment to manage dependencies. You can create a virtual environment by using a Python virtual environment tool of your choice. For example, to create a virtual environment named `env`,       you   would run:
      ```bash
       python -m venv env
      ```
  
  
  
4. **Activate the Virtual Environment**
        Once the virtual environment is created, activate it to start using it.
    - On Windows:
        ```
        .\env\Scripts\activate
        ```
     - On macOS and Linux:
        ```
        source env/bin/activate
        ```
  
  
5. **Install Dependencies**
      Install the required Python packages using the `requirements.txt` file:
      ```bash
      pip install -r requirements.txt
      ```
  
6. **Apply Migrations**
      Run migrations to set up the database schema:
      ```bash
        python manage.py migrate
      ```
  
  
7. **Run the Development Server**
      Start the Django development server to run the backend:
      ```bash
      python manage.py runserver
      ```
  
8. **Access the Application**
      Once the server is running, you can access the application in your web browser at `http://127.0.0.1:8000/`.

9. **Using the API Endpoints**
     For detailed information on how to interact with the API, including endpoints for getting and creating watch data, refer to the [API Documentation](API_DOCUMENTATION.md).

  
By following these steps, you will have the WatchShop backend set up and running locally.


