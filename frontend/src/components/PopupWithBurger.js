import { Popup } from './Popup.js';

export class PopupWithBurger extends Popup {
	constructor(popupSelector) {
		super(popupSelector);
		this.burgerButton = document.querySelector('.burger-button');
		this._burgerButtonElements = this.burgerButton.querySelectorAll('.burger-button__line-element');
	}

	open() {
		this._popup.classList.add('popup_opened');
		this._setEventListeners();
		this._activateBurgerButton();
	}

	close() {
		this._popup.classList.remove('popup_opened');
		this._removeEventListeners();
		this._deactivateBurgerButton();
	}

	toggleBurgerMenu = () => {
		this._popup.classList.contains('popup_opened') ? this.close() : this.open();
	}

	_handlePressClick = (evt) => {
		if (!evt.target.classList.contains('popup_opened') &&
			!evt.target.classList.contains('logo_type_header-animals') &&
			!evt.target.classList.contains('burger-button') &&
			!evt.target.classList.contains('burger-button__line-element')
		) {
			setTimeout(() => {this.close()}, 200);
		}
	};

	_setEventListeners() {
		document.addEventListener('mousedown', this._handlePressClick);
		document.addEventListener('keydown', this._handlePressEsc);
	}

	_removeEventListeners() {
		document.removeEventListener('mousedown', this._handlePressClick);
		document.removeEventListener('keydown', this._handlePressEsc);
	}

	_deactivateBurgerButton() {
		this._burgerButtonElements.forEach(function(element) {
			element.classList.remove('burger-button__line-element_active');
		});
	}

	_activateBurgerButton() {
		this._burgerButtonElements.forEach(function(element) {
			element.classList.add('burger-button__line-element_active');
		});
	}
}
