import {useEffect,useState} from "react";
import api from "../api";
import KpiCard from "../components/KpiCard";

export default ()=>{
 const [m,setM]=useState({});
 useEffect(()=>{api.get("/metrics").then(r=>setM(r.data));},[]);
 return (
  <>
    <h2>FedEx Command Center</h2>
    <div style={{display:"flex",gap:20}}>
      <KpiCard label="Total Cases" value={m.total_cases}/>
      <KpiCard label="Recovered" value={m.recovered}/>
      <KpiCard label="Open" value={m.open_cases}/>
    </div>
  </>
 );
};
