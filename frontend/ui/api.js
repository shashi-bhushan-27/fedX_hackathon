// Prefer env override; otherwise default to backend on same host (port 8000)
// In GitHub Codespaces, use the forwarded HTTPS URL format
const BASE =
  import.meta.env.VITE_API_BASE ||
  (() => {
    const hostname = window.location.hostname;
    if (hostname.includes('app.github.dev')) {
      // GitHub Codespaces: replace port in hostname (e.g., -5173 -> -8000)
      const backendHost = hostname.replace(/-\d+\./, '-8000.');
      return `https://${backendHost}/api`;
    }
    // Local development
    return `http://localhost:8000/api`;
  })()

export const ingestCase = data =>
  fetch(`${BASE}/ingest`, {method:"POST",headers:{'Content-Type':'application/json'},body:JSON.stringify(data)}).then(r=>r.json())

export const predict = data =>
  fetch(`${BASE}/predict`, {method:"POST",headers:{'Content-Type':'application/json'},body:JSON.stringify(data)}).then(r=>r.json())

export const allocate = data =>
  fetch(`${BASE}/allocate`, {method:"POST",headers:{'Content-Type':'application/json'},body:JSON.stringify(data)}).then(r=>r.json())

export const metrics = () =>
  fetch(`${BASE}/metrics`).then(r=>r.json())

export const copilot = q =>
  fetch(`${BASE}/copilot?question=${encodeURIComponent(q)}`,{method:"POST"}).then(r=>r.json())

export const dcaCases = id =>
  fetch(`${BASE}/dca_portal/${id}`).then(r=>r.json())
