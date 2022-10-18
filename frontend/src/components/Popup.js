import scrollLock from 'scroll-lock';

class Popup {
	constructor(popupSelector) {
		this._popup = document.querySelector(popupSelector);
		this._popupContainer = this._popup.querySelector('.popup__container');
		this._closeBtns = this._popup.querySelectorAll('.popup__close-button');
		this.__addEventToBtns();
	}

	open() {
		this._popup.classList.add('popup_opened');
		this._popupContainer.classList.add('popup__container_opened');
		this._setEventListeners();
		this.__removeTabsFromDoc();
		this.__setTabsFromPopup();
		this.__setTabsFromPopup();
		scrollLock.disablePageScroll();
	}

	close() {
		this.__setTabsFromDoc();
		this._popup.classList.remove('popup_opened');
		this._popupContainer.classList.remove('popup__container_opened');
		this._removeEventListeners();
		scrollLock.enablePageScroll();
	}

	_handlePressEsc = (evt) => {
		if (evt.key === 'Escape') {
			this.close();
		}else if(!(evt.key === 'Tab')){
			evt.preventDefault();
		}
	};

	_handlePressClick = (evt) => {
		if (
			evt.target.classList.contains('popup_opened') ||
			evt.target.classList.contains('button') ||
			evt.target.classList.contains('popup__close-button')
		) {
			setTimeout(() => {this.close()}, 100);
		}
	};

	_setEventListeners() {
		this._popup.addEventListener('mousedown', this._handlePressClick);
		document.addEventListener('keydown', this._handlePressEsc);
	}

	_removeEventListeners() {
		this._popup.removeEventListener('mousedown', this._handlePressClick);
		document.removeEventListener('keydown', this._handlePressEsc);
	}

	// убираем табуляцию из документа

	__removeTabsFromDoc(){
		const els = document.querySelectorAll('a, link, button, input, select, textarea');
		els.forEach(element => {
			element.setAttribute('tabindex', '-1');
		});
	}

	// возвращаем штатную табуляцию из документа

	__setTabsFromDoc(){
		const els = document.querySelectorAll('a, link, button, input, select, textarea');
		els.forEach(element => {
			element.removeAttribute('tabindex');
		});
	}

	// устанавливаем табуляцию в попапе

	__setTabsFromPopup(){
		const els = this._popup.querySelectorAll('a, link, button, input, select, textarea');
		els.forEach(element => {
			element.removeAttribute('tabindex');
		});
	}

	_handleKeyPress = (evt) => {
		if (evt.key === 'Enter' || evt.keyCode === 13 || evt.key === ' ' || evt.keyCode === 32) {
			this.close();
		}
	};

	__addEventToBtns(){
		this._closeBtns.forEach(element => {
			element.addEventListener('keydown', this._handleKeyPress);
		});
	}

}

export { Popup };
