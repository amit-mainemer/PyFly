import React, { useState, useEffect } from "react";
import { useAuth } from "../AuthContext";
import { useSnackbar } from "../SnackbarContext";
import {
  Box,
  IconButton,
  Card,
  CardContent,
  Typography,
  Tooltip,
} from "@mui/material";
import { UserAvatar } from "../components/UserAvatar/UserAvatar";
import { api } from "../api";
import DeleteIcon from "@mui/icons-material/Delete";
import FlightIcon from "@mui/icons-material/Flight";

export const Profile = () => {
  const { user } = useAuth();
  const { pop } = useSnackbar();
  const [tickets, setTickets] = useState([]);

  const fetchTickets = async () => {
    try {
      const response = await api.get("/user/tickets/" + user.id);
      setTickets(response.data);
    } catch (ex) {
      console.warn(ex);
    }
  };

  const deleteTicket = async (id) => {
    try {
      await api.delete("ticket/" + id);
      pop({ message: "Ticket Deleted", severity: "success" });
      fetchTickets();
    } catch (ex) {
      console.warn(ex);
    }
  };

  useEffect(() => {
    fetchTickets();
  }, [user]);

  return (
    <Box padding={"24px"} display="flex" flexDirection={"column"} gap={2}>
      <Box display={"flex"} justifyContent={"space-between"}>
        <Box
          className="t-card"
          display="flex"
          flexDirection="column"
          justifyContent="center"
          alignItems="center"
        >
          <UserAvatar text={user.full_name.charAt(0)} />
          <Typography variant="subtitle1">Hello {user.full_name}</Typography>
        </Box>
        <Box className="t-card">
          <Typography>Total tickets: {tickets.length}</Typography>
        </Box>
      </Box>
      <Box className="t-card">
        <Typography>Here are your tickets:</Typography>
        <Box
          style={{
            marginTop: "12px",
            display: "flex",
            gap: "10px",
            flexWrap: "wrap",
          }}
        >
          {tickets.map(({ id, flight }) => (
            <Card key={id} style={{ maxWidth: "260px" }}>
              <CardContent
                style={{ display: "flex", justifyContent: "space-between" }}
              >
                <Box>
                  <Box display={"flex"} alignItems={"center"}>
                    <Box
                      display={"flex"}
                      alignItems={"center"}
                      paddingRight={"4px"}
                    >
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
                    <Box
                      display={"flex"}
                      alignItems={"center"}
                      paddingLeft={"4px"}
                    >
                      <Typography variant="body2">
                        {flight.dest_country.code}
                      </Typography>
                    </Box>
                  </Box>
                  <Typography variant="body2">{flight.timestamp}</Typography>
                </Box>
                <Box>
                  <Tooltip title="Delete Ticket" style={{ marginLeft: "auto" }}>
                    <IconButton color="error" onClick={() => deleteTicket(id)}>
                      <DeleteIcon />
                    </IconButton>
                  </Tooltip>
                </Box>
              </CardContent>
            </Card>
          ))}
        </Box>
      </Box>
    </Box>
  );
};
