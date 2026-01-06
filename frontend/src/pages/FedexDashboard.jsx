import {useEffect,useState} from "react";
import KpiCard from "../components/KpiCard";

export default function FedexDashboard(){
  const [m,setM]=useState({});
  useEffect(()=>{fetch("http://localhost:8000/api/metrics").then(r=>r.json()).then(setM)},[]);
  return (
    <>
      <h2>FedEx Command Center</h2>
      <div style={{display:"flex",gap:20}}>
        <KpiCard label="Total Cases" value={m.total_cases}/>
        <KpiCard label="Recovered" value={m.recovered}/>
        <KpiCard label="Open Cases" value={m.open_cases}/>
      </div>
    </>
  );
}
