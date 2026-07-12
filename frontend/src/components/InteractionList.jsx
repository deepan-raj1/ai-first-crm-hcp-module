import { useEffect, useState } from "react";
import { Paper, Typography, List, ListItem, ListItemText } from "@mui/material";

import { getInteractions } from "../services/interactionApi";

const InteractionList = () => {
  const [interactions, setInteractions] = useState([]);

  useEffect(() => {
    loadInteractions();
  }, []);

  const loadInteractions = async () => {
    try {
      const data = await getInteractions();
      setInteractions(data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Paper sx={{ p: 3 }}>
      <Typography variant="h6" gutterBottom>
        Interaction History
      </Typography>

      <List>
        {interactions.map((item) => (
          <ListItem key={item.id}>
            <ListItemText
              primary={item.hcp_name}
              secondary={`${item.interaction_type} • ${item.date}`}
            />
          </ListItem>
        ))}
      </List>
    </Paper>
  );
};

export default InteractionList;