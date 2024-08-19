import React from "react";
import trees from "../../assets/trees.jpg";
import paris from "../../assets/paris.jpg";
import grand from "../../assets/grand.jpg";
import ice from "../../assets/ice.jpg";
import ny from "../../assets/ny.jpg";
import baloon from "../../assets/baloon.jpg";
import desert from "../../assets/desert.jpg";
import lake from "../../assets/lake.jpg";
import BackgroundSlider from "react-background-slider";

export const BackgroundSliderCustom = () => {
  return (
    <BackgroundSlider
      images={[lake, trees, paris, grand, ice, ny, desert, baloon]}
      duration={8}
      transition={1}
    />
  );
};
