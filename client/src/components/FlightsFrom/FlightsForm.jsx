import React, { useState, useMemo } from "react";
import {
  Box,
  Autocomplete,
  TextField,
  Typography,
  Button,
} from "@mui/material";
import css from "./FlightsForm.module.css";
import CalendarMonthIcon from "@mui/icons-material/CalendarMonth";
import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";

export const FlightsFrom = ({ countries, searchFlights }) => {
  const [originCountry, setOriginCountry] = useState(null);
  const [destCountry, setDestCountry] = useState(null);
  const [date, setDate] = useState(null);

  const countriesOptions = useMemo(
    () =>
      countries
        ? countries?.map(({ name, id }) => ({ label: name, value: id }))
        : [],
    [countries]
  );
  return (
    <Box className="t-card" display="flex" gap={2}>
      <Autocomplete
        disablePortal
        options={countriesOptions}
        size="small"
        sx={{ width: 300 }}
        value={originCountry}
        onChange={(_, newValue) => {
          setOriginCountry(newValue);
        }}
        renderInput={(params) => <TextField {...params} label="From" />}
      />
      <Autocomplete
        disablePortal
        options={countriesOptions}
        sx={{ width: 300 }}
        value={destCountry}
        size="small"
        onChange={(_, newValue) => {
          setDestCountry(newValue);
        }}
        renderInput={(params) => <TextField {...params} label="To" />}
      />
      <Box display={"flex"} alignItems={"center"} gap={1}>
        <Typography variant="body1">Date</Typography>
        <DatePicker
          showIcon
          className={css.datePicker}
          selected={date}
          onChange={(date) => setDate(date)}
          icon={<CalendarMonthIcon />}
        />
      </Box>
      <Button
        variant="contained"
        style={{ marginLeft: "auto" }}
        onClick={() =>
          searchFlights({
            from: originCountry?.value ?? "",
            to: destCountry?.value ?? "",
            date: date ?? "",
          })
        }
      >
        Search
      </Button>
    </Box>
  );
};
