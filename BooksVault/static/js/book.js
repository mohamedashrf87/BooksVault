(() => {
  const bookOptionsIcon = document.querySelector("#bookOptionsIcon");
  const bookOptionsContainer = document.querySelector("#bookOptionsContainer");
  const bookOptionsExit = document.querySelector("#bookOptionsExit");

  bookOptionsIcon.onclick = function () {
    bookOptionsContainer.style.display = 'flex';
    bookOptionsExit.style.display = 'block';
  };

  bookOptionsExit.onclick = function () {
    bookOptionsExit.style.display = 'none';
    bookOptionsContainer.style.display = 'none';
  };
})();