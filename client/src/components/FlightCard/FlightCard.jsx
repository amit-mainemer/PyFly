import React, { useCallback } from "react";
import {
  Box,
  Card,
  CardActions,
  CardContent,
  Typography,
  Button,
} from "@mui/material";
import FlightTakeoffIcon from "@mui/icons-material/FlightTakeoff";
import FlightLandIcon from "@mui/icons-material/FlightLand";
import AirplaneTicketIcon from "@mui/icons-material/AirplaneTicket";
import FlightIcon from "@mui/icons-material/Flight";
import EventIcon from "@mui/icons-material/Event";
import FlightClassIcon from "@mui/icons-material/FlightClass";
import { useAuth } from "../../AuthContext";
import { api } from "../../api";
import { useSnackbar } from "../../SnackbarContext";

export const FlightCard = ({ flight, refresh }) => {
  const { user } = useAuth();
  const { pop } = useSnackbar();
  const buyTicket = useCallback(async () => {
    try {
     await api.post("/tickets", {
        user_id: user.id,
        flight_id: flight.id,
      });
      pop({message: "Ticket was bought successfully", severity: "success"});
      refresh();
    } catch (ex) {
      console.warn(ex);
    }
  }, [user, flight, refresh]);

  return (
    <Card opacity={1}>
      <CardContent>
        <Box display={"flex"} alignItems={"center"}>
          <Box display={"flex"} alignItems={"center"} paddingRight={"4px"}>
            <Typography variant="body2">
              {flight.origin_country.code}
            </Typography>
          </Box>
          -------
          <FlightIcon
            style={{
              transform: "rotate(90deg)",
              transformOrigin: "center center",
              padding: "0 4px",
              marginBottom: "-2px",
            }}
            color="action"
          />
          ------
          <Box display={"flex"} alignItems={"center"} paddingLeft={"4px"}>
            <Typography variant="body2">{flight.dest_country.code}</Typography>
          </Box>
        </Box>
        <Box>
          <Box display="flex" alignItems={"center"} gap={1}>
            <FlightTakeoffIcon color="action" fontSize={"small"} />
            <Typography variant="subtitle2">
              Origin Country: <b>{flight.origin_country.name}</b>
            </Typography>
          </Box>
          <Box display="flex" alignItems={"center"} gap={1}>
            <FlightLandIcon color="action" fontSize={"small"} />
            <Typography variant="subtitle2">
              Destination Country: <b>{flight.dest_country.name}</b>
            </Typography>
          </Box>
          <Box display="flex" alignItems={"center"} gap={1}>
            <EventIcon color="action" fontSize={"small"} />
            <Typography variant="subtitle2">
              Date: <b>{flight.timestamp}</b>
            </Typography>
          </Box>
          <Box display="flex" alignItems={"center"} gap={1}>
            <FlightClassIcon color="action" fontSize={"small"} />
            <Typography variant="subtitle2">
              Remaining Seats: <b>{flight.remaining_seats}</b>
            </Typography>
          </Box>
        </Box>
      </CardContent>
      <CardActions>
        <Button
          variant="contained"
          startIcon={<AirplaneTicketIcon />}
          disabled={flight.remaining_seats === 0}
          style={{ marginLeft: "auto" }}
          onClick={buyTicket}
        >
          Buy Ticket
        </Button>
      </CardActions>
    </Card>
  );
};
