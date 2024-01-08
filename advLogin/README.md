# Introduction

Welcome to our streamlined login and new ID creation system! This system is crafted to effectively manage user data and store it in a specialized `.json` file. What sets it apart is its dynamic ability to create a new `.json` file if one doesn't already exist.

## How It Works

### `FileAccess.py`

Operating behind the scenes, our dedicated helper, `FileAccess.py`, takes care of reading, writing, and overseeing user data within the `.json` file. Think of it as a reliable manager for our user information.

#### Class: `FileAccess`

- **Constructor:**
  - Simply provide the file path during instantiation.

- **read_data():**
  - Retrieves data from the `.json` file, which is organized as a list containing multiple dictionaries.

- **add_user(new_userID):**
  - When creating a new ID, this manager seamlessly incorporates user details into the list and saves it to the `.json` file.

## Special Feature
  - If the file path provided in the constructor does not exist, it dynamically creates and saves your data in the `.json` file.

### `main.py`

This serves as the heart of our system, utilizing the capabilities of the `FileAccess` manager to handle user interactions.

- **Initialization:**
  - `main.py` begins by importing the `FileAccess` manager and extracting data as a list of dictionaries with keys `name` and `password`.

- **Basic Login and New User ID Creation:**
  - Implements a straightforward login system to demonstrate the functionality.

That's it! Our system prioritizes simplicity and efficiency, effortlessly creating a new `.json` file when necessary while ensuring the safety of your user data. Feel free to explore and experience the seamless features of our user management system. Login, create new IDs, and enjoy the convenience it brings to your user experience.

## Contact Information

- **Twitter:** [@karnikhil90](https://twitter.com/karnikhil90)
- **Email:** [nikhilkarmakar4020@gmail.com](mailto:nikhilkarmakar4020@gmail.com)