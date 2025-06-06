function toggleNav() {
  const navMenu = document.querySelector('.nav-menu');
  if (navMenu.style.display === 'none' || navMenu.style.display === '') {
    navMenu.style.display = 'block'; // Exibe o menu
  } else {
    navMenu.style.display = 'none'; // Oculta o menu
  }
}
let currentIndex = 0;
const carousel = document.getElementById('carousel');
const totalImages = carousel.children.length;

function updateCarousel() {
  carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
}
function prevSlide() {
  currentIndex = (currentIndex - 1 + totalImages) % totalImages;
  updateCarousel();
}
function nextSlide() {
  currentIndex = (currentIndex + 1) % totalImages;
  updateCarousel();
}


let toqueinicial = 0;
let toquefinal = 0;

carousel.addEventListener('touchstart', (e) => {
  toqueinicial = e.changedTouches[0].screenX;
});

carousel.addEventListener('touchend', (e) => {
  toquefinal = e.changedTouches[0].screenX;
  handleGesture();
});

function handleGesture() {
  const swipeDistance = toquefinal - toqueinicial;
  const swipeThreshold = 50; 

  if (swipeDistance > swipeThreshold) {
  
    prevSlide();
  } else if (swipeDistance < -swipeThreshold) {
  
    nextSlide();
  }
  
}
const slidesData = [
  {
    title: "alguma coisa",
    content: "lorem ipsum"
  },
  {
    title: "alguma coisa",
    content: "lorem ipsum"
  },
  {
    title: "alguma coisa",
    content: "lorem ipsum"
  }
];



function updateCarousel() {
  carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
  updateText();
}

function updateText() {
  const textTitle = document.getElementById('text-title');
  const textContent = document.getElementById('text-content');
  const dynamicText = document.getElementById('dynamic-text');
  
  if (!textTitle || !textContent || !dynamicText) return;
  
  
  dynamicText.classList.add('text-fade-out');
  
  
  setTimeout(() => {
    textTitle.textContent = slidesData[currentIndex].title;
    textContent.textContent = slidesData[currentIndex].content;
    
    
    dynamicText.classList.remove('text-fade-out');
    dynamicText.classList.add('text-fade-in');
    
    setTimeout(() => {
      dynamicText.classList.remove('text-fade-in');
    }, 300);
  }, 150);
}

function prevSlide() {
  currentIndex = (currentIndex - 1 + totalImages) % totalImages;
  updateCarousel();
}

function nextSlide() {
  currentIndex = (currentIndex + 1) % totalImages;
  updateCarousel();
}



document.addEventListener('DOMContentLoaded', () => {
  updateText();
});



let corPadrao = "#e2e1de";
const imgPadrao = document.getElementById("mudar-imagem");
const botaoMudarCor = document.getElementById('mudar-cor');
const iconeSol = "./src/assets/Sol.png";
const iconeLua = "./src/assets/Lua.png";


function mudarTema() {
    if (corPadrao === "#e2e1de") {
        document.body.style.backgroundColor = "#001233";
        if (imgPadrao) imgPadrao.setAttribute("src", iconeSol);
        corPadrao = "#001233";
    } else {
        document.body.style.backgroundColor = "#e2e1de";
        if (imgPadrao) imgPadrao.setAttribute("src", iconeLua);
        corPadrao = "#e2e1de";
    }
}
if (botaoMudarCor && imgPadrao) {
    botaoMudarCor.addEventListener('click', mudarTema);
}

// mudança de cores da pagina pt 2

const coresDaFesta = ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#00ffff"];

let festaIntervalId = null;

function trocaDeCores() {

    if (festaIntervalId !== null) {
        clearInterval(festaIntervalId);
    }

    let repeticoes = 0;
    const maxRepeticoes = 30;
    const intervaloEntreCores = 350; 
    let i = 0;

    festaIntervalId = setInterval(function() {
        
        if (repeticoes >= maxRepeticoes) {
            clearInterval(festaIntervalId); 
            festaIntervalId = null; 
            document.body.style.backgroundColor = '#e2e1de'; 
            return; 
        }

        document.body.style.backgroundColor = coresDaFesta[i];

        i++;
        
        if (i >= coresDaFesta.length) {
            i = 0;
        }
        repeticoes++;

    }, intervaloEntreCores);
}

const festaNoSite = document.getElementById("festa");

if (festaNoSite) {
    festaNoSite.addEventListener("click", trocaDeCores);
}