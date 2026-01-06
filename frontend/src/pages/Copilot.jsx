import {useState} from "react";
import api from "../api";

export default ()=>{
 const [q,setQ]=useState("");
 const [a,setA]=useState("");
 const ask=async()=>{
   const r=await api.post(`/copilot?question=${q}`);
   setA(r.data.answer);
 };
 return (
  <>
    <h2>Recovery Copilot</h2>
    <input value={q} onChange={e=>setQ(e.target.value)}/>
    <button onClick={ask}>Ask</button>
    <p>{a}</p>
  </>
 );
};
