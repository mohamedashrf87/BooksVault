const imageInputLabel = document.getElementById('imageInputLabel');
const preview = document.getElementById('imagePreview');

preview.style.width = `${imageInputLabel.offsetWidth}px`;
preview.style.height = `${imageInputLabel.offsetHeight}px`;
preview.style.borderRadius = '5px';

document.getElementById('imageInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file && file.type.startsWith('image/')) { 
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.src = e.target.result;
            preview.style.width = `${imageInputLabel.offsetWidth}px`;
            preview.style.height = `${imageInputLabel.offsetHeight}px`;
            preview.style.borderRadius = '5px';
            preview.style.display = 'block';
            document.querySelector('#imageInputP').style.display = 'none';
            imageInputLabel.appendChild(preview);
        };
        reader.readAsDataURL(file);
    } else {
        alert("Please select an image file.");
    }
});

let authorsValues = [];
const authorsValuesInput = document.getElementById('authorsValues');
const chosenAuthors = document.getElementById('chosenAuthors');
const authorsInput = document.getElementById('authorsInput');
const authorsList = document.getElementById('authorsList');
const authorsListNames = authorsList.querySelectorAll('.authors-names');
const authorsSelectedNames = authorsList.querySelectorAll('.selected-authors');

Array.from(authorsSelectedNames).forEach(function(element) {
    authorsList.removeChild(element);
    chosenAuthors.appendChild(element);
    authorsValues.push(element.innerText);
    authorsValuesInput.value = authorsValues.join(",");
});

authorsInput.onfocus = function(){
    authorsInput.style.borderRadius = '5px 5px 0px 0px';
    authorsList.style.display = 'block';
}
authorsInput.onblur = function(){
    authorsInput.style.borderRadius = '5px';
    authorsList.style.display = 'none';
}

chosenAuthors.addEventListener('mousedown', function(event) {
    event.preventDefault();
    authorsInput.focus();
});
authorsList.addEventListener('mousedown', function(event) {
    event.preventDefault();
    authorsInput.focus();
});

authorsInput.onkeyup = function() {
    authorsSearch()
}
authorsInput.onkeydown = function() {
    authorsSearch()
}

Array.from(authorsListNames).forEach(function(element) {
    element.onclick = function() {
        if (authorsValues.length < 3) {
            if (chosenAuthors.contains(element)) {
                chosenAuthors.removeChild(element);
                authorsList.appendChild(element);
                authorsValues.splice(authorsValues.indexOf(element.innerText), 1);

                authorsValuesInput.value = authorsValues.join(",");
            } else {
                authorsList.removeChild(element);
                chosenAuthors.appendChild(element);
                authorsValues.push(element.innerText);

                authorsValuesInput.value = authorsValues.join(",");
            }
        } else if (chosenAuthors.contains(element)) {
            chosenAuthors.removeChild(element);
            authorsList.appendChild(element);
            authorsValues.splice(authorsValues.indexOf(element.innerText), 1);
            
        }
        authorsInput.style.paddingLeft = (chosenAuthors.offsetWidth) + 'px';
        authorsInput.value = '';
    };
});


function checkIfThereIsAuthorsNames() {
    let allHidden = true;
    authorsListNames.forEach((p) => {
        if (window.getComputedStyle(p).display !== 'none') {
            allHidden = false;
        }
    });
    if (allHidden) {
        document.querySelector('#authorsListNoResults').style.display = 'block';
    } else {
        document.querySelector('#authorsListNoResults').style.display = 'none';
    }
}

function authorsSearch() {
    Array.from(authorsListNames).forEach(function(element) {
        if (!chosenAuthors.contains(element)) {
            if (element.innerText.toLowerCase().includes(authorsInput.value.toLowerCase())) {
                element.style.display = 'block'; 
            } else {
                element.style.display = 'none';
            }
        }
    });

    checkIfThereIsAuthorsNames()
}
