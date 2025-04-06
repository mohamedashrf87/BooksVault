(() => {
  const optionsIcon = document.querySelector("#optionsIcon");
  const blurForOptions = document.querySelector("#blurForOptions");
  const optionsContainer = document.querySelector("#optionsContainer");

  optionsIcon.onclick = function () {
    blurForOptions.style.display = 'block';
    optionsContainer.style.display = 'flex';
  };

  const newAuthorOpenForm = document.getElementById('newAuthorOpenForm');
  const newAuthorForm = document.getElementById('newAuthorForm');
  const newPublisherOpenForm = document.getElementById('newPublisherOpenForm');
  const newPublisherForm = document.getElementById('newPublisherForm');

  newAuthorOpenForm.onclick = function () {
    document.querySelector('#authorName').value = '';
    document.querySelector('#Biography').value = '';
    blurForOptions.style.display = 'block';
    newAuthorForm.style.display = 'block';
    optionsContainer.style.display = 'none';
  };

  newPublisherOpenForm.onclick = function () {
    document.querySelector('#publisherName').value = '';
    document.querySelector('#Address').value = '';
    blurForOptions.style.display = 'block';
    newPublisherForm.style.display = 'block';
    optionsContainer.style.display = 'none';
  };

  blurForOptions.onclick = function () {
    blurForOptions.style.display = 'none';
    optionsContainer.style.display = 'none';
    newAuthorForm.style.display = 'none';
    newPublisherForm.style.display = 'none';
  };

  newAuthorForm.addEventListener('submit', function (event) {
    event.preventDefault();

    const authorName = document.querySelector('#authorName').value;
    const Biography = document.querySelector('#Biography').value;

    if (!authorName || !Biography) {
      alert("Please fill out all fields.");
      document.querySelector('#authorName').value = '';
      document.querySelector('#Biography').value = '';
      blurForOptions.style.display = 'block';
      newAuthorForm.style.display = 'block';
      optionsContainer.style.display = 'none';
      return;
    }

    fetch('/books/vault/new/author', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: authorName, biography: Biography }),
    })
      .then(response => response.json())
      .then(data => {})
      .catch(error => console.log('Error:', error));

    location.reload();
  });

  newPublisherForm.addEventListener('submit', function (event) {
    event.preventDefault();

    const publisherName = document.querySelector('#publisherName').value;
    const Address = document.querySelector('#Address').value;

    if (!publisherName || !Address) {
      alert("Please fill out all fields.");
      document.querySelector('#publisherName').value = '';
      document.querySelector('#Address').value = '';
      blurForOptions.style.display = 'block';
      newAuthorForm.style.display = 'block';
      optionsContainer.style.display = 'none';
      return;
    }

    fetch('/books/vault/new/publisher', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: publisherName, address: Address }),
    })
      .then(response => response.json())
      .then(data => {})
      .catch(error => console.log('Error:', error));

    location.reload();
  });

  const toggleButton = document.getElementById('toggleButton');

  function makeImagesDarkmode() {
    const authorsImg = document.getElementById('authorsImg');
    if (authorsImg) {
      authorsImg.src = authorsImg.getAttribute('data-darkmode-src');
    }
  }

  function makeImageslightmode() {
    const authorsImg = document.getElementById('authorsImg');
    if (authorsImg) {
      authorsImg.src = authorsImg.getAttribute('data-lightmode-src');
    }
  }

  if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark-mode');
    makeImagesDarkmode();
  }

  toggleButton.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');

    const theme = document.body.classList.contains('dark-mode') ? 'dark' : 'light';
    if (theme === 'dark') {
      makeImagesDarkmode();
    } else {
      makeImageslightmode();
    }

    localStorage.setItem('theme', theme);
  });

  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.addEventListener('focus', function () {
      searchInput.setAttribute('placeholder', 'Title / ISBN');
    });
    searchInput.addEventListener('blur', function () {
      searchInput.setAttribute('placeholder', 'Search');
    });
  }
})();
