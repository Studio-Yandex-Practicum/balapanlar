function scrollToAnchor(link, headerSelector = null, pixelOffset = 0) {
	link.addEventListener('click', function(evt) {
			evt.preventDefault();

			const href = this.getAttribute('data-attribute-anchor');
			const scrollTarget = document.getElementById(href);

			let topOffset = pixelOffset;

			if (headerSelector) {
				topOffset = document.querySelector(headerSelector).offsetHeight;
			}

			const elementPosition = scrollTarget.getBoundingClientRect().top;
			const offsetPosition = elementPosition - topOffset;

			window.scrollBy({
					top: offsetPosition,
					behavior: 'smooth'
			});
	});
}

export { scrollToAnchor }
