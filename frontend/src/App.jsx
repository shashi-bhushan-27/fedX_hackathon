import {BrowserRouter,Routes,Route} from "react-router-dom";
import Navbar from "./components/Navbar";
import FedexDashboard from "./pages/FedexDashboard";
import DcaDashboard from "./pages/DcaDashboard";
import Copilot from "./pages/Copilot";

export default ()=>(
<BrowserRouter>
 <Navbar/>
 <Routes>
   <Route path="/fedex" element={<FedexDashboard/>}/>
   <Route path="/dca" element={<DcaDashboard/>}/>
   <Route path="/copilot" element={<Copilot/>}/>
 </Routes>
</BrowserRouter>
);
