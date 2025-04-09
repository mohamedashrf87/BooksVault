const gridDisplayIcon = document.getElementById('gridDisplayIcon');
const listDisplayIcon = document.getElementById('listDisplayIcon');
const booksContainer = document.getElementById('booksContainer');
let gridDisplayIconPath = gridDisplayIcon.querySelector('path');
let listDisplayIconPath = listDisplayIcon.querySelector('path');

gridDisplayIcon.onclick = function() {
    booksContainer.className = 'books-container grid';
}

listDisplayIcon.onclick = function() {
    booksContainer.className = 'books-container list';
}