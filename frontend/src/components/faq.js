const faqQuestionOpened = ()=>document.querySelectorAll('.faq-qst_opened');
const faqQuestions = document.querySelectorAll('.faq-qst');
let focusable = true;
let resizeId;

function hideFaqTexts(faq){
	const answers = faq.querySelectorAll('.faq-qst__text');
	answers.forEach(element => {
		element.classList.remove('faq-qst__text_show');
	});
}

function setTabUrl(urls, status){
	urls.forEach(element => {
		if(status){
			element.setAttribute('tabindex', '0');
		}else{
			element.setAttribute('tabindex', '-1');
		}
	});
}

function closeFaqs() {
	faqQuestionOpened().forEach(faq => {
		faq.classList.remove('faq-qst_opened');
		const plus = faq.querySelector('.faq-qst__plus');
		const urls = faq.querySelectorAll('.faq-qst__email');
		const button = faq.querySelector('.faq-qst__button');
		plus.classList.remove('faq-qst__plus_opened');
		button.classList.remove('faq-qst__button_active');
		setTabUrl(urls, false);
		hideFaqTexts(faq);
		faq.style.height = `${parseInt(faq.dataset.qh)}px`;
	});
}

function openFaq(faq) {
	if(!faq.classList.contains('faq-qst_opened')){
		closeFaqs();
		faq.classList.add('faq-qst_opened');
		const answers = faq.querySelectorAll('.faq-qst__text');
		const plus = faq.querySelector('.faq-qst__plus');
		const button = faq.querySelector('.faq-qst__button');
		const urls = faq.querySelectorAll('.faq-qst__email');
		setTabUrl(urls, true);
		button.classList.add('faq-qst__button_active');
		plus.classList.add('faq-qst__plus_opened');
		answers.forEach(element => {
			element.classList.add('faq-qst__text_show');
		});
		faq.style.height = `${parseInt(faq.dataset.qh) + parseInt(faq.dataset.ah)}px`;
	}else{
		closeFaqs();
	}
}

function getHeightsElem(element) {
	const question = element.querySelector('.faq-qst__question');
	const answers = element.querySelectorAll('.faq-qst__text');
	let answersHeight = 0;
	answers.forEach(answ => {
		answersHeight += answ.offsetHeight;
	});
	return {qh: question.offsetHeight, ah: answersHeight};
}

function buttonsBlur(){
	const buttons = document.querySelectorAll('.faq-qst__button');
	buttons.forEach(element => {
		element.blur();
	});
}

function resizeFaq() {
	faqQuestions.forEach(element => {
		const button = element.querySelector('.faq-qst__button');
		const heights = getHeightsElem(element);
		element.dataset.qh = heights.qh;
		element.dataset.ah = heights.ah;
		button.style.height = `${heights.qh}px`;
		if(element.classList.contains('faq-qst_opened')){
			element.style.height = `${parseInt(element.dataset.qh) + parseInt(element.dataset.ah)}px`;
		}else{
			element.style.height = `${parseInt(element.dataset.qh)}px`;
		}
	});
	buttonsBlur();
}

function focusFaqButton(element, status){
	if(!focusable||!status){
		element.classList.remove('faq-qst_focused');
	}else{
		element.classList.add('faq-qst_focused');
	}
}

function initFaq() {
	faqQuestionOpened().forEach(element => {
		const button = element.querySelector('.faq-qst__button');
		const heights = getHeightsElem(element);
		element.dataset.qh = heights.qh;
		element.dataset.ah = heights.ah;
		button.style.height = `${heights.qh}px`;
		button.addEventListener('pointerdown', ()=>{
			focusable=false;
			focusFaqButton(element, false)
		});
		button.addEventListener('click', ()=>{
			focusable=true;
			openFaq(element);
		});
		button.addEventListener('focus', ()=>focusFaqButton(element, true));
		button.addEventListener('blur', ()=>focusFaqButton(element, false));
	});
	closeFaqs();
}

window.addEventListener('load', ()=>initFaq());
window.addEventListener('resize', function() {
		clearTimeout(resizeId);
		resizeId = setTimeout(resizeFaq, 500);
});
