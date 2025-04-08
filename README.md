# BooksVault
Hello! My web application, BooksVault, is a personal online library where you can add and manage the books you own at home or have stored digitally.


## Distinctiveness  
**BooksVault** stands out as a personalized online library tailored specifically for individuals who want to keep track of their own book collections. Unlike typical public or shared platforms, it focuses entirely on giving users a private, organized space to manage the books they own—whether physical or digital.

## Complexity  
Under the hood, **BooksVault** provides a structured system that allows for intuitive book entry, detailed metadata management, and seamless access across devices. It combines a clean, user-friendly interface with efficient data handling to ensure that managing even large personal collections remains smooth and scalable.



## 📄 `views.py`

This file contains all the view logic for the **BooksVault** web application. It handles routing, rendering templates, processing form data, and interacting with models. Below is an overview of the key views and their purposes:

### 🔐 Authentication Views
- **`login_view(request)`**: Authenticates users and logs them in. Handles error validation for login fields.
- **`create_account(request)`**: Handles user registration with validations for username, email, and password uniqueness.
- **`logout_view(request)`**: Logs the user out and redirects them to the login page.

### 📚 Book Management
- **`index(request)`**: Main dashboard displaying the user's books.
- **`new_book(request)`**: Handles adding a new book, including image upload to Cloudinary.
- **`edit_book(request, BookID)`**: Edits existing book information including authors and publisher.
- **`delete_book(request, BookID)`**: Deletes a book from the user’s collection.
- **`book(request, BookID)`**: Displays detailed information about a single book.

### 🔍 Searching and Filtering
- **`search(request)`**: Searches for books by name or ISBN.
- **`category(request, Category)`**: Filters books by category.

### 👤 Authors and Publishers
- **`authors(request)`**: Displays a list of authors added by the user.
- **`new_author(request)`**: Handles AJAX POST request to add a new author.
- **`author(request, AuthorID)`**: Displays author details and related books.
- **`delete_author(request, AuthorID)`**: Deletes an author and optionally their books.
  
- **`publishers(request)`**: Displays a list of publishers.
- **`new_publisher(request)`**: Handles AJAX POST request to add a new publisher.
- **`publisher(request, PublisherID)`**: Displays publisher details and related books.
- **`delete_publisher(request, PublisherID)`**: Deletes a publisher.

### 📋 Book Lists
- **`lists(request)`**: Displays all user-created book lists.
- **`new_list(request)`**: Creates a new book list with selected books.
- **`list(request, ListID)`**: Displays a specific list and its books.
- **`delete_list(request, ListID)`**: Deletes a book list.

---

Each view includes validation logic to ensure a smooth and secure experience for the user. The app heavily relies on the Django ORM for database operations and integrates **Cloudinary** for managing book cover images.


## 📄 forms.py

This file defines form classes used in the **BooksVault** application.

### UploadFileForm

This is a simple form with one field:

- **image**: A file input field used to upload images (typically book cover images). It is used in views where users add or edit books and need to upload a cover photo.

This form ensures that uploaded files are handled properly before being sent to Cloudinary for storage.


## 📄 choices.py

This file defines constant values used throughout the **BooksVault** application.

### CATEGORIES

A list of predefined book categories, each represented by a short code and a readable name. These categories help organize books by genre or subject, making it easier for users to classify and filter their personal collections.

Examples of categories include Art, Biography, Fiction, History, Romance, Science, and more. These are used in forms and views to ensure consistency and simplify user input.


## 📄 models.py

This file defines the data models for the **BooksVault** application. It contains classes representing the core entities in the application: User, Authors, Publisher, Book, and List. Each class is associated with a table in the database that stores related information.

### User

- Extends the built-in `AbstractUser` class, allowing the use of Django's authentication system while adding no additional fields for now.

### Authors

- Represents authors of books in the user's collection.
- Contains the author’s **name** and **biography**.
- Linked to a user via a foreign key, meaning each author is associated with a specific user.

### Publisher

- Represents book publishers in the user's collection.
- Contains the publisher's **name**.
- Also linked to a user via a foreign key.

### Book

- Represents a book in the user's library.
- Contains fields like **name**, **ISBN**, **category** (using predefined categories from `choices.py`), **image_url**, **authors** (a many-to-many relationship with Authors), and **publisher** (a foreign key to the Publisher model).
- Tracks when the book was **added** with an automatic timestamp.

### List

- Represents a custom list of books created by the user.
- Contains a **name** for the list and a many-to-many relationship with **books**.
- Allows users to organize books into different lists.

Each model is tied to a specific user, ensuring that the books, authors, and publishers belong to that user and are stored accordingly in the database.


## 📄 urls.py

This file contains the URL routing for the **BooksVault** application. It maps each URL path to its corresponding view function, which handles the logic for rendering pages or performing actions.

### URL Routes:

- **`/`**: Redirects to the **index** page, which shows the user's library.
- **`/search`**: A search page where users can search for books by name or ISBN.
- **`/category/<Category>`**: Displays books in a specific category, such as Fiction, History, etc.
- **`/authors`**: A page listing all authors associated with the current user.
- **`/publishers`**: A page listing all publishers associated with the current user.
- **`/lists`**: Displays all the custom book lists created by the user.

### Book Management:

- **`/new/book`**: A page to add a new book to the user's library.
- **`/edit/book/<BookID>`**: A page to edit an existing book in the library.
- **`/book/<BookID>`**: Displays details about a specific book.
- **`/delete/book/<BookID>`**: Deletes a specific book from the user's library.

### Author & Publisher Management:

- **`/new/author`**: Allows users to add a new author.
- **`/new/publisher`**: Allows users to add a new publisher.
- **`/author/<AuthorID>`**: Displays details about a specific author and their books.
- **`/publisher/<PublisherID>`**: Displays details about a specific publisher and their books.
- **`/delete/author/<AuthorID>`**: Deletes a specific author.
- **`/delete/publisher/<PublisherID>`**: Deletes a specific publisher.

### List Management:

- **`/create/new/list`**: A page to create a new book list.
- **`/list/<ListID>`**: Displays the books in a specific list.
- **`/delete/list/<ListID>`**: Deletes a specific list.

### User Authentication:

- **`/create/account`**: A page for creating a new user account.
- **`/login`**: A login page for users to authenticate.
- **`/logout`**: Logs the user out of the application.

Each URL route is linked to a specific view that handles the requested action, from displaying pages to handling form submissions or deletions.


### Templates

## 📄 layout.html

This is the base layout template used for the entire application. It provides the structure for all pages, including common header elements, navigation, and footer. Other templates (such as login, home, etc.) extend this layout and insert their own content into the body section.

### Template Structure:

1. **Head Block:**
   - The main `<head>` section of the template includes meta tags for character encoding and viewport settings for responsive design.
   - The `Global.css` file is linked for styling, with additional styles inserted through the `{% block head %}`.

2. **Body Block:**
   - The body section contains navigation and a variety of elements depending on the user’s authentication status.

### Key Elements:

- **User Authentication Check:**
  - If the user is authenticated, a navigation bar is displayed, which includes links to different sections of the site (e.g., Home, Authors, Publishers, Lists). 
  - There's also a **mobile-friendly navigation bar** for smaller screens.
  
- **Main Navigation:**
  - **For authenticated users:**
    - The "BooksVault" title is displayed, followed by links to different sections such as Home, Authors, Publishers, and Lists.
    - An icon (`optionsIcon`) opens a dropdown menu for additional options, including:
      - Add a new book.
      - Add a new author.
      - Add a new publisher.
      - Create a new list.
      - Toggle between themes (light/dark mode).
      - Log out.
      
- **Mobile Navigation:**
  - A secondary set of navigation links is available for mobile users, providing access to Home, Authors, Publishers, and Lists.
  
- **Options Menu:**
  - When clicked, the options menu becomes visible and provides the user with the ability to add new content (book, author, publisher, or list), toggle the theme, or log out.

- **Forms for Adding New Content:**
  - **Add New Author Form:** A form to input the author's name and biography.
  - **Add New Publisher Form:** A form to input the publisher's name.
  - Both forms are hidden by default and are revealed when the respective menu option is selected.

- **Block Definitions:**
  - `{% block head %}`: A placeholder to insert additional content into the head section (e.g., styles or meta tags).
  - `{% block body %}`: The main content area that will be replaced by the content from the extending template (e.g., login, homepage).

- **Global JavaScript:**
  - The template includes a link to `Global.js`, which is likely used to manage interactive elements, such as the options menu or theme toggle.

### Style:
- The layout is designed to be responsive with the mobile version of the menu and a main top-bar for larger screens. CSS classes like `main-tape`, `main-options-container`, and `mobiles-second-tape` are used to style these elements.

This layout ensures consistency across all pages and provides the necessary functionality for authenticated users to navigate the application.


## 📄 login.html

This template is responsible for rendering the login form where users can authenticate themselves to access their library account. It extends the **layout.html** template, which contains the common layout structure for the application.

### Template Structure:

1. **Head Block:**
   - The `authentication.css` stylesheet is loaded here to style the login page specifically.

2. **Body Block:**
   - The main body of the page contains the login form and other elements related to authentication.

### Key Elements:

- **Form:**
  - The form submits a **POST** request to the `login` URL, which processes the login attempt.
  - It contains two main fields:
    1. **Email Field:**
       - The `email` field is styled based on whether there’s an error (`emailE`), which triggers a red outline.
       - If there's an error with the email input, the error message is displayed below the field.
    2. **Password Field:**
       - The `password` field similarly styles the input with a red outline if there's an error (`passwordE`), and any password-related errors are displayed below the field.
  
- **Error Handling:**
  - If there's an error with either the email or password, it is displayed next to the corresponding input field in red text.

- **Account Creation Link:**
  - A link is provided at the bottom of the form, which directs users to the account creation page if they don’t have an account.

- **CSRF Token:**
  - The form includes a **CSRF token** for security purposes, to prevent cross-site request forgery attacks.

- **Background Image:**
  - An image (`online-library.png`) is shown in the background to enhance the visual appeal of the login page.

### Style:
- The page uses a specific class (`authentication-form-container`) to structure the form, and custom classes are applied for styling the inputs, error messages, and buttons.
  
This template ensures that the user has an easy, secure, and error-friendly experience when logging into their account.


## 📄 create-account.html

This template is used to create a new account for the "BooksVault" application. It contains a form where users can input their username, email, and password to create an account and access the application.

### Template Structure:

1. **Head Block:**
   - Links to `authentication.css` for styling the account creation form.

2. **Body Block:**
   - The body contains the account creation form along with error messages for invalid inputs.

### Key Sections:

#### **Account Creation Form:**

- **Form Header:**
  - The form starts with a title ("Create new library account") and a subtitle prompting users to enter their information.

- **Input Fields:**
  - **Username:**
    - A text input field for the username. If there is an error (`usernameE`), the border of the input will be red and an error message will be displayed below the field.
  - **Email:**
    - A text input field for the user's email. Similarly, if there is an error (`emailE`), the border turns red and the error message is shown.
  - **Password:**
    - A password input field. If the password input has an error (`passwordE`), the input border turns red and an error message is shown.

- **Login Link:**
  - A link to the login page for users who already have an account.

- **CSRF Token:**
  - Includes `{% csrf_token %}` to prevent CSRF attacks, ensuring security when submitting the form.

- **Submit Button:**
  - A submit button labeled "Create" to submit the form and create the account.

#### **Background Image:**
- Displays an image with the source `{% static 'imgs/online-library.png' %}` as a background image for the account creation page.

### Error Handling:

- Each input field has a conditional style applied to the border (using `outline: 1px solid red;`) if an error exists for that particular field.
- Error messages are displayed below the respective fields when a validation error is present.

### Design and Layout:

- The form is placed within a container with the class `authentication-form-container` to centralize the form on the page.
- The form elements are styled with classes like `authentication-username`, `authentication-email`, and `authentication-password` to differentiate each field.
- The page includes a background image and a responsive layout for the form elements, making it user-friendly and easy to navigate.

### JavaScript:
- No JavaScript is included in this template, but the style manipulation is handled inline within the HTML for the error states.

This template allows users to create a new account with validation feedback if any field is filled incorrectly.


## 📄 index.html

This template is the homepage of the "BooksVault" application, which provides users with the ability to search for and browse books in their personal library. It also displays an overview of the books in the collection.

### Template Structure:

1. **Head Block:**
   - Links to `index.css` for styling the homepage layout.

2. **Body Block:**
   - The body contains sections for searching books, adding new books, displaying the total number of books, and showing the books themselves.

### Key Sections:

#### **Search and Browse Books:**

- **Search Bar:**
  - Allows users to search for books by their name or ISBN.
  - A POST form sends the search query to the `search` URL.
  - Includes a search icon within the button.

- **Categories:**
  - Displays a list of book categories (from the `CATEGORIES` variable).
  - Each category is a clickable link that navigates to the respective category page.

- **Add New Book:**
  - A call-to-action section that invites users to add a new book to their collection.
  - Includes an icon and a brief description of the benefits of tracking their personal book collection.

#### **Books Overview:**

- **Total Books:**
  - Displays the total count of books in the collection (`Books.count`).

- **Display Options:**
  - Includes buttons/icons to toggle between grid and list view for displaying books.

- **Books List/Grid:**
  - A container that holds all the books available in the collection.
  - Each book is displayed in a card with the following information:
    - **Image** of the book.
    - **Name** of the book.
    - **Details** about the book (ISBN, category, authors, and publisher).
    - The book is a link that leads to its detailed page.

#### **Script:**
- Includes the `index.js` file for any JavaScript functionality related to the homepage.

### Design and Layout:
- The layout is responsive and includes a grid view for books. Users can switch between different display modes (grid or list view).
- CSS classes like `search-container`, `books-container`, and `new-book-container` are used to style the sections.
- The page uses Flexbox and CSS Grid to arrange the layout for the search bar, books, and categories.
- Each book is displayed as a clickable box with details like its ISBN, category, authors, and publisher.

This template allows users to interact with their personal book collection by searching for books, browsing by category, and adding new books easily.


## 📄 search.html

This template displays the results of a search query, showing a list of books that match the search term. It allows users to toggle between grid and list views for displaying the results.

### Template Structure:

1. **Head Block:**
   - Links to the `issuers.css` and `index.css` stylesheets for consistent page styling.

2. **Body Block:**
   - Contains the main content of the search results page, which includes the search term, number of results, and the list of matching books.

### Key Sections:

#### **Page Title:**
- **Dynamic Title:**
  - Displays the text `Search : {{ search }}`, where `{{ search }}` is the search term entered by the user.

#### **Results Count:**
- **Results Display:**
  - Shows the number of books found that match the search query using `{{ Books.count }}`.

#### **Display Mode (Grid/List View):**
- **Toggle View:**
  - Provides two icons to toggle between grid view and list view for the books. 
  - The grid view icon displays books in a grid layout, while the list view icon displays them in a linear list.

#### **Books List:**
- **Books Display:**
  - A grid layout is used by default to display the books that match the search query.
  - Each book displays:
    - **Book Image:** A thumbnail of the book.
    - **Book Name:** The name of the book.
    - **Book Details:**
      - ISBN number.
      - Category.
      - Authors (multiple authors separated by commas).
      - Publisher name.
  - Each book is clickable, linking to the book's detail page at `/books/vault/book/{{ Book.id }}`.

#### **No Results Found:**
- **No Results Message:**
  - If no books are found, the message `No results` is displayed below the books container.

#### **Styling:**
- The layout is styled using `grid` by default for book listings.
- The toggle buttons for grid and list views are represented by SVG icons.

### Features:
- **Dynamic Search Term:** The search term entered by the user is dynamically displayed at the top of the page.
- **Grid/List View Toggle:** Users can toggle between grid and list views to change how the books are displayed.
- **No Results Message:** If no matching books are found, a message is displayed.
- **Book Details:** Each book displays basic information, including the book's name, ISBN, category, authors, and publisher.

### Design and Layout:
- The page uses a responsive grid layout for displaying the books and includes toggleable icons for adjusting the view mode.
- The `search` term is highlighted with a special color (`var(--special-text)`) to draw attention to the query.


## 📄 new-book.html

This template is used for adding a new book to the "BooksVault" application. Users can fill out a form to upload book details, including the book image, name, ISBN, category, authors, and publisher.

### Template Structure:

1. **Head Block:**
   - Links to `new-book.css` for styling the "Add new book" page.

2. **Body Block:**
   - Contains the form elements for adding a new book.

### Key Sections:

#### **Add New Book Form:**

- **Form Header:**
  - The form starts with a main title ("Add new book").

- **Image Upload:**
  - **Input Field:** 
    - The image input allows users to upload a book image, supporting file types such as `.jpg`, `.png`, and `.pdf`. The `input` element is hidden, and a custom label (`Book Image Upload`) is used to trigger the file selection.
    - If there is an error in the image upload (`imageE`), the border of the label turns red, and an error message is displayed.
  - **Image Preview:** 
    - Once a file is selected, the image preview is shown.

- **Book Details Inputs:**
  - **Book Name:**
    - A text input for the book's name. If there is an error (`nameE`), the input border turns red and the error message is shown.
  - **ISBN:**
    - A number input for the book's ISBN. If there is an error (`ISBNE`), the input border turns red and the error message is shown.
  - **Category:**
    - A dropdown (`<select>`) for selecting the book's category. Categories are dynamically loaded from the `CATEGORIES` context variable. If there's an error (`categoryE`), the border turns red and the error message is shown.
  - **Authors:**
    - A text input for entering authors. As users type, matching authors are shown below the input field. If the input contains errors (`authorsE`), the border turns red and an error message is displayed.
    - The list of authors is dynamically loaded from the `AUTHORS` context variable.
    - The selected authors are displayed in the `chosen-authors` container.
  - **Publisher:**
    - A dropdown (`<select>`) for selecting the publisher from the available list (`PUBLISHERS`). If there’s an error (`publisherE`), the border turns red and the error message is shown.

- **Form Submission:**
  - The form is submitted using the `POST` method, and the `enctype="multipart/form-data"` attribute allows file uploads.
  - A submit button (`Add`) is provided to add the book to the collection.

#### **JavaScript:**
- The page includes a link to `new-book.js`, which likely handles functionality such as dynamic author search, previewing the image, and managing the form submission.

### Error Handling:

- Each input field has a conditional style applied to the border (using `outline: 1px solid red;`) if an error exists for that particular field.
- Error messages are displayed below the respective fields when a validation error is present.

### Design and Layout:

- The form is laid out in two main sections: image upload and book details.
- The image upload section uses a custom label to trigger the file input, making the UI cleaner.
- The book details inputs are grouped in a container, with each field being individually styled and validated.
- The `new-book-submit` class styles the submit button to appear prominently at the bottom of the form.

### Features:

- **Dynamic Author List:** As users type in the "Authors" field, matching authors are displayed dynamically. The user can select authors, which will be added to the form input.
- **Image Upload Preview:** Once an image is selected, a preview is displayed before submission, allowing the user to confirm their upload.

This template provides a user-friendly way to add a book to the library, ensuring all necessary information is gathered, and validation is performed for a smooth user experience.


## 📄 book.html

This template displays the details of a specific book, including the book's image, name, ISBN, category, authors, and publisher. It also provides options for editing, adding to a list, or deleting the book.

### Template Structure:

1. **Head Block:**
   - Links to the `book.css` stylesheet for styling the "Book Details" page.

2. **Body Block:**
   - Contains the structure to display the book details and options for managing the book.

### Key Sections:

#### **Book Details Section:**

- **Book Image:**
  - Displays the book image using the `Book.image_url` variable, with an `alt` attribute set to the image URL for accessibility.

- **Book Information:**
  - **Book Name:** The book's name is displayed at the top of the details section (`Book.name`).
  
  - **Book Details:**
    - **Left Column:**
      - Displays labels for ISBN, Category, Authors, and Publisher.
    - **Right Column:**
      - **ISBN:** The book's ISBN number is displayed (`Book.ISBN`).
      - **Category:** The book's category is displayed using `Book.get_category_display`, which shows the human-readable category name.
      - **Authors:** A list of authors is displayed, with each author's name being a clickable link to their profile page (`/books/vault/author/{{ author.id }}`). Multiple authors are displayed separated by commas.
      - **Publisher:** The publisher's name is displayed as a clickable link to the publisher's profile page (`/books/vault/publisher/{{ Book.publisher.id }}`).

#### **Options Section:**

- **Options Icon:**
  - An SVG icon (`list-options-icon`) is used to represent the options menu for the book.
  
- **Options Container:**
  - A hidden container (`bookOptionsContainer`) contains links for:
    - **Edit:** A link to the book's edit page (`/books/vault/edit/book/{{ Book.id }}`).
    - **Add to List:** A link to add the book to a list (`/books/vault/add/book/{{ Book.id }}/to/list`).
    - **Delete:** A link to delete the book (`/books/vault/delete/book/{{ Book.id }}`).
  
- **Exit Icon:**
  - An SVG icon (`book-options-exit`) to close or exit the options menu.

#### **JavaScript:**
- The page includes a link to `book.js`, which likely handles the interactivity of the options menu, including showing and hiding the book options.

### Features:

- **Dynamic Links for Authors and Publisher:** Each author and publisher is a clickable link that leads to their respective profile page.
  
- **Book Management Options:** Users can edit, add to a list, or delete the book from the interface using the options menu.
  
- **Responsive and Interactive Design:** The options menu is interactive, allowing the user to reveal the options and perform actions on the book.

### Design and Layout:

- The layout consists of two main parts: the book image on the left and the book details on the right.
- The options for managing the book are hidden initially and can be revealed by interacting with the options icon.
- The design is clean and straightforward, allowing users to easily view and manage book information.


## 📄 edit-book.html

This template allows the user to edit the details of an existing book. It includes fields for modifying the book's name, ISBN, category, authors, publisher, and image.

### Template Structure:

1. **Head Block:**
   - Links to the `new-book.css` stylesheet for styling the edit book form.

2. **Body Block:**
   - Contains a form where the user can modify the book's information. The form submits data to the URL `/books/vault/edit/book/{{ Book.id }}` using a POST request.

### Key Sections:

#### **Edit Book Title:**

- **Main Title:**  
  Displays the title "Edit Book" followed by the current book's name (dynamic value of `Book.name`).

#### **Book Image:**

- **Image Upload:**
  - An input field (`type="file"`) allows the user to upload a new image for the book.
  - The current image is displayed by default as `{{ Book.image_url }}` within an `img` tag.

#### **Book Details Form:**

- **Book Name:**
  - The book's name is pre-filled in the form using `{{ Book.name }}`.

- **ISBN:**
  - The ISBN field is pre-filled with the current ISBN of the book (`{{ Book.ISBN }}`).

- **Category:**
  - The book's category is displayed as a dropdown (`<select>`). The options are dynamically generated from the `CATEGORIES` variable. The category of the current book is marked as selected (`{% if code == Book.category %}selected{% endif %}`).

- **Authors:**
  - This section allows the user to modify the authors of the book:
    - A hidden input field (`id="authorsValues"`) stores the selected authors.
    - A dynamic list of authors is shown (`<div class="authors-list">`), where each author is listed with the class `authors-names`. The authors who are already linked to the book are styled with the class `selected-authors`.
    - A text input (`id="authorsInput"`) is provided for searching or entering new authors.

- **Publisher:**
  - The publisher dropdown is populated dynamically from the `PUBLISHERS` variable. The current publisher is marked as selected using the condition `{% if publisher.name == Book.publisher %}selected{% endif %}`.

#### **Submit Button:**

- **Save Changes:**
  - The form has a submit button labeled "Save" which will update the book's details when clicked.

#### **JavaScript:**
- The page includes a link to the `edit-book.js` file, which likely handles the interactions within the form, such as managing the authors list and image preview.

### Features:

- **Editable Book Details:** All the fields (name, ISBN, category, authors, publisher, and image) are pre-filled with the current book's data and can be modified.
- **Image Preview:** The current book image is displayed, and the user can upload a new one.
- **Dynamic Authors List:** Authors are displayed dynamically, and the user can select or deselect authors. Existing authors for the book are highlighted.
- **Category and Publisher:** The category and publisher fields are pre-selected based on the current book's information.

### Design and Layout:

- The layout is consistent with the "Add New Book" page (`new-book.html`), providing a user-friendly interface for editing the book details.
- Form fields are clearly labeled, and the structure allows easy interaction for updating the book's information.


## 📄 category.html

This template displays the list of books belonging to a specific category. It provides options for changing the display style and shows detailed information about each book, such as ISBN, category, author, and publisher.

### Template Structure:

1. **Head Block:**
   - Links to the `issuers.css` and `index.css` stylesheets for styling the category page.

2. **Body Block:**
   - Displays the category name, a count of the books, and the list of books in that category.

### Key Sections:

#### **Category Information:**

- **Category Name:**  
  The category name is displayed with a highlighted color (`var(--special-text)`). The template uses the `Category` variable to display the category name dynamically.

- **Book Count:**  
  The number of books in the selected category is displayed as `Results : {{ Books.count }}`.

#### **Display Options:**

- **Grid/List View Switch:**
  - Two SVG icons are provided for switching between grid and list display modes. The grid view icon (`gridDisplayIcon`) and the list view icon (`listDisplayIcon`) allow the user to toggle between different layouts for displaying the books.
  
#### **Books List Section:**

- **Books Container:**
  - A container (`books-container`) holds all the books related to the selected category. It is initially set to a grid layout (`grid`) using the class `grid`. The books are displayed dynamically from the `Books` variable.

- **Book Details:**
  - Each book is displayed as a clickable box (`book-box`) that links to the book's detailed page (`/books/vault/book/{{ Book.id }}`). Each book has:
    - **Image:** The book's image is shown using the `Book.image_url` variable.
    - **Name:** The book's name is displayed (`Book.name`).
    - **Book Details:** 
      - **ISBN:** The book's ISBN number (`Book.ISBN`).
      - **Category:** The human-readable name of the book's category (`Book.get_category_display`).
      - **Authors:** A list of authors is displayed, and each author’s name is shown separated by commas. Links to the author's profile are omitted here but can be added if needed.
      - **Publisher:** The publisher's name is displayed (`Book.publisher.name`).

#### **No Results:**

- If no books are found for the selected category, a message "No results" is displayed at the bottom of the books container.

#### **JavaScript:**
- The page includes a link to `index.js`, which likely handles the interaction for switching between the grid and list views.

### Features:

- **Dynamic Book Listings:** The books are dynamically displayed using the `Books` variable passed to the template.
- **Category-Specific Books:** Only the books in the selected category are shown.
- **Switchable Display Modes:** Users can toggle between grid and list view icons to change the layout of the book list.
- **No Results Message:** If no books are available in the selected category, a "No results" message is shown.

### Design and Layout:

- The layout is responsive and adapts based on the chosen display mode (grid or list).
- The book details are displayed in a clean, organized manner, allowing users to easily browse through books in the selected category.


## 📄 issuers.html

This template displays a list of either authors or publishers depending on the page context. It includes a dynamic title, result count, and a list of authors or publishers with links to their individual pages.

### Template Structure:

1. **Head Block:**
   - Links to the `issuers.css` and `index.css` stylesheets for styling the page.

2. **Body Block:**
   - Contains the main content of the page, which is dynamically generated based on the type of issuer (authors or publishers).

### Key Sections:

#### **Page Title:**

- **Dynamic Title:**
  - If the page is displaying authors, the title "Authors" is shown. 
  - If the page is displaying publishers, the title "Publishers" is shown.
  - This is controlled by the `authorsPage` variable.

#### **Results Count:**

- **Dynamic Results:**
  - The number of authors or publishers is displayed based on whether the page is showing authors or publishers.
  - If the page is showing authors, the result count is displayed as `{{ AUTHORS.count }}`.
  - If the page is showing publishers, the result count is displayed as `{{ PUBLISHERS.count }}`.

#### **Issuer List:**

- **Dynamic List of Authors or Publishers:**
  - If the page is showing authors (`authorsPage` is true), a list of authors is displayed. Each author's name is a clickable link that directs the user to the author's individual page (`/books/vault/author/{{ Author.id }}`).
  - If the page is showing publishers (`authorsPage` is false), a list of publishers is displayed. Each publisher's name is a clickable link that directs the user to the publisher's individual page (`/books/vault/publisher/{{ Publisher.id }}`).

#### **Styling:**

- The page uses the `issuer-list` class to display the list of authors or publishers.
- The `second-tape` div is used to display the result count, and it changes dynamically based on whether authors or publishers are being displayed.

### Features:

- **Dynamic Page Title:** The title changes based on the context (`Authors` or `Publishers`).
- **Result Count:** The number of authors or publishers is displayed dynamically.
- **Clickable Links:** Each author or publisher name is a clickable link that directs the user to the detailed page for that particular author or publisher.

### Design and Layout:

- The layout is consistent with other pages and provides a simple list of authors or publishers.
- The result count is displayed at the top, and the list of authors or publishers follows.


## 📄 issuer.html

This template displays the details of either an author or a publisher, including their biography or additional information, along with a list of books associated with them. It also provides options to delete the author or publisher.

### Template Structure:

1. **Head Block:**
   - Links to the `index.css` and `issuer.css` stylesheets for styling the page.

2. **Body Block:**
   - Contains the main content of the page, which is dynamically generated based on whether the entity is an author or a publisher.

### Key Sections:

#### **Page Title:**
- **Dynamic Title:**
  - If the page is displaying an author, the title `Author : {{ Author.name }}` is shown, including the author's name.
  - If the page is displaying a publisher, the title `Publisher : {{ Publisher.name }}` is shown, including the publisher's name.

#### **Delete Option:**
- **Delete Icon:**
  - A red delete icon is displayed next to the author or publisher name. Clicking this icon will trigger the deletion of the respective entity.
  - For authors, the link is `/books/vault/delete/author/{{ Author.id }}`.
  - For publishers, the link is `/books/vault/delete/publisher/{{ Publisher.id }}`.

#### **Biography (For Authors Only):**
- **Biography Section:**
  - If the page is displaying an author, a `biography` section is shown with the author's biography.

#### **Books Count:**
- **Books List Count:**
  - The total number of books associated with the author or publisher is displayed, dynamically showing the count of books with `{{ Books.count }}`.

#### **Display Mode (Grid/List View):**
- **Toggle View:**
  - Two icons are provided for switching between grid and list view of the books. 
  - Each icon toggles the book display style.

#### **Books List:**
- **Dynamic Books Display:**
  - A list of books associated with the author or publisher is displayed. Each book is shown in a grid layout with details like the book's name, ISBN, category, authors, and publisher.
  - Each book's image, name, ISBN, category, author(s), and publisher are displayed.
  - The books are clickable and link to their detailed pages at `/books/vault/book/{{ Book.id }}`.

#### **Styling:**
- The page uses a grid layout for displaying the books and includes specific classes like `book-box` for styling each book item.
- The `delete-icon` is styled as a clickable SVG icon in red.

### Features:
- **Dynamic Entity Display:** The template displays information based on whether the entity is an author or publisher.
- **Delete Functionality:** Allows the deletion of authors or publishers via a clickable red icon.
- **Books List:** Displays a list of books associated with the author or publisher.
- **Flexible Display Modes:** Users can toggle between grid and list view for the books.

### Design and Layout:
- The layout is consistent with other pages, featuring a dynamic title, biography (for authors), a book list, and a delete option.
- The books are displayed in a grid format, but users can toggle to a list format for better readability.

## 📄 new-list.html

This template allows the user to create a new list of books. The form enables users to provide a list name and select books to be added to the list. It also allows users to toggle between grid and list views to see the available books for selection.

### Template Structure:

1. **Head Block:**
   - Links to the `new-list.css` and `index.css` stylesheets for the styling of the page.

2. **Body Block:**
   - Contains the main content of the page, including the form for creating a new list and the list of available books to choose from.

### Key Sections:

#### **Page Title:**
- **Title Display:**
  - Displays the text `Create new list`.

#### **Form for Creating a New List:**
- **Form Fields:**
  - **List Name:** A text input field for entering the name of the new list.
  - **Books Selection:** A hidden input field (`books_ids`) holds the IDs of the selected books. This field is populated via JavaScript.
  - **Submit Button:** A button labeled `Create` for submitting the form and creating the new list.

#### **Selected Books Count:**
- **Selected Books Counter:**
  - Displays the number of books currently selected for the new list. This number is updated dynamically as books are selected or deselected.

#### **Display Mode (Grid/List View):**
- **Toggle View:**
  - Provides two icons to toggle between grid view and list view for displaying books. 
  - The grid view icon displays the books in a grid layout, while the list view icon displays them in a linear list.

#### **Books List:**
- **Books Display:**
  - A grid layout is used to display available books for selection.
  - Each book displays:
    - **Book Image:** A thumbnail image of the book.
    - **Book Name:** The name of the book.
    - **Book Details:**
      - ISBN number.
      - Category.
      - Authors (multiple authors separated by commas).
      - Publisher name.
  - Each book is presented in a `div` with the class `book-box`, and a hidden input field holds the book’s ID for selection purposes.

#### **Styling:**
- The page is styled using a grid layout for displaying books.
- The toggle buttons for grid and list views are represented by SVG icons.

### Features:
- **Dynamic Selected Count:** The number of books selected for the list is dynamically updated using JavaScript.
- **Book Selection:** Users can select books to be added to their new list by interacting with the books' checkboxes (handled via JavaScript).
- **Grid/List View Toggle:** Users can switch between a grid view and a list view for viewing available books.

### Design and Layout:
- The page uses a responsive grid layout for book listings, and provides a clean, easy-to-use interface for selecting books.
- The page includes icons for changing between different display views (grid and list).


## 📄 lists.html

This template displays a list of all available lists. Each list is clickable, and users can view the details of a specific list by clicking on its name.

### Template Structure:

1. **Head Block:**
   - Links to the `issuers.css` and `index.css` stylesheets to style the page and its components.

2. **Body Block:**
   - Contains the main content of the page, including the title, the count of available lists, and the listing of all available lists.

### Key Sections:

#### **Page Title:**
- **Title Display:**
  - Displays the text `Lists`, indicating that the page shows available lists.

#### **Results Counter:**
- **Results Count:**
  - Displays the total number of lists available in the `LISTS` variable.

#### **Lists Display:**
- **Lists Display:**
  - A list of all available lists is presented in an unordered list (`<ul>`). Each list is rendered as a list item (`<li>`) with a clickable link (`<a>`) that leads to the details page of the respective list.
  - Each list is displayed with its name, and when clicked, it navigates to the URL `/books/vault/list/{{ List.id }}`, where `List.id` is the unique identifier of the list.

### Design and Layout:
- The layout is simple and clean, with the lists being presented in a vertical list format.
- The page includes a section for showing the total number of lists available.


## 📄 list.html

This template is used to display the details of a specific book list. It shows the list's name, the books in the list, and allows users to edit or delete the list.

### Template Structure:

1. **Head Block:**
   - Links to the `index.css`, `issuer.css`, and `list.css` stylesheets to style the page and its components.

2. **Body Block:**
   - Contains the main content of the page, including the list's title, options for editing and deleting the list, and the books contained in the list.

### Key Sections:

#### **Page Title:**
- **Title Display:**
  - Displays the name of the current list (`{{ List.name }}`), indicating the list being viewed.

#### **List Options (Edit/Delete):**
- **Options Icon:**
  - An SVG icon that represents the options menu.
- **Options Container:**
  - Contains links for editing (`/books/vault/edit/list/{{ List.id }}`) and deleting (`/books/vault/delete/list/{{ List.id }}`) the list. These actions allow the user to modify or remove the list from their library.

#### **Books in the List:**
- **Books Count:**
  - Displays the total number of books in the list (`{{ List.books.all.count }}`).
- **Books Display:**
  - The books are displayed as clickable cards in a grid format. Each book card shows:
    - **Image**: The book's cover image.
    - **Details**: Includes the book’s ISBN, category, authors, and publisher.
    - **Link**: Clicking on the book's image or name takes the user to the book's detailed page (`/books/vault/book/{{ Book.id }}`).

#### **Display Options:**
- **Grid/List View Toggle:**
  - SVG icons that allow users to toggle between grid and list views for displaying the books.

### Design and Layout:
- The page features a clean design with a grid layout for displaying the books in the list.
- The page also includes interactive icons for list options (edit and delete) and a toggle to switch between grid and list views.

### Scripts:
- The `index.js` and `book.js` JavaScript files are loaded for handling page functionality, such as toggling display views and interacting with the list's books.

