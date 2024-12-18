import { useState } from 'react'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import Login from './components/login'
import Register from './components/register'

  function App() {
    return (
      <Router>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path='register' element={<Register/>}/>
        </Routes>
      </Router>
    )
  }
export default App



/*
function App() {
  const [url, setUrl] = useState('');
  const [email, setEmail] = useState('')
  
  const handleSubmit = (e) => {
    e.preventDefault();
    
    fetch('http://127.0.0.1:5000/track', {
      method: 'POST',
      headers: {
        'Content-Type' : 'application/json'
      },
      body: JSON.stringify({url, email}),
    })
    .then((Response) => Response.json())
    .then((res) => {
      console.log('success', res)
      alert('data submitted');
    })
    .catch((err) => {
      console.error('ERROR', err)
      alert('failed to submit')
    })
  }
  return (
    <>
      <form onSubmit={handleSubmit}>
      <label htmlFor="url">Product URL:</label><br />
      <input 
        type="text" 
        id="url" 
        name="url"
        value={url}
        onChange={(e) => setUrl(e.target.value)} 
        required 
      /><br /><br />
      <label htmlFor="email">Email:</label><br />
      <input 
        type="email" 
        id="email" 
        name="email" 
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required 
      /><br /><br />

      <button type="submit">Submit</button>
    </form>
    </>
  )
}

export default App
*/