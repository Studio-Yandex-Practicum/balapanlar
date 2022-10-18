var myMap;
ymaps.ready(init);
function init () {
	myMap = new ymaps.Map('map', {
				center: [44.321946, 41.919865],
				zoom: 15,
				controls: ['zoomControl']
			},{
				searchControlProvider: 'yandex#search'
			});
		myMap.behaviors.disable(['rightMouseButtonMagnifier'])
		myMap.options.set('scrollZoomSpeed', 3);
	var myPlacemark = new ymaps.Placemark(
			[44.321946, 41.919865]
		);
	myMap.geoObjects.add(myPlacemark);
}
