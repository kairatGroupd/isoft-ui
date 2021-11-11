import "./App.css";
import NavBar from "./components/NavBar";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./components/Pages/Home";
import { About } from "./components/Pages/About";
import { Blog } from "./components/Pages/Blog";
import { Contact } from "./components/Pages/Contact";

function App() {
  return (
    <BrowserRouter>    
        <NavBar/>
        
        <div className="pages">
            <Routes>
              <Route exact="true" path="/" component={Home} />
              <Route exact="true" path="/about" component={About} />
              <Route exact="true" path="/blog" component={Blog} />
              <Route exact="true" path="/contact" component={Contact} />
            </Routes>
        
        </div>
        
    </BrowserRouter>
  );
}

export default App;

