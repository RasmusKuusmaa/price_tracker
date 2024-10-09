import { useState } from 'react'
import './App.css'

function App() {

  return (
    <>
      <form>
      <label htmlFor="url">Product URL:</label><br />
      <input 
        type="text" 
        id="url" 
        name="url" 
        required 
      /><br /><br />
      <label htmlFor="email">Email:</label><br />
      <input 
        type="email" 
        id="email" 
        name="email" 
        required 
      /><br /><br />

      <button type="submit">Submit</button>
    </form>
    </>
  )
}

export default App
