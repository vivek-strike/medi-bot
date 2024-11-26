### MediBot – A Disease Prediction Model
MediBot is a web-based application that predicts diseases based on user-inputted symptoms. Built using Python and Django, MediBot leverages machine learning to provide users with reliable health insights and guides them toward the nearest medical facilities for effective treatment.

________________________________________
### 🚀 Features

- **Symptom-Based Disease Prediction:**
Users can input their symptoms, and MediBot predicts potential diseases using the K-Nearest Neighbors (KNN) algorithm.
- **User-Friendly Web Interface:**
The application features an intuitive and interactive interface for effortless user navigation.
- **Hospital Locator:**
Suggests nearby hospitals where the predicted disease can be treated effectively.
- **Doctor Availability & Booking:**
Displays a list of available doctors and allows users to book consultations directly through the platform.

________________________________________

### 🛠️ Technologies Used
**Frameworks & Libraries**
•	Backend: Python (Django Framework)
•	Frontend: HTML, CSS, JavaScript

**Machine Learning**
•	Algorithms: K-Nearest Neighbors (KNN), Random Forest Classifier, Decision Tree Classifier

**Database Tools**
•	Database: SQLite (default for Django)

________________________________________

### 📦 Installation

**Clone the Repository**

`git clone https://github.com/vivek-strike/medi-bot.git `
 
**Open file in Visual Studio Code**
For a smooth development experience, open the project folder in VS Code

**Ensure the following are installed on your system:**

1. Python: Version 3.12 or higher
2. Django: Web framework
3. Libraries: pandas, numpy, scikit-learn
4. VS Code: Recommended IDE for development

**Install Required Libraries:**

- `pip install django  `
- `pip install pandas  `
- `pip install numpy  `
-  `pip install scikit-learn `  

**Run the Server:**

-  `python manage.py runserver  `

________________________________________

### 🔐 Role-Based Access Control (RBAC)
MediBot is based on Role-Based Access Control (RBAC), which helps manage user permissions by assigning roles to each user. This ensures that users only have access to the features and resources they are authorized to use.

1. **Admin Role:**  Has full access to manage the platform, including adding and managing hospitals, doctors, users, and other administrative duties.
2. **User Role:**  Provides access to the website’s disease prediction features and general data about nearby hospitals and available doctors, but without administrative privileges.

RBAC enhances security by enforcing strict control over what users can view or modify based on their assigned roles.

________________________________________
### 📝 User Login and Account Creation

To access the MediBot platform, users can create an account and log in to utilize the disease prediction features, symptom checkers, and more.
________________________________________
### 🔑 Temporary Admin Access
The MediBot application provides both an administration panel for managing backend data and a website section for adding key resources such as hospitals and doctors. The below-provided login credential cannot modify user or admin duties or functions(only can view)

**Login Credentials:**
```
Username: TESTADMIN
Password: #10ADMIN10#
```

**1. Access the Website Section**
After logging in with the admin credentials, users can explore and manage the website’s functionalities, including:

- Adding Hospitals
- Adding Doctors

These actions are available through the main website interface, allowing for easy management of key resources.

**2. Access the Admin Panel**
To manage more advanced features like symptom-disease mappings, user records, and other administrative tasks:

- URL: Append **`/admin`** to the generated URL (e.g., http://127.0.0.1:8000/admin).

________________________________________
### 📸 Screenshots

![image](https://github.com/user-attachments/assets/dfbc962d-9251-4290-9d96-c064b4a15d9d)
![image](https://github.com/user-attachments/assets/bbf0f2cc-45e5-4d55-a6f2-fa626e303379)
![image](https://github.com/user-attachments/assets/1af254ed-d248-4c7f-83be-0e1a38500866)
![image](https://github.com/user-attachments/assets/5e681dce-37ee-4d67-9661-6022cbb810f2)
![image](https://github.com/user-attachments/assets/90734b1b-6328-4f78-84be-7a1e00015c13)
![image](https://github.com/user-attachments/assets/6678fcd3-4f2b-45be-a850-a4592b14d3bf)

________________________________________
### 🤝 Contributing
**Contributions are welcome!**
For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.
________________________________________
Created by **_Vivek T M_**
