const myHeading = document.querySelector('h1');

function changeTitle() {
    myHeading.textContent = 'Greetings young padawan!';
}

let li1 = document.getElementById('li1');
let li2 = document.getElementById('li2');
li1.textContent = 'Pauline'
li2.textContent = '& Zoey'

function swapPlaces() {
    if (li1.textContent === 'Pauline') {
        li1.textContent = 'Zoey', li2.textContent = '& Pauline'
    } else {
        li1.textContent = 'Pauline', li2.textContent = '& Zoey'
    }
}

setTimeout(changeTitle, 3000)
setInterval(swapPlaces, 1000)

/*document.querySelector('html').addEventListener('click', function() {
    alert('Ouch! Stop poking me!');
  });*/

let catImage = document.getElementById('cats');

catImage.onclick = function changeCat() {
  let catSrc = catImage.getAttribute('src');
  if (catSrc === 'images/cat.jpg') {
    catImage.setAttribute('src', 'images/cat2.jpg');
  }
  else if (catSrc === 'images/cat2.jpg') {
    catImage.setAttribute('src', 'images/cat3.jpg');
  }
  else {
    catImage.setAttribute('src', 'images/cat.jpg');
  }
}

let mysteriousButton = document.querySelector('button');

function mysteriousButtonAction() {
    let myName = prompt('whats your name?');
    localStorage.setItem('name', myName);
    myHeading.textContent = 'Greetings ' + myName
}

mysteriousButton.onclick = function() {
    mysteriousButtonAction();
}

/* function testForGitHub() {}*/
