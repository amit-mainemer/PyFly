import React from "react";
import { Avatar } from "@mui/material";

export const UserAvatar = ({ text, onClick = null }) => {
  return (
    <Avatar
      sx={{ bgcolor: "#009688", ...(onClick && { cursor: "pointer" }) }}
      onClick={onClick}
    >
      {text}
    </Avatar>
  );
};
