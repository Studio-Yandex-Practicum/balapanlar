import { Popup } from './Popup.js';

export class PopupHowToFind extends Popup {
	constructor(popupSelector) {
		super(popupSelector);
		this.openButton = document.querySelector('.button_for_how-to-find');
	}

	_handlePressClick = (evt) => {
		if (evt.target != document.querySelector('.popup__fullscreen-image')) {
			setTimeout(() => {this.close()}, 100);
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
}
