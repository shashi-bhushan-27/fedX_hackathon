import {Link} from "react-router-dom";

export default ()=>(
<div style={{padding:10,background:"#4d148c",color:"white"}}>
  <Link to="/fedex" style={{color:"white",marginRight:20}}>FedEx</Link>
  <Link to="/dca" style={{color:"white",marginRight:20}}>DCA Portal</Link>
  <Link to="/copilot" style={{color:"white"}}>Copilot</Link>
</div>
);
