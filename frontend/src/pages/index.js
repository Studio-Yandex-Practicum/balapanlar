import './index.css';
import { PopupWithCourse } from '../components/PopupWithCourse.js';
import { PopupWithPartner } from '../components/PopupWithPartner.js';
import { PopupWithBurger } from '../components/PopupWithBurger.js';
import { checkScreenWidth } from '../components/headerState.js';
import { Tween } from '../components/tween.js';
import { scrollToAnchor } from '../components/anchorLinkScroll.js';
import { PopupHowToFind } from '../components/PopupHowToFind';
import '../components/howToFindMap.js';
import '../components/faq.js';

//--- no-js ---

document.querySelector("html").classList.remove("no-js");

//--- popupHeader ---

const popupHeader = new PopupWithBurger('.popup_type_header');

checkScreenWidth(popupHeader);

window.addEventListener('resize', () => checkScreenWidth(popupHeader));

popupHeader.burgerButton.addEventListener(
	'mousedown',
	popupHeader.toggleBurgerMenu
);

//--- popupCourses ---

const popup = new PopupWithCourse('.popup_type_course');

document.querySelectorAll('.course-card__popup-button').forEach((btn) => {
	btn.addEventListener('mousedown', () => {
		popup.open(btn.closest('.course-card').cloneNode(true).innerHTML);
	});
});

//--- popupPartners ---

const popupPartner = new PopupWithPartner('.popup_type_partner');

const partners = document.querySelectorAll('.partners__partner-item');
partners.forEach((partner) => {
	partner.addEventListener('click', (evt) => {
		popupPartner.open(partner.cloneNode(true));
	});
});

const howToFind = new PopupHowToFind('.popup_type_how-to-find')

document.querySelector('.button_for_how-to-find').addEventListener('click',function(){
	howToFind.open();
})

// --- HorizontalScroll settings objects ---

	const principlesTweenData = {
		selector: '.principles',
		horizontalShift: -66.66666666,
		triggerSelector: '.principles',
		start: '80px top',
		snap: .5,
		pinState: true,
	};

	const principlesHeadingTweenData = {
		selector: '.principles__heading',
		horizontalShift: 66.66666666,
		triggerSelector: '.principles',
		start: '80px top',
		snap: .5,
		pinState: false,
	};

	let cardsWidthSum = 0
	document.querySelectorAll('.advantages__card').forEach(function(item){
		cardsWidthSum += item.offsetWidth;
	})
	const advantagesPadding = parseInt(window.getComputedStyle(document.querySelector('.advantages')).paddingLeft)
	const advantagesWidth = cardsWidthSum + document.querySelector('.advantages__title').offsetWidth + advantagesPadding + 40*4;
	const advantagesTweenData = {
		selector: '.advantages__content',
		horizontalShift: -100 * (1 - window.innerWidth / (advantagesWidth + window.innerWidth/1.5)),
		triggerSelector: '.advantages',
		start: 'center center',
		pinState: true,
	};

// --- horizontalScroll init ---
if (window.innerWidth > 768) {
	const principlesTween = new Tween(principlesTweenData);
	const principlesHeadingTween = new Tween(principlesHeadingTweenData);
	const advantagesTween = new Tween(advantagesTweenData);

	principlesTween.toggleTween();
	principlesHeadingTween.toggleTween();
	advantagesTween.toggleTween();
};

var cachedWidth = window.innerWidth;

window.addEventListener('resize', () => {
	if (cachedWidth != window.innerWidth)	{
		document.location.reload();
		cachedWidth = window.innerWidth;
	};
});

document
	.querySelectorAll('[data-attribute-anchor]')
	.forEach((link) => scrollToAnchor(link));
