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
    let myName = prompt('whats your name then?');
    localStorage.setItem('name', myName);
    myHeading.textContent = 'Greetings ' + myName
}

mysteriousButton.onclick = function() {
    mysteriousButtonAction();
}

let computersChoice = document.getElementById("BotChoice");
let yourChoice = document.getElementById("PlayerChoice");

let stoneButton = document.getElementById('stone');
let paperButton = document.getElementById('paper');
let scissorsButton = document.getElementById('scissors');

function randomStonePaperScissors() {
  let randomNumber = Math.floor(Math.random() * (3) + 1);
  if (randomNumber === 1) {
    computersChoice.textContent = 'Stone'
  }
  else if (randomNumber === 2) {
    computersChoice.textContent = 'Paper'
  }
  else {computersChoice.textContent = 'Scissors'}
}

function stoneButtonAction() {
  yourChoice.textContent = 'Stone';
  randomStonePaperScissors();
}
stoneButton.onclick = function () {
  stoneButtonAction();
}

function paperButtonAction() {
  yourChoice.textContent = 'Paper';
  randomStonePaperScissors();
}
paperButton.onclick = function () {
  paperButtonAction();
}

function scissorsButtonAction() {
  yourChoice.textContent = 'Scissors';
  randomStonePaperScissors();
}
scissorsButton.onclick = function () {
  scissorsButtonAction();
}
