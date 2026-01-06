import { useEffect, useState } from "react";
import { getCases } from "../api";
import CaseTable from "../components/CaseTable";

export default function DcaDashboard(){
  const [cases,setCases] = useState([]);
  useEffect(()=>{ getCases("DCA001").then(setCases); },[]);
  return <CaseTable data={cases} />;
}
