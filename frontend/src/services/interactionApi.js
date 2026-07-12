import api from "./api";

export const getInteractions = async () => {
  const response = await api.get("/interactions/");
  return response.data;
};

export const createInteraction = async (data) => {
  const response = await api.post("/interactions/", data);
  return response.data;
};

export const updateInteraction = async (id, data) => {
  const response = await api.put(`/interactions/${id}`, data);
  return response.data;
};

export const deleteInteraction = async (id) => {
  const response = await api.delete(`/interactions/${id}`);
  return response.data;
};

