import {useState} from "react";
import {askCopilot} from "../api";

export default function Copilot(){
  const [q,setQ] = useState("");
  const [a,setA] = useState("");

  const ask = async ()=>{
    const res = await askCopilot(q);
    setA(res.answer);
  };

  return (
    <>
      <h2>FedEx Recovery Copilot</h2>
      <input value={q} onChange={e=>setQ(e.target.value)} />
      <button onClick={ask}>Ask</button>
      <p>{a}</p>
    </>
  );
}
