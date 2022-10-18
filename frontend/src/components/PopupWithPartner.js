import { Popup } from './Popup.js';

export class PopupWithPartner extends Popup {
	constructor(popupSelector) {
		super(popupSelector);
	}

	open(nodeElem) {
		const content = this._popup.querySelector('.popup__content');
		content.innerHTML = '';
		const data = nodeElem;
		const linkElement = data.querySelector('.partners__partner-link');
		const image = data.querySelector('.partners__partner-logo');
		image.className = 'popup__partner-image';
		content.append(image);
		const descriptions = data.querySelectorAll('.partners__description');
		descriptions.forEach(description => {
			description.className = 'popup__partner-description';
			content.append(description);
		});
		const openButton = this._popup.querySelector('.button_for_partner');
		openButton.href = linkElement.href;

		super.open()
	}

}
