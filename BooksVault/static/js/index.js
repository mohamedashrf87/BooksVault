const gridDisplayIcon = document.getElementById('gridDisplayIcon');
const listDisplayIcon = document.getElementById('listDisplayIcon');
const booksContainer = document.getElementById('booksContainer');
let gridDisplayIconPath = gridDisplayIcon.querySelector('path');
let listDisplayIconPath = listDisplayIcon.querySelector('path');

gridDisplayIcon.onclick = function() {
    // Array(gridDisplayIconPath).forEach(path) {
    //     path.style.stroke = 'var(--selected-icons)';
    // };
    // Array(listDisplayIconPath).forEach(path) {
    //     path.style.stroke = 'var(--icons)';
    // };
    booksContainer.className = 'books-container grid';
}

listDisplayIcon.onclick = function() {
    // Array(listDisplayIcon).forEach(path) {
    //     path.style.stroke = 'var(--selected-icons)';
    // };
    // Array(gridDisplayIconPath).forEach(path) {
    //     path.style.stroke = 'var(--icons)';
    // };
    booksContainer.className = 'books-container list';
}