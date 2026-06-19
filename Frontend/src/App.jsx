import { BrowserRouter, Routes, Route } from 'react-router-dom'
import HomePage from './pages/HomePage'
import BurguerListPage from './pages/BurguerListPage'
import BurguerDetailPage from './pages/BurguerDetailPage'
import './App.css'

function App() {
  return (
   
    <BrowserRouter>
     <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/burguers" element={<BurguerListPage />} />
      <Route path="/burguers/:id" element={<BurguerDetailPage />} />
     </Routes>
    </BrowserRouter>

  )
}

export default App