const booksBoxs = document.querySelectorAll('.book-box');
const SelectedBooksBoxs = document.querySelectorAll('.selected-books');
const SelectedNumber = document.getElementById('SelectedNumber').querySelector('span');
const selectedBooksIDsInput = document.getElementById('selectedBooksIDs');
let selectedBooksIDs = [];

Array.from(SelectedBooksBoxs).forEach(function(element) {
    const bookID = element.querySelector('#BookID').value;
    selectedBooksIDs.push(bookID);
    selectedBooksIDsInput.value = selectedBooksIDs.join(",");
});

Array.from(booksBoxs).forEach(function(book) {
    const bookID = book.querySelector('#BookID').value;
    book.onclick = function() {
        if (selectedBooksIDs.includes(bookID)) {
            book.className = 'book-box';
            selectedBooksIDs.splice(selectedBooksIDs.indexOf(bookID), 1);
        } else {
            book.className = 'book-box selected-books';
            selectedBooksIDs.push(bookID);
        }
        SelectedNumber.innerHTML = selectedBooksIDs.length;
        selectedBooksIDsInput.value = selectedBooksIDs.join(",");
    }
});
