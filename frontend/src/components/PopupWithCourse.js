import { Popup } from './Popup.js';

export class PopupWithCourse extends Popup {
	constructor(popupSelector) {
		super(popupSelector)
	}

	open(nodeElem) {
		this._changeStyle(nodeElem)
		super.open()
	}

	_changeStyle(nodeElem) {
		const content = this._popup.querySelector('.popup__content')
		content.style.display = 'flex';
		content.innerHTML = nodeElem;
		const btn = content.querySelector('.course-card__popup-button');
		btn.textContent = 'Закрыть';
		btn.addEventListener('mousedown', () => super.close());
		btn.addEventListener('keydown', (evt) => {
			if (evt.key === 'Enter' || evt.keyCode === 13 || evt.key === ' ' || evt.keyCode === 32) {
				super.close()
			}
		});
		if (document.documentElement.clientWidth >= 1000) {
		content.querySelector('.flex-container_type_info').style = 'flex-direction: row';};
		content.querySelector('.course-card__list').className = 'popup__text-skills';
		content.querySelectorAll('.course-card__list-item').forEach(item => {
			item.classList.add('course-card__list-item_popup');
			item.classList.remove('course-card__list-item');
		})
	}
}
