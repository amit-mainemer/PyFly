import React from "react";
import {
  Box,
  Button,
} from "@mui/material";
import { FlightCard } from "../FlightCard/FlightCard";

export const FlightsList = ({ flights, next, page, prev, pages, refresh }) => {
  return (
    <Box
      className="t-card"
      style={{ opacity: 1, backgroundColor: "#fefefedd" }}
      display={"flex"}
      flexDirection={"column"}
      gap={2}
    >
      {flights.map((flight) => (
        <FlightCard key={flight.id} flight={flight} refresh={refresh}/>
      ))}
      <Box display={"flex"} marginLeft={"auto"} gap={2}>
        {page > 1 && (
          <Button onClick={prev} variant="contained">
            Prev
          </Button>
        )}
        {pages > page && (
          <Button onClick={next} variant="contained">
            Next
          </Button>
        )}
      </Box>
    </Box>
  );
};
