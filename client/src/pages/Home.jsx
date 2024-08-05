import React, { useCallback, useState, useEffect } from "react";
import { Box, Typography } from "@mui/material";
import { FlightsFrom } from "../components/FlightsFrom/FlightsForm";
import { FlightsList } from "../components/FlightsList/FlightsList";
import { api } from "../api";

export const Home = () => {
  const [flights, setFlights] = useState([]);
  const [from, setFrom] = useState("");
  const [to, setTo] = useState("");
  const [date, setDate] = useState("");
  const [page, setPage] = useState(1);
  const [pages, setPages] = useState(0);
  const [countries, setCountries] = useState([]);

  const fetchCountries = useCallback(async () => {
    try {
      const response = await api.get("/countries");
      setCountries(response.data);
    } catch (ex) {
      console.warn(ex);
    }
  }, [setCountries]);

  const fetchFlights = useCallback(async () => {
    try {
      const response = await api.get(
        `/flights?page=${page}&from=${from}&to=${to}&date=${date}`
      );
      setFlights(response.data.flights);
      setPages(response.data.pages);
    } catch (ex) {
      console.warn(ex);
    }
  }, [setFlights, page, from, to, date]);

  const searchFlights = ({ from, to, date }) => {
    setPage(1);
    setDate(date);
    setFrom(from);
    setTo(to);
  };

  useEffect(() => {
    fetchCountries();
  }, []);

  useEffect(() => {
    fetchFlights();
  }, [page, from, to, date]);

  return (
    <Box
      style={{ padding: 24, display: "flex", flexDirection: "column", gap: 24 }}
    >
      <FlightsFrom countries={countries} searchFlights={searchFlights} />
      {flights && flights.length > 0 ? (
        <FlightsList
          flights={flights}
          page={page}
          next={() => setPage(page + 1)}
          prev={() => setPage(page - 1)}
          pages={pages}
          refresh={fetchFlights}
        />
      ) : (
        <Box className="t-card">
          <Typography variant="subtitle1">
            No results try a different search
          </Typography>
        </Box>
      )}
    </Box>
  );
};
