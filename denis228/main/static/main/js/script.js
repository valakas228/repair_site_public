var IsMenuShow = false;
var IsMenuShow2 = false;
var IsMenuShow3 = false;
var IsMenuShow4 = false;
var IsMenuShow5 = false;
var IsAboutMoreContentShown = false
let offset = 0;







const moreBtns = document.querySelectorAll('.more-btn');

moreBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const product = btn.parentNode;
    const moreInfo = product.querySelector('.more-info');

    moreInfo.classList.toggle('show');
    if (moreInfo.classList.contains('show')) {
      btn.textContent = 'Скрыть';
    } else {
      btn.textContent = 'Подробнее';
    }
  });
});

const btn = document.querySelector('.more-btn');

btn.addEventListener('click', () => {
  btn.classList.add('animated', 'pulse'); 
  setTimeout(() => {
    btn.classList.remove('animated', 'pulse'); 
  }, 1000); 
});

const faqList = document.querySelector('.faq__list');
const faqQuestions = faqList.querySelectorAll('.faq__question');

faqQuestions.forEach((question) => {
  question.addEventListener('click', () => {
    question.classList.toggle('active');
    const answer = question.nextElementSibling;
    if (answer.style.maxHeight) {
      answer.style.maxHeight = null;
    } else {
      answer.style.maxHeight = answer.scrollHeight + 'px';
    }
  });
});


const animatedElements = document.querySelectorAll('.more-btn');

function checkScroll() {
  animatedElements.forEach((element) => {
    const elementTop = element.getBoundingClientRect().top;
    const elementBottom = element.getBoundingClientRect().bottom;

    if (elementTop < window.innerHeight && elementBottom > 0) {
      element.classList.add('animate');
    } else {
      element.classList.remove('animate');
    }
  });
}

window.addEventListener('scroll', checkScroll);
