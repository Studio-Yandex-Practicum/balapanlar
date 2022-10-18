const header = document.querySelector('.header');
const headerLogo = header.querySelector('.logo');
const firstSection = document.getElementsByTagName('section')[0];
const headerStandartPadding = '10px';
const headerNarrowPadding = '18px';
const headerTabletPadding = '24px';
const headerMobilePadding = '12px';
const compensatePadding = '48px';
const initialPadding = '0';
const burgerWidth = 1110;
const mobileWidth = 480;

function setAnimalLogo() {
	headerLogo.classList.remove('logo_type_header-text');
	headerLogo.classList.add('logo_type_header-animals');
}

function setTextLogo() {
	headerLogo.classList.remove('logo_type_header-animals');
	headerLogo.classList.add('logo_type_header-text');
}

function toggleHeaderState() {
	const scroll = window.pageYOffset;
	if (scroll > 0) {
		setTextLogo();
		header.style.paddingBottom = headerNarrowPadding;
		firstSection.style.paddingTop = compensatePadding;
	}
	if (scroll === 0) {
		setAnimalLogo();
		header.style.paddingBottom = headerStandartPadding;
		firstSection.style.paddingTop = initialPadding;
	}
}

function checkScreenWidth(popup) {
	const screenWidth = window.innerWidth;
	if (screenWidth > burgerWidth) {
		toggleHeaderState();
		document.addEventListener('scroll', toggleHeaderState);
		setAnimalLogo();
		popup.close();
	}
	else {
		document.removeEventListener('scroll', toggleHeaderState);
		setTextLogo();
		firstSection.style.paddingTop = initialPadding;
		if (screenWidth > mobileWidth) {
			header.style.paddingBottom = headerTabletPadding;
		}
		else {
			header.style.paddingBottom = headerMobilePadding;
		}
	}
}

export { checkScreenWidth }
