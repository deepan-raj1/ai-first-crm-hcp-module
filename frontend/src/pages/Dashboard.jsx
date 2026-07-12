import { Typography, Box } from "@mui/material";
import InteractionList from "../components/InteractionList";

const Dashboard = () => {
  return (
    <Box sx={{ padding: 4 }}>
      <Typography variant="h4" fontWeight="bold">
        AI-First CRM HCP Module
      </Typography>

     <InteractionList />
    </Box>
  );
};

export default Dashboard;