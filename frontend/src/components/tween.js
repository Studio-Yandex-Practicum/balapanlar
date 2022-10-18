import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

class Tween {
	constructor(tweenData) {
		this.data = tweenData;
		this.tween = gsap.to(tweenData.selector, {
			xPercent: tweenData.horizontalShift,
			ease: "none",
			scrollTrigger: {
				trigger: this.data.triggerSelector,
				pin: tweenData.pinState,
				start: tweenData.start || 'top top',
				scrub: 1,
				snap: tweenData.snap,
				end: "bottom",
			},
		});
	}

	toggleTween = () => {
		if (window.innerWidth <= 768) {
			this.tween.scrollTrigger.disable();
		} else {
			this.tween.scrollTrigger.enable();
		}
	};
}

export { Tween };
