const API = "http://localhost:8000/api";

export const getCases = (dca_id) =>
  fetch(`${API}/dca_portal/${dca_id}`).then(res => res.json());

export const updateCase = (data) =>
  fetch(`${API}/dca_update`, {method:"POST", body:JSON.stringify(data)});

export const askCopilot = (q) =>
  fetch(`${API}/copilot?question=${encodeURIComponent(q)}`)
    .then(res=>res.json());
