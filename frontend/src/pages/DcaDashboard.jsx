import {useEffect,useState} from "react";
import api from "../api";
import CaseTable from "../components/CaseTable";

export default ()=>{
 const [cases,setCases]=useState([]);
 useEffect(()=>{api.get("/dca_portal/DCA001").then(r=>setCases(r.data));},[]);
 return <CaseTable data={cases}/>;
};
