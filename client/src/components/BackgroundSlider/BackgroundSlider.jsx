import React, { useState, useEffect } from "react";
import css from "./BackgroundSlider.module.css";

const images = ["trees.jpg", "paris.jpg", "ice.jpg", "ny.jpg", "greece.jpg"];

const BackgroundSlider = () => {
  const [currentImage, setCurrentImage] = useState(0);
  const [nextImage, setNextImage] = useState(images[1]);
  const [isTransitioning, setIsTransitioning] = useState(false);

  useEffect(() => {
    const interval = setInterval(() => {
      setIsTransitioning(true);

      setNextImage(images[(currentImage + 1) % images.length]);

      setTimeout(() => {
        setCurrentImage((currentImage + 1) % images.length);
        setIsTransitioning(false);
      }, 1000); // Duration of the transition in milliseconds
    }, 8000); // Interval for changing images

    return () => clearInterval(interval);
  }, [currentImage]);

  return (
    <div className={css.backgroundSlider}>
      <div
        className={`${css.backgroundImage} ${
          isTransitioning ? css.fadeOut : css.fadeIn
        }`}
        style={{ backgroundImage: `url(${images[currentImage]})` }}
      ></div>
      <div
        className={`${css.backgroundImage} ${
          isTransitioning ? css.fadeIn : css.fadeOut
        }`}
        style={{ backgroundImage: `url(${nextImage})` }}
      ></div>
    </div>
  );
};

export default BackgroundSlider;
