Role-Based Access Control (RBAC) System with Post Management
This project is a Django-based web application implementing a Role-Based Access Control (RBAC) system. The application has three main user roles: Admin, Moderator, and User, each with distinct permissions. The system also supports user authentication, post creation, and role-specific dashboards.

Features
1. User Authentication
      Signup: Users can create accounts by providing necessary details.
      Login: Users log in with their credentials.
      Logout: Users can log out to terminate their session.
2. Role-Based Dashboards
      Admin Dashboard
        View all users in a tabular format, including their roles.
        View all posts created by users, including post titles, content, and authors.
        Manage and supervise all data.
      Moderator Dashboard
        View all users (admins, moderators, and regular users) in a tabular format.
        Focus on role-based management without edit permissions.
      User Dashboard
        View all posts created by all users in a simplified format.
        Create new posts.
        View their post history and details.
3. Post Management
      Post Creation: Users can create posts with a title and content.
      Post Viewing: All users can view posts created by others.
      Post Attribution: Each post displays the author who created it.
   
4. Use this command to install:
pip install django
pip install mysqlclient
python manage.py makemigrations
python manage.py migrate
Make sure to add username and password for the mysql database connection


6. Start the Development Server
python manage.py runserver


How to Use the Application	
Signup:	Navigate to /signup/ to create an account. Provide a username, email, password, and role.
Login:	Navigate to /login/ to log in with your credentials. Redirects to the appropriate dashboard based on the user role.
Admin Dashboard:	Accessible to users with the role Admin. View all users and posts in tabular format.
Moderator Dashboard:	Accessible to users with the role Moderator. View all users categorized by role.
User Dashboard:	Accessible to users with the role User. View all posts and create new ones.
