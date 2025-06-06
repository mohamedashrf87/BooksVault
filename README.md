# BooksVault

BooksVault is a personal book cataloging web application designed to help users manage and organize their book collection. The application enables users to add, view, edit, and delete books in their library, while storing important information such as the book's title, author, genre, reading status, and a cover image. The project utilizes Django for backend functionality and Cloudinary for media storage and management of book cover images. The user interface is clean, responsive, and supports both light and dark modes for a comfortable user experience.

## Features

- **Add and Manage Books:** Users can easily add books to their collection, including relevant details such as title, author, cover image, and genre.
- **Dynamic Filtering:** Users can filter books based on their genre and reading status, making it easier to browse their library.
- **Responsive Design:** The application is fully responsive, ensuring a smooth experience across desktops, tablets, and mobile devices.
- **Dark and Light Mode:** The application supports both light and dark modes, allowing users to toggle between them for better readability.
- **Cloudinary Integration:** Book cover images are uploaded and stored via Cloudinary, enabling easy management of media files.
- **Minimalist Design:** The user interface focuses on simplicity, ensuring that the user experience remains intuitive and clutter-free.

---

## Distinctiveness and Complexity

BooksVault distinguishes itself from many other web applications by focusing on a **single-user library**. Instead of supporting multiple users and complex social interactions, the application aims to provide a personal, streamlined catalog for an individual’s book collection. The technical complexity arises from several areas of development, including:

- **Dynamic form handling** using Django's form system, ensuring that each book can be added or updated seamlessly with appropriate validation.
- **Custom filtering** functionality, which enables users to sort books by genre or reading status using Django ORM queries.
- **Image handling** via Cloudinary, allowing users to upload and display book cover images efficiently, while ensuring high quality and scalability.
- **Responsive layout** that adapts to various screen sizes using CSS Grid and Flexbox for a modern, fluid design.
- **Dark and light mode toggle**, which provides an adaptable user interface depending on user preferences or environmental lighting.

The project successfully integrates multiple Django features while maintaining a simple and intuitive interface. The complexity lies not in the number of users, but in how data is managed, presented, and interacted with in a personal context.

---

## Files Structure

### models.py

This file contains the definitions of models for the project. The models describe the structure of the database and define relationships between different entities such as users, authors, books, publishers, and lists.

---

#### 1. **User**
   - **Inherits from**: `AbstractUser`
   - **Description**: This model extends Django's built-in `AbstractUser` model without adding any additional fields. It serves as the base for the user-related data.

---

#### 2. **Authors**
   - **Fields**:
     - `user`: A foreign key linking to the `User` model, establishing a one-to-many relationship where a user can have multiple authors.
     - `name`: A `CharField` to store the author's name, with a maximum length of 255 characters.
     - `biography`: A `TextField` to store a short biography of the author.

---

#### 3. **Publisher**
   - **Fields**:
     - `user`: A foreign key linking to the `User` model, establishing a one-to-many relationship where a user can have multiple publishers.
     - `name`: A `CharField` to store the publisher's name, with a maximum length of 255 characters.

---

#### 4. **Book**
   - **Fields**:
     - `user`: A foreign key linking to the `User` model, establishing a one-to-many relationship where a user can have multiple books.
     - `name`: A `CharField` to store the book's name, with a maximum length of 64 characters.
     - `ISBN`: A `CharField` to store the ISBN number of the book, with a maximum length of 13 characters.
     - `category`: A `CharField` to store the category of the book. The choices for this field are defined in the `CATEGORIES` variable imported from `choices.py`.
     - `image_url`: A `URLField` to store the URL of the book's image.
     - `authors`: A `ManyToManyField` to link multiple authors to the book.
     - `publisher`: A foreign key linking to the `Publisher` model, establishing a one-to-many relationship where each book is linked to a publisher.
     - `added_at`: A `DateTimeField` that automatically stores the date and time when the book is added.
   - **Methods**:
     - `__str__(self)`: A string representation of the book, showing its name and ISBN.

---

#### 5. **List**
   - **Fields**:
     - `user`: A foreign key linking to the `User` model, establishing a one-to-many relationship where a user can have multiple lists.
     - `name`: A `CharField` to store the name of the list, with a maximum length of 64 characters.
     - `books`: A `ManyToManyField` to link multiple books to the list.

---

### Summary

- The `User` model extends Django's built-in authentication system.
- The `Authors`, `Publisher`, `Book`, and `List` models define relationships to the `User` model, with each representing entities in the library or book management system.
- The `Book` model has relationships to authors and publishers, as well as an automatically set `added_at` field.
- The `List` model allows users to organize books into custom lists.

This file helps structure the database schema for users, books, authors, publishers, and book lists, supporting the overall functionality of the project.

### choices.py

This file contains the definition of the `CATEGORIES` list, which provides the available choices for the category field in the `Book` model. Each category has a short code and a human-readable label for display purposes.

---


#### **CATEGORIES**

The `CATEGORIES` list contains tuples, where the first element is the short code for a category, and the second element is the full name of the category. These choices are used in the `Book` model to categorize books.

- **Format**: `('short_code', 'Full Category Name')`
- **Categories**:
  - `'ART'`: Art
  - `'BIOG'`: Biography
  - `'BUS'`: Business
  - `'CHR'`: Christian
  - `'CLA'`: Classics
  - `'COM'`: Comics
  - `'COOK'`: Cookbooks
  - `'EBOOK'`: Ebooks
  - `'FAN'`: Fantasy
  - `'FIC'`: Fiction
  - `'GRAPH-NOV'`: Graphic Novels
  - `'HIST-FIC'`: Historical Fiction
  - `'HIS'`: History
  - `'HOR'`: Horror
  - `'MEM'`: Memoir
  - `'MUS'`: Music
  - `'MYS'`: Mystery
  - `'NF'`: Nonfiction
  - `'POE'`: Poetry
  - `'PSY'`: Psychology
  - `'ROM'`: Romance
  - `'SCI'`: Science
  - `'SCI-FIC'`: Science Fiction
  - `'SH'`: Self Help
  - `'SPT'`: Sports
  - `'THR'`: Thriller
  - `'TRV'`: Travel
  - `'YA'`: Young Adult

These categories are used in the `Book` model to classify books into specific genres or types, making it easier to filter and organize them.

---

### Summary

- The `CATEGORIES` list defines a wide range of book genres and categories.
- Each category consists of a short code and its corresponding full name for use in the `Book` model.
- This allows for a standardized approach to categorizing books in the system.


### urls.py

This file defines the URL routing for the application. It maps various URL paths to corresponding view functions in the `views.py` file. The routes handle actions such as viewing, creating, editing, and deleting books, authors, publishers, and lists, as well as managing user authentication.

---

#### **URL Patterns**

1. **Home & Search**:
   - `""`: Maps to the `index` view, usually representing the homepage.
   - `"/search"`: Maps to the `search` view, allowing users to search for books, authors, or publishers.

2. **Category**:
   - `"/category/<str:Category>"`: Maps to the `category` view, displaying books from a specific category.

3. **Authors & Publishers**:
   - `"/authors"`: Maps to the `authors` view, listing all authors.
   - `"/publishers"`: Maps to the `publishers` view, listing all publishers.

4. **Lists**:
   - `"/lists"`: Maps to the `lists` view, showing a user's book lists.

5. **Create New Entities**:
   - `"/new/book"`: Maps to the `new_book` view, allowing users to create a new book.
   - `"/new/author"`: Maps to the `new_author` view, allowing users to create a new author.
   - `"/new/publisher"`: Maps to the `new_publisher` view, allowing users to create a new publisher.
   - `"/create/new/list"`: Maps to the `new_list` view, allowing users to create a new list.

6. **Book Details & Editing**:
   - `"/book/<int:BookID>"`: Maps to the `book` view, showing details of a specific book by its ID.
   - `"/edit/book/<int:BookID>"`: Maps to the `edit_book` view, allowing users to edit a specific book.
   - `"/add/book/<int:BookID>/to/list"`: Maps to the `add_book_to_list` view, adding a book to a user's list.

7. **Author, Publisher & List Details**:
   - `"/author/<int:AuthorID>"`: Maps to the `author` view, showing details of a specific author by ID.
   - `"/publisher/<int:PublisherID>"`: Maps to the `publisher` view, showing details of a specific publisher by ID.
   - `"/list/<int:ListID>"`: Maps to the `list` view, showing details of a specific list by ID.

8. **Edit Lists**:
   - `"/edit/list/<int:ListID>"`: Maps to the `edit_list` view, allowing users to edit a specific list.

9. **Delete Entities**:
   - `"/delete/book/<int:BookID>"`: Maps to the `delete_book` view, allowing users to delete a specific book.
   - `"/delete/author/<int:AuthorID>"`: Maps to the `delete_author` view, allowing users to delete a specific author.
   - `"/delete/publisher/<int:PublisherID>"`: Maps to the `delete_publisher` view, allowing users to delete a specific publisher.
   - `"/delete/list/<int:ListID>"`: Maps to the `delete_list` view, allowing users to delete a specific list.

10. **Authentication**:
    - `"/create/account"`: Maps to the `create_account` view, allowing users to create a new account.
    - `"/login"`: Maps to the `login_view` view, allowing users to log in.
    - `"/logout"`: Maps to the `logout_view` view, allowing users to log out.

---

### Summary

- The URL routes define how users interact with different pages in the application, from browsing books and authors to managing their own lists and accounts.
- Views are mapped to their respective URLs for viewing, creating, editing, and deleting content.
- Authentication routes are included for account creation, login, and logout functionality.


### views.py

This file contains the view functions that handle the logic for each route in the application. Each function manages interactions with the database and renders HTML templates, often based on user input or requests.

---

#### **View Functions**

1. **`index(request)`**: 
   - Displays the homepage with a list of books the user has added.
   - **Template**: `index.html`
   - **Context**: List of books sorted by the most recently added.

2. **`search(request)`**: 
   - Allows users to search for books by name or ISBN.
   - **Template**: `search.html`
   - **Context**: Display search results based on user query.

3. **`category(request, Category)`**:
   - Displays books belonging to a specific category.
   - **Template**: `category.html`
   - **Context**: List of books in the selected category.

4. **`authors(request)`**:
   - Lists all authors the user has added.
   - **Template**: `issuers.html`
   - **Context**: List of authors.

5. **`publishers(request)`**:
   - Lists all publishers the user has added.
   - **Template**: `issuers.html`
   - **Context**: List of publishers.

6. **`lists(request)`**:
   - Displays the user's saved book lists.
   - **Template**: `lists.html`
   - **Context**: List of user-created book lists.

7. **`new_book(request)`**:
   - Allows users to create a new book by uploading details such as name, ISBN, category, authors, and publisher.
   - **Template**: `new-book.html`
   - **Context**: Lists of authors, publishers, and categories.

8. **`new_author(request)`**:
   - Allows users to create a new author via a POST request.
   - **Context**: No template, returns HTTP response.

9. **`new_publisher(request)`**:
   - Allows users to create a new publisher via a POST request.
   - **Context**: No template, returns HTTP response.

10. **`new_list(request)`**:
    - Allows users to create a new book list by selecting books.
    - **Template**: `new-list.html`
    - **Context**: List of books for selection.

11. **`book(request, BookID)`**:
    - Displays detailed information about a specific book.
    - **Template**: `book.html`
    - **Context**: Book details.

12. **`edit_book(request, BookID)`**:
    - Allows users to edit an existing book's details.
    - **Template**: `edit-book.html`
    - **Context**: Book details, lists of authors, publishers, and categories.

13. **`author(request, AuthorID)`**:
    - Displays detailed information about a specific author and their books.
    - **Template**: `issuer.html`
    - **Context**: Author details and their associated books.

14. **`publisher(request, PublisherID)`**:
    - Displays detailed information about a specific publisher and their books.
    - **Template**: `issuer.html`
    - **Context**: Publisher details and their books.

15. **`list(request, ListID)`**:
    - Displays a user's book list.
    - **Template**: `list.html`
    - **Context**: List details.

16. **`edit_list(request, ListID)`**:
    - Allows users to edit an existing list by adding or removing books.
    - **Template**: `edit-list.html`
    - **Context**: List details and books available for selection.

17. **`add_book_to_list(request, BookID)`**:
    - Allows users to add a book to a list.
    - **Template**: `add-book-to-list.html`
    - **Context**: Book details and list of available lists.

18. **`delete_book(request, BookID)`**:
    - Allows users to delete a book from their collection.
    - **Context**: No template, redirects to the index page after deletion.

19. **`delete_author(request, AuthorID)`**:
    - Allows users to delete an author and remove them from books.
    - **Context**: No template, redirects to the index page after deletion.

20. **`delete_publisher(request, PublisherID)`**:
    - Allows users to delete a publisher.
    - **Context**: No template, redirects to the index page after deletion.

21. **`delete_list(request, ListID)`**:
    - Allows users to delete a book list.
    - **Context**: No template, redirects to the index page after deletion.

22. **`login_view(request)`**:
    - Handles the login process for users.
    - **Template**: `login.html`
    - **Context**: Error messages for failed login attempts.

23. **`create_account(request)`**:
    - Allows users to create a new account and log in automatically.
    - **Template**: `create-account.html`
    - **Context**: Error messages for invalid account creation.

24. **`logout_view(request)`**:
    - Logs the user out and redirects to the login page.
    - **Context**: No template, simply redirects.

---

### Summary

- The view functions provide the core logic for interacting with books, authors, publishers, and lists.
- User authentication is required for most actions, ensuring that users can only modify their own data.
- Each view is associated with its respective HTML template to render the page.



## Templates


### `layout.html`

This is the main layout file for the "Books Vault" web application. It defines the general structure of the HTML page and contains placeholders for dynamic content to be injected from other views. The file is built with Django template language and uses static files for styling and scripting. Below is a breakdown of the key sections and their contents:

1. **Head Section:**
   - The file includes metadata such as charset and viewport settings for responsive design.
   - It links the global stylesheet (`Global.css`) via Django's `{% static %}` tag.
   - The `{% block head %}` tag allows for additional content to be added to the head section from other templates that extend this layout.

2. **Body Section:**
   - **Authentication Check:** 
     The file includes conditional logic to check if the user is authenticated using `{% if request.user.is_authenticated %}`. If the user is logged in, the following elements are rendered:
     
     - **Main Navigation Bar:**
       A set of links (`Home`, `Authors`, `Publishers`, and `Lists`) is provided for navigation throughout the site.
       - Each link uses Django's `{% url %}` template tag to generate the correct URLs based on the app's URL configuration.
     
     - **Options Menu:**
       A set of options is available for the authenticated user to interact with, such as adding new books, authors, publishers, and creating new lists. There is also an option to toggle the theme and log out.
     
     - **Forms:**
       - **New Author Form:** A form for adding a new author with fields for the author's name and biography.
       - **New Publisher Form:** A form for adding a new publisher with a field for the publisher's name.
       
     - The forms are hidden by default and shown when the user interacts with specific elements (e.g., clicking on the "Add new Author" button).
     
     - **Mobile Navigation:**
       A second navigation bar specifically for mobile users with the same links (`Home`, `Authors`, `Publishers`, and `Lists`).
     
3. **Scripts:**
   - The file includes a script (`Global.js`) at the end to handle any JavaScript functionality for the layout, such as toggling the options menu or changing the theme.

4. **Dynamic Blocks:**
   - `{% block body %}` and `{% block head %}` are placeholders for other templates to inject their own content into the layout when they extend this base template.

This layout provides a clean structure that can be reused throughout the application for consistency and efficient content rendering.


### `index.html`

This file extends the `layout.html` template and serves as the homepage for the "Books Vault" application. It displays various features such as a search bar, book categories, and a list of books from the user's collection. The file uses Django's template language to dynamically load content and interact with the user. Below is a breakdown of the key sections and their contents:

1. **Head Section:**
   - The `{% block head %}` is extended to include a specific stylesheet for the homepage (`index.css`) using Django's `{% static %}` tag.

2. **Body Section:**
   - **Search and Browse Books:**
     - A search bar is provided to allow users to search for books by name or ISBN. The form submits a `POST` request to the `search` URL and includes a CSRF token for security.
     - Below the search bar, a set of categories is displayed, each linking to a page filtered by that category.
     
   - **Add New Book:**
     - A prominent call-to-action button is provided for users to add a new book to their collection. The button includes an SVG icon and text, and it links to the `new-book` URL where the user can enter details for a new book.

   - **Books Count and Display Options:**
     - The page shows the total number of books in the user's collection using `{{ Books.count }}`.
     - There are icons for toggling between grid and list display formats for showing the books, allowing users to choose their preferred layout.

   - **Books Listing:**
     - The books in the collection are displayed in a grid layout by default (`class="grid"`). Each book is presented as a clickable card that links to a detailed page for that book.
     - For each book, key details like ISBN, category, authors, and publisher are displayed. The authors are listed dynamically, and their names are separated by commas if there are multiple authors.

3. **Scripts:**
   - The file includes a script (`index.js`) at the end to handle any JavaScript functionality for the homepage, such as toggling display options (grid or list).

This file serves as the main page where users can interact with their book collection by searching for books, browsing categories, adding new books, and viewing their books in different layouts.


### `new-book.html`

This file extends the `layout.html` template and serves as the page where users can add a new book to their collection. The form allows users to input various details about the book, such as its name, ISBN, category, authors, publisher, and cover image. It uses Django's template language to display any validation errors, pre-fill the form with data (such as categories and authors), and handle the submission securely with CSRF protection. Below is a breakdown of the key sections and their contents:

1. **Head Section:**
   - The `{% block head %}` is extended to include the `new-book.css` stylesheet specific to the "Add New Book" page.

2. **Body Section:**
   - **Form Setup:**
     - The form uses `POST` method and `enctype="multipart/form-data"` to handle file uploads (for the book image). It posts data to the `new-book` URL and includes a CSRF token for security.

   - **Main Title:**
     - A main title (`Add new book`) is displayed at the top of the page to indicate the purpose of the form.

   - **Image Upload:**
     - The form includes a file input (`<input type="file">`) for uploading a book image. A custom label (`image-label`) is provided to trigger the file input, and the uploaded image can be previewed once selected.
     - If there is an image validation error (represented by the `imageE` variable), the label is styled with a red outline and the error message is displayed.

   - **Book Details Inputs:**
     - **Book Name:**
       - An input field for the book name (`book_name`). If there’s a validation error (represented by `nameE`), the input field is outlined in red, and the error message is shown.
     - **ISBN:**
       - An input field for the ISBN number (`ISBN`). Similar to the book name input, any validation errors are displayed with a red outline.
     - **Category:**
       - A dropdown menu to select the book's category (`category`). The options are dynamically populated from the `CATEGORIES` context variable.
     - **Authors:**
       - A text input for entering authors. As authors are typed, a list of matching authors (`authorsList`) is displayed below, and users can choose authors from the list. The selected authors are dynamically added to a hidden input field (`authorsValues`) and displayed in the `chosen-authors` section.
     - **Publisher:**
       - A dropdown menu for selecting the publisher (`publisher`). The options are dynamically populated from the `PUBLISHERS` context variable.

   - **Submit Button:**
     - A submit button (`Add`) allows the user to submit the form and add the new book to the collection.

3. **Scripts:**
   - The file includes a script (`new-book.js`) at the end to handle any dynamic functionality, such as displaying the list of authors or previewing the uploaded image.

This file serves as the page for adding a new book to the "Books Vault" application, allowing users to input and upload all necessary information about the book.


### `category.html`

This template is used to display books within a specific category. The page shows the category name, the number of books in that category, and a list of books available within that category. Each book is displayed with its name, ISBN, category, authors, and publisher, as well as an image. It also includes display options for grid and list view.

1. **Head Section:**
   - The `{% block head %}` is extended to include the `issuers.css` and `index.css` stylesheets for styling the page layout and the display of books.

2. **Body Section:**
   - **Category Title:**
     - The page begins with a title (`Category: <Category Name>`), where `<Category Name>` is dynamically populated from the `Category` context variable. The category name is highlighted using a custom text color (`--special-text`).
   
   - **Results Section:**
     - A section that shows the number of books in the selected category (`Results: <number>`). The number of books is dynamically fetched with `Books.count`.
   
   - **Display Options (Grid/List View):**
     - Two display icons are provided for switching between grid and list views for displaying books. These icons are SVG elements that provide visual control over how books are displayed.

   - **Books Display:**
     - A loop (`{% for Book in Books %}`) iterates over all the books in the selected category. Each book is displayed in a box that includes:
       - **Image:** The book's cover image (`Book.image_url`).
       - **Details:** Information about the book, including:
         - ISBN
         - Category (displayed using the `Book.get_category_display` method)
         - Authors (looped over if multiple authors are present)
         - Publisher
       - Clicking on the book box redirects the user to the detailed view of the book.

   - **No Results Message:**
     - If no books are found in the selected category (`Books|length == 0`), a message saying `No results` is displayed.

3. **Scripts:**
   - The file includes a script (`index.js`) at the end to handle dynamic interactions, such as toggling between grid and list views.

This page allows users to browse books filtered by category, view their details, and easily toggle between grid and list views for a better browsing experience.


### `search.html`

This template is used to display the results of a search query for books. The page shows the search query, the number of books found, and the list of books that match the search criteria. It also allows users to toggle between grid and list views for displaying the results.

1. **Head Section:**
   - The `{% block head %}` includes two stylesheets (`issuers.css` and `index.css`) to style the layout and display of books.

2. **Body Section:**
   - **Search Query Title:**
     - The page begins with a title (`Search: <search term>`), where `<search term>` is dynamically populated from the `search` context variable. The search term is highlighted using the custom text color `--special-text`.
   
   - **Results Section:**
     - A section shows the number of books that match the search query (`Results: <number>`). The number of books is dynamically fetched with `Books.count`.
   
   - **Display Options (Grid/List View):**
     - Two icons are provided for switching between grid and list views for displaying books. These are SVG icons that allow the user to toggle between the two display formats.

   - **Books Display:**
     - A loop (`{% for Book in Books %}`) iterates over all the books returned by the search. Each book is displayed in a box with:
       - **Image:** The book's cover image (`Book.image_url`).
       - **Details:** Information about the book, including:
         - ISBN
         - Category (displayed using the `Book.get_category_display` method)
         - Authors (looped over if multiple authors are present)
         - Publisher
       - Clicking on the book box redirects the user to the detailed view of the book.

   - **No Results Message:**
     - If no books are found that match the search query (`Books|length == 0`), a message saying `No results` is displayed.

3. **Scripts:**
   - The file includes a script (`index.js`) at the end to handle dynamic interactions, such as toggling between grid and list views.

This page is designed to display the search results efficiently, with options to toggle views for a better browsing experience.


### `book.html`

This template is used to display detailed information about a specific book. The page shows the book's image, name, and various details such as ISBN, category, authors, and publisher. It also provides options for the user to edit, add to a list, or delete the book.

1. **Head Section:**
   - The `{% block head %}` includes a single stylesheet (`book.css`) that styles the layout and presentation of the book details.

2. **Body Section:**
   - **Main Container:**
     - The page's main container is structured to display the book's image and textual details side by side.
   
   - **Book Image:**
     - The book's image is displayed using `<img class="book-img">`, with the `src` attribute dynamically set from the `Book.image_url` context variable.

   - **Book Details:**
     - The book's name is displayed in a prominent text field.
     - The details of the book are shown in a split format:
       - **Left Column:** Displays static labels for ISBN, Category, Authors, and Publisher.
       - **Right Column:** Displays the corresponding values for the above details:
         - ISBN is displayed directly.
         - The category is displayed using the `Book.get_category_display` method.
         - Authors are listed, with each author's name linked to their own author page (`/books/vault/author/{{ author.id }}`).
         - The publisher is displayed as a clickable link to the publisher's page (`/books/vault/publisher/{{ Book.publisher.id }}`).

   - **Book Options:**
     - An SVG icon (three dots) is used to indicate available options for the book.
     - When clicked, these options are displayed in a container with links for:
       - **Edit:** Redirects the user to the edit page for the book (`/books/vault/edit/book/{{ Book.id }}`).
       - **Add to List:** Allows the user to add the book to a list (`/books/vault/add/book/{{ Book.id }}/to/list`).
       - **Delete:** Allows the user to delete the book (`/books/vault/delete/book/{{ Book.id }}`).
     - The options container is shown or hidden based on user interaction, and the "exit" button allows closing the options.

3. **Scripts:**
   - The file includes a script (`book.js`) to manage interactions such as toggling the visibility of the options container.

This template is designed to present a detailed, interactive view of a book, with clear options for editing, adding to a list, or deleting the book.


### `edit-book.html`

This template is used for editing a book's details. It displays a form where users can update the book's image, name, ISBN, category, authors, and publisher. The form is pre-filled with the current book's information, and the user can modify these fields and submit the updated details.

1. **Head Section:**
   - The `{% block head %}` includes a specific stylesheet (`new-book.css`) to style the book-editing form and its elements.

2. **Body Section:**
   - **Form:**
     - The form is set to `POST` data to `/books/vault/edit/book/{{ Book.id }}`, where the book's details will be updated.
     - The `{% csrf_token %}` ensures protection against Cross-Site Request Forgery attacks.

   - **Title:**
     - A main title is displayed, indicating that the user is editing the book with its current name (`"{{ Book.name }}"`).

   - **Main Container:**
     - The container is divided into two main sections:
       - **Image Input:**
         - The user can change the book's image by selecting a new image file. The current image is shown as a preview (`<img src="{{ Book.image_url }}">`), and the file input field is hidden, being triggered when the user clicks on the preview image.

       - **Details Inputs:**
         - The following fields are displayed for editing:
           - **Book Name:** A text input for the book's name.
           - **ISBN:** A number input for the book's ISBN.
           - **Category:** A dropdown select input that shows all available categories from `CATEGORIES`. The currently selected category is pre-selected.
           - **Authors:** A text input where users can type to search for authors. A list of authors (`AUTHORS`) is displayed, and authors already associated with the book are visually marked as selected. Authors can be chosen from this list.
           - **Publisher:** A dropdown select input to choose the publisher from `PUBLISHERS`, with the current publisher pre-selected.

   - **Submit Button:**
     - A submit button (`Save`) is included to allow the user to save the changes made to the book's details.

3. **Scripts:**
   - A script (`edit-book.js`) is included to handle dynamic interactions on the page, such as managing the authors list and input fields for authors.

This template provides a comprehensive and user-friendly interface for editing a book's details, with an easy-to-use form for updating various fields related to the book.


### `new-list.html`

This template is used for creating a new list of books. It allows the user to give a name to the list, and then select books to add to it. After the list is created, it submits the data (including selected book IDs) to be processed and stored.

1. **Head Section:**
   - The `{% block head %}` includes two stylesheets: `new-list.css` and `index.css` to style the page and form elements.

2. **Body Section:**
   - **Page Title:**
     - A title (`Create new list`) is displayed at the top of the page.

   - **Form:**
     - The form submits a `POST` request to the `{% url 'new-list' %}` URL to create a new list. It contains:
       - **List Name:** A text input field for entering the name of the list.
       - **Create Button:** A submit button labeled "Create" to create the new list.

     - **Hidden Input Field:** An input field (`books_ids`) is included to store the IDs of selected books. This input is hidden from the user.

3. **Second Tape Section:**
   - **Selected Books Count:** A paragraph showing the number of selected books (`Selected : 0`). This value is updated dynamically as books are selected.
   
   - **Display Icons:**
     - Icons for grid and list view are included, allowing users to toggle between different book display modes.

4. **Books Display Section:**
   - **Books Grid:**
     - A grid of books (`books-container`) is displayed. For each book:
       - An image of the book is shown (`<img src="{{ Book.image_url }}">`).
       - Book details such as ISBN, category, authors, and publisher are displayed in a structured format.
       - Each book is wrapped inside a `book-box` div. A hidden input field with the book's ID (`<input type="hidden" id="BookID" value="{{ Book.id }}">`) is included for future selection.

5. **Scripts:**
   - Two JavaScript files are included:
     - `new-list.js` to manage dynamic interactions such as selecting books and updating the selected count.
     - `index.js` which may handle common interactions across the app.

### User Flow:
- The user enters a name for the list in the "List Name" input field and selects books from the grid.
- The user can toggle between different views (grid or list) for the books.
- Once the books are selected, the form submits the list name and selected book IDs to create the new list.

This template provides a simple and functional interface for creating new lists and adding books to them.


### `issuers.html`

This template is used for displaying a list of either authors or publishers based on the `authorsPage` variable. It dynamically adjusts the content and page title depending on whether the page is for authors or publishers.

1. **Head Section:**
   - The `{% block head %}` includes two stylesheets: `issuers.css` and `index.css` for styling the layout and general elements of the page.

2. **Body Section:**
   - **Page Title:**
     - The title changes based on the value of the `authorsPage` variable:
       - If `authorsPage` is `True`, the title is "Authors".
       - Otherwise, it shows "Publishers".

   - **Results Count:**
     - Displays the number of results (authors or publishers) depending on whether `authorsPage` is `True` or `False`.
     - If `authorsPage` is `True`, it displays the number of authors with `{{ AUTHORS.count }}`.
     - If `authorsPage` is `False`, it displays the number of publishers with `{{ PUBLISHERS.count }}`.

   - **Issuer List:**
     - A list (`issuer-list`) of authors or publishers is displayed using an unordered list (`<ul>`). Depending on the `authorsPage` flag:
       - **Authors:** The template loops through the `AUTHORS` queryset and displays each author's name as a clickable link (`<a href="/books/vault/author/{{ Author.id }}">`).
       - **Publishers:** Similarly, it loops through the `PUBLISHERS` queryset and displays each publisher's name as a clickable link (`<a href="/books/vault/publisher/{{ Publisher.id }}">`).

3. **Conditional Rendering:**
   - The page dynamically adjusts the content displayed based on the `authorsPage` flag. This ensures that either authors or publishers are shown, depending on the context of the page.

### User Flow:
- The user is presented with a list of authors or publishers, depending on the page they are visiting.
- The page also shows the total number of authors or publishers available.
- Clicking on a name will redirect the user to the respective author or publisher page (`/books/vault/author/{{ Author.id }}` or `/books/vault/publisher/{{ Publisher.id }}`).

This template provides a flexible structure for displaying lists of authors or publishers and their details on separate pages.


### `lists.html`

This template is used to display a list of all the book lists created by the user. It shows the name of each list and links to a detailed page for each one.

1. **Head Section:**
   - The `{% block head %}` includes two stylesheets: `issuers.css` and `index.css` for styling the layout and general elements of the page.

2. **Body Section:**
   - **Page Title:**
     - The title of the page is statically set to "Lists".

   - **Results Count:**
     - Displays the total number of lists available using the variable `{{ LISTS.count }}`. This shows how many lists have been created.

   - **Lists:**
     - A list of all available book lists is rendered using an unordered list (`<ul>`). Each list (`List`) is displayed with a clickable link (`<a>`). The link points to a detailed page of the list (`/books/vault/list/{{ List.id }}`), where users can view more details or interact with the list.

3. **User Flow:**
   - The user is presented with a page displaying all created lists. The total number of lists is shown at the top.
   - Each list name is a clickable link, which, when clicked, will take the user to a detailed view of the respective list.

### Summary:
- This template provides a straightforward way for users to view all the lists they have created in the system. Each list is linked to a detail page where users can further interact with the list.


## `issuer.html`

This template displays detailed information about either an **author** or a **publisher** and lists the books associated with them. It also includes a delete button for the author or publisher.

### Head Section:
- **CSS Styles:**
  - Includes two stylesheets: `index.css` and `issuer.css` for general and issuer-specific styling.

### Body Section:

1. **Author/Publisher Name:**
   - Depending on whether the `Author` object exists, the page will either show details for an author or a publisher.
   - If it's an author, the page displays the author's name and biography.
   - If it's a publisher, only the publisher's name is shown.

2. **Delete Icon:**
   - A red delete icon (trash can) is available for both authors and publishers. Clicking this icon will initiate a deletion request for the respective entity.
   - The delete action for authors and publishers leads to different URLs: `/books/vault/delete/author/{{ Author.id }}` or `/books/vault/delete/publisher/{{ Publisher.id }}`.

3. **Books Count:**
   - Displays the number of books associated with the author or publisher.
   - This is shown inside the second tape (`<div class="second-tape">`), which also includes icons for changing the display format (grid or list).

4. **Books List:**
   - Books associated with the author or publisher are displayed in a grid layout.
   - Each book is shown with its image, name, ISBN, category, authors, and publisher.
   - Each book's name is a clickable link that leads to the book’s details page (`/books/vault/book/{{ Book.id }}`).

5. **Icons for Display:**
   - Two display icons (grid and list view) are provided to toggle between different formats for showing the books.

6. **JS:**
   - Includes `index.js` for additional interactivity or functionality on the page.

### User Flow:
- If an author or publisher is selected, their detailed information is shown, including a biography for authors.
- A list of books associated with the selected author/publisher is displayed in a grid format, with options to change the display style.
- Users can delete authors or publishers, which will be reflected upon confirmation.

### Summary:
This template serves to show detailed information about authors or publishers along with the books they are associated with. It also provides options to delete authors or publishers, while allowing users to view the list of books in different formats.


## `list.html`

This template displays the details of a book list (e.g., a reading list or a curated list) and provides options to edit or delete the list. It also displays all books within the list, offering a grid view and various options for displaying the books.

### Head Section:
- **CSS Styles:**
  - Includes three stylesheets: `index.css`, `issuer.css`, and `list.css`, which provide general, issuer-specific, and list-specific styling.

### Body Section:

1. **List Name:**
   - Displays the name of the list (`List.name`).

2. **Options for the List:**
   - A set of three circles (represented as an SVG icon) provides an interface to open options for the list.
   - When clicked, it shows options to:
     - **Edit** the list: Links to `/books/vault/edit/list/{{ List.id }}`
     - **Delete** the list: Links to `/books/vault/delete/list/{{ List.id }}`

3. **Close Options:**
   - An SVG icon (a cross) allows users to close the options container.

4. **Books in the List:**
   - The number of books in the list is displayed in the second tape (`<div class="second-tape">`).
   - Two display options (grid and list view) are available using SVG icons to toggle the format of how books are shown.

5. **Books List:**
   - Displays a grid of books within the list.
   - Each book is represented by a `book-box` that includes:
     - The book's image
     - The book’s name
     - A detailed view of the book's:
       - ISBN
       - Category
       - Authors (with a comma separating multiple authors)
       - Publisher

   - Each book is a clickable link that leads to the book’s detail page (`/books/vault/book/{{ Book.id }}`).

6. **JS:**
   - Includes two JavaScript files:
     - `index.js` for general functionality or interactivity.
     - `book.js` for book-specific functionality or behavior.

### User Flow:
- When the user selects a list, they can see its name and the options to either edit or delete it.
- The list of books within the list is displayed in a grid format, and users can toggle between grid and list view formats.
- Users can click on individual books to view their details.

### Summary:
This template serves to display a specific book list with its books. It also provides options to manage the list (edit or delete). The books are shown in a grid layout, and users can view detailed information about each book by clicking on it. The design offers options for adjusting how the books are displayed.

## `edit-list.html`

This template allows the user to edit a book list, including updating the list name and selecting or deselecting books. It includes a form to save the changes and displays the current books in the list with options for adjusting the layout.

### Head Section:
- **CSS Styles:**
  - Includes two stylesheets: `new-list.css` for specific list editing styles and `index.css` for general styling.

### Body Section:

1. **Page Title:**
   - Displays a title indicating the page is for editing the list, with the name of the list highlighted using a special color (`var(--special-text)`).

2. **Edit List Form:**
   - The form includes:
     - A **text input** for the list name, which defaults to the current list name (`List.name`).
     - A **submit button** to save the changes, which submits the form to `/books/vault/edit/list/{{ List.id }}`.
     - A hidden input (`books_ids`) for tracking the selected books’ IDs.

3. **Second Tape (Selected Books):**
   - Displays the number of books in the list (`List.books.all.count`).
   - Two display options (grid and list view) are available using SVG icons to toggle between the two formats.

4. **Books Selection:**
   - Displays a grid of books from the `Books` context variable, which includes:
     - An **input field** for each book's ID (hidden) to track selected books.
     - **Book details** including the book's image, name, ISBN, category, authors, and publisher.
   - If a book is already part of the list (`Book in List.books.all`), it is marked with the class `selected-books`.

5. **JavaScript:**
   - Includes two JavaScript files:
     - `edit-list.js` for handling the list editing functionality, likely for selecting or deselecting books.
     - `index.js` for general interactivity or common functionality.

### User Flow:
- When the user visits this page, they can:
  - Edit the name of the list.
  - Select or deselect books by clicking on them (the selection is tracked with the hidden `books_ids` input).
  - Submit the form to save changes to the list, including the updated name and selected books.

### Summary:
This template serves as an edit page for a book list. It allows the user to modify the list's name and manage the books within the list, providing a grid view of books and an option to toggle the display format. Users can save their changes by submitting the form. The selected books are tracked and saved with the list update.

## `add-book-to-list.html`

This template allows the user to add a book to a specific list. It displays a list of available lists and lets the user select one to add the book to by submitting a form.

### Head Section:
- **CSS Styles:**
  - Includes two stylesheets: `issuers.css` for list styling and `index.css` for general styling.

### Body Section:

1. **Page Title:**
   - The page title indicates the action of adding a book to a list. The name of the book is highlighted using a special color (`var(--special-text)`).

2. **Second Tape (Select List):**
   - A simple section with the label "Select List" to prompt the user to choose a list.

3. **List of Available Lists:**
   - An unordered list (`<ul>`) is populated with a form for each available list (`LISTS`):
     - Each list is displayed as a list item (`<li>`), with a form that includes:
       - A hidden input field (`list_id`) to track which list the user is selecting.
       - A **submit button** that, when clicked, submits the form to `/books/vault/add/book/{{ Book.id }}/to/list`, adding the selected book to the chosen list.
     - The button displays the name of the list (`List.name`).

4. **JavaScript:**
   - No JavaScript is included in this template, as the functionality relies on form submission.

### User Flow:
- When the user visits this page, they can:
  - See a list of available lists to which they can add the book.
  - Select a list by clicking the corresponding button, which submits a form to add the book to the chosen list.

### Summary:
This template is designed to add a book to a specific list. It displays a list of all available lists and allows the user to select one by submitting a form. The selected list's ID is sent along with the book's ID to update the database and add the book to the chosen list.


## `login.html`

This template handles the user login functionality, allowing users to log in to their library account. It includes a form where users can enter their email and password.

### Head Section:
- **CSS Styles:**
  - Includes a single stylesheet: `authentication.css` for styling the login form and related elements.

### Body Section:

1. **Form Container:**
   - The main form is wrapped inside a container (`authentication-form-container`) for proper alignment and styling.
   - The form uses `POST` method and submits to the `login` URL, which is likely routed to the login view in Django.
   
2. **Form Title and Instructions:**
   - The title (`Log in to your library account`) informs the user about the purpose of the page.
   - A secondary line explains that they can log in with the credentials they provided during registration.

3. **Email Input:**
   - A labeled text input (`Email`) where the user can enter their email address.
   - The field has a dynamic red outline if there’s an email error (`emailE`).
   - If there's an error related to the email, it is displayed below the input field in red text.

4. **Password Input:**
   - A labeled password input (`Password`) for the user to enter their password.
   - The field also has a red outline when there is a password error (`passwordE`).
   - If there's a password error, it is shown below the input field.

5. **Error Display:**
   - Both email and password inputs have conditional error messages (`emailE` and `passwordE`) shown in a `<p>` tag with the class `errors`.

6. **Account Creation Link:**
   - A reminder that users can create an account if they don’t already have one, with a link to the account creation page.

7. **CSRF Token:**
   - `{% csrf_token %}` to include CSRF protection for form submissions.

8. **Submit Button:**
   - The submit button labeled "Login" allows the user to submit the form.

9. **Background Image:**
   - A background image (`online-library.png`) is included at the bottom right of the page for visual enhancement.

### User Flow:
- When a user visits this page, they will:
  1. Enter their email address and password into the respective fields.
  2. If there are validation errors (either email or password), those errors will be displayed next to the corresponding field.
  3. Click the "Login" button to submit the form and authenticate the user.
  4. If they don’t have an account, they can create one by following the link to the registration page.

### Summary:
This template provides a user-friendly login interface with clear labels, error handling, and a link to create a new account. It ensures that users are aware of any input mistakes and can easily access the necessary resources for logging in or signing up.


## `create-account.html`

This template is used for creating a new user account on the library platform. It provides a form where users can input their username, email, and password to register for an account.

### Head Section:
- **CSS Styles:**
  - It includes the `authentication.css` stylesheet, which styles the form and related elements.

### Body Section:

1. **Form Container:**
   - The form is placed inside a container (`authentication-form-container`) for proper alignment and visual design.
   - The form uses the `POST` method and is submitted to the `create-account` URL, likely handled by Django's view for account creation.

2. **Form Title and Instructions:**
   - The title (`Create new library account`) clearly indicates the purpose of the page.
   - A secondary line gives instructions, informing the user that they need to enter the required information to create an account.

3. **Username Input:**
   - A labeled text input (`Username`) allows the user to enter their desired username.
   - The field will have a red outline if there's an error related to the username (`usernameE`).
   - If there is an error, it will be displayed below the input field in red text.

4. **Email Input:**
   - A labeled text input (`Email`) for the user to enter their email address.
   - Like the username input, it will show a red outline if there is an error with the email.
   - If an error is present, it will be displayed below the input field.

5. **Password Input:**
   - A labeled password input (`Password`) where users can enter their password.
   - The field will display a red outline if there's a password error (`passwordE`).
   - If there's an error, it will appear below the input field.

6. **Error Display:**
   - Error messages for the username, email, and password inputs are conditionally shown below the respective fields (`usernameE`, `emailE`, and `passwordE`), in red text.

7. **Login Link:**
   - A prompt reminding users who already have an account to log in, with a link to the login page (`/books/vault/login`).

8. **CSRF Token:**
   - The `{% csrf_token %}` ensures CSRF protection for the form submission.

9. **Submit Button:**
   - The submit button is labeled "Create" and allows users to submit the form and create their account.

10. **Background Image:**
   - A background image (`online-library.png`) is displayed at the bottom right of the page for added visual appeal.

### User Flow:
- When a user visits this page, they will:
  1. Enter their desired username, email, and password into the respective fields.
  2. If any of the fields have validation errors, the corresponding error messages will appear.
  3. After filling in the details, the user can click the "Create" button to submit the form and create their account.
  4. If they already have an account, they can click the "Login" link to navigate to the login page.

### Summary:
This template provides a simple and clear account creation interface, with form validation and error handling. It helps guide users through the registration process while ensuring they are aware of any input errors. The background image and overall layout are designed for a user-friendly experience.



## Static Files


### Global.js

The `Global.js` file contains various JavaScript functions for managing UI interactions and functionality across the site. Here's a breakdown of what it contains:

1. **Options Menu Toggle:**
   - When the options icon (`#optionsIcon`) is clicked, it displays an options container (`#optionsContainer`) and a blur effect (`#blurForOptions`).
   
2. **Forms for New Author and Publisher:**
   - When the "new author" or "new publisher" buttons are clicked, it opens respective forms (`newAuthorForm` and `newPublisherForm`) for adding a new author or publisher.
   - The forms' input fields are reset before being shown.
   
3. **Blur Effect Close:**
   - Clicking the blur effect (`#blurForOptions`) will close the options container and forms.

4. **Form Submission for New Author/Publisher:**
   - Both forms (`newAuthorForm` and `newPublisherForm`) submit the data to respective endpoints (`/books/vault/new/author` and `/books/vault/new/publisher`) using a POST request with JSON data.
   - If the fields are empty, an alert is shown, and the form is reopened.
   - After submission, the page is reloaded.

5. **Dark Mode Toggle:**
   - It includes functionality to toggle between dark and light mode based on user preference.
   - It checks the current theme from local storage and applies the respective theme.
   - The theme is toggled when the toggle button (`#toggleButton`) is clicked, and the theme preference is saved in local storage.
   - The images are also updated based on the theme (e.g., switching to dark mode images).

6. **Search Input Focus/Blur:**
   - When the search input (`#searchInput`) is focused, the placeholder changes to "Title / ISBN."
   - When the search input loses focus, the placeholder reverts to "Search."


### index.js

The `index.js` file contains JavaScript that controls the display mode of the books container. Here's what it does:

1. **Grid and List View Toggle:**
   - The script listens for clicks on two icons (`#gridDisplayIcon` and `#listDisplayIcon`) to toggle between grid and list views for the books container (`#booksContainer`).
   
2. **Grid View:**
   - When the grid display icon is clicked, the `booksContainer` class is changed to `'books-container grid'`, applying the grid layout to the books.
   
3. **List View:**
   - When the list display icon is clicked, the `booksContainer` class is changed to `'books-container list'`, applying the list layout to the books.


### book.js

The `book.js` file contains JavaScript that handles the functionality of displaying and hiding a book options menu. Here's a breakdown of its contents:

1. **Book Options Menu Toggle:**
   - When the book options icon (`#bookOptionsIcon`) is clicked, it displays the book options container (`#bookOptionsContainer`) and the exit button (`#bookOptionsExit`).
   
2. **Book Options Menu Close:**
   - When the exit button (`#bookOptionsExit`) is clicked, it hides both the book options container and the exit button.

This script is used for showing and hiding a menu with options related to a specific book when the user interacts with the book options icon.


### new-book.html

The `new-book.html` file contains JavaScript that handles the file input for book image previews, as well as the management of author selection. Here's a breakdown of its features:

1. **Image Preview for Book:**
   - When an image file is selected using the image input (`#imageInput`), the script reads the file and displays a preview in the same size as the input label.
   - If the selected file is not an image, an alert is shown to the user asking them to select an image file.

2. **Author Selection:**
   - The script manages a list of authors (`authorsList`) that the user can select from. When an author is clicked, it is added to the chosen authors list (`chosenAuthors`) or removed if already selected.
   - The input field (`#authorsInput`) is used for searching authors by name. It shows the authors list (`#authorsList`) when focused and hides it when the focus is lost.
   - Up to three authors can be selected. If more than three are selected, additional selections are ignored.
   - A hidden input (`#authorsValues`) is updated with the list of selected authors, which is used to store the chosen authors in a comma-separated format.

3. **Search Authors:**
   - The script listens for keyup and keydown events on the authors input field to search through the author list and show matching names. If no authors match the search, a "No results" message (`#authorsListNoResults`) is shown.

4. **Dynamic Styling and Interactions:**
   - The appearance of the authors input field is dynamically adjusted, including changing the border radius and padding as authors are selected.
   - The chosen authors are displayed with their names, and the authors input resets after a selection is made.

This script enhances the user experience by allowing easy image previewing and smooth author selection with a search feature.


### edit-book.js

The `edit-book.js` file contains JavaScript that allows users to update the book’s image and author selection. Here's a breakdown of its functionality:

1. **Image Preview for Editing:**
   - When an image file is selected using the image input (`#imageInput`), the file is read, and the image is displayed as a preview (`#imagePreview`).
   - The preview is styled to match the input field dimensions and is shown with a border-radius of 5px.
   - If the selected file is not an image, an alert is displayed.

2. **Pre-selecting Authors:**
   - If authors are already selected (indicated by `.selected-authors` elements), these authors are moved from the list (`#authorsList`) to the chosen authors container (`#chosenAuthors`).
   - The selected authors' names are stored in an array (`authorsValues`), and the hidden input (`#authorsValues`) is updated with a comma-separated list of these authors.

3. **Author Selection and Search:**
   - The author input field (`#authorsInput`) shows a list of authors (`#authorsList`) when focused, and hides it when blurred.
   - Users can search for authors by typing in the input field, and the list is filtered dynamically.
   - A maximum of three authors can be selected. If more than three are selected, further selections are ignored.
   - Authors can be added to or removed from the chosen authors list (`#chosenAuthors`) by clicking their names.
   - The input field's padding adjusts based on the number of selected authors.

4. **Dynamic Search and No Results:**
   - When searching for authors, the script checks if there are any visible author names left in the list. If none are visible, a "No results" message (`#authorsListNoResults`) is shown.

This script enables users to easily modify the book's image and authors, providing a smooth user experience for updating book details.


### new-list.js

The `new-list.js` file contains JavaScript that enables the selection of multiple books within a list. Here's a breakdown of its features:

1. **Book Selection:**
   - The script listens for clicks on each book box (`.book-box`). When a book is clicked, it toggles between the "selected" and "unselected" states.
   - If the book is already selected, it is removed from the selected books list and its class is reset to `'book-box'`.
   - If the book is not selected, it is added to the list of selected books and its class is changed to `'book-box selected-books'`.

2. **Tracking Selected Books:**
   - The `selectedBooksIDs` array is used to store the IDs of the selected books. The IDs are fetched from each book's hidden input field (`#BookID`).
   - As books are selected or unselected, the array is updated accordingly.

3. **Updating Selection Count:**
   - The number of selected books is dynamically displayed in the `#SelectedNumber` span, which is updated whenever the selection changes.

4. **Updating Selected Books IDs Input:**
   - The `#selectedBooksIDs` hidden input field is updated with a comma-separated list of selected book IDs (`selectedBooksIDs.join(",")`).

This script allows users to select and unselect books from a list, with the number of selected books displayed and stored in a hidden input for further use (e.g., submission to a server).


### edit-list.js

The `edit-list.js` file contains JavaScript that enables the editing of selected books within a list. Here's a breakdown of its features:

1. **Pre-selecting Books:**
   - When the page loads, any books that are initially marked as selected (having the class `selected-books`) are processed.
   - The IDs of these selected books are pushed into the `selectedBooksIDs` array, and the hidden input field (`#selectedBooksIDs`) is updated with a comma-separated list of selected book IDs.

2. **Book Selection and Deselecting:**
   - The script listens for clicks on each book box (`.book-box`). When a book is clicked:
     - If the book is already selected (its ID exists in `selectedBooksIDs`), it is deselected, its class is reset to `'book-box'`, and its ID is removed from the array.
     - If the book is not selected, it is added to the selected books list, its class is changed to `'book-box selected-books'`, and its ID is added to the array.

3. **Tracking Selected Books:**
   - The `selectedBooksIDs` array keeps track of the IDs of the currently selected books.
   - The selection count is dynamically updated in the `#SelectedNumber` span to reflect the number of selected books.

4. **Updating Selected Books IDs Input:**
   - The hidden input field (`#selectedBooksIDs`) is updated with a comma-separated list of selected book IDs every time a book is selected or deselected.

This script allows users to modify the selection of books within a list, with the selected books' IDs stored and displayed for further processing.





## Acknowledgements

I am **Mohamed Ashraf Ramadan**, the creator of this project, and I would like to thank Harvard University for the CS50 Web course that helped me develop this project. I hope you enjoy it and I look forward to your feedback.