import React, { useState } from 'react'

function Login(){
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({email, password})
        });
        const res = await response.json();
        if (response.ok) {
            alert('login successful')
        } else {
            alert(res.error || 'login not successful')
        }
        } catch (error) {
            console.error('login frnt err', error)
            alert('NO BUENO')
        } 

    }
    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    Email:
                </label>
                <input
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <br/>
                <br/>
                <label>Password: </label>
                <input value={password}
                type='password'
                onChange={(e) => setPassword(e.target.value)}/>
                <button type='submit'>Login</button>
            </form>
            <button onClick={() => window.location.href = '/register'}>
                create an account</button>
            
        </div>
    )
}
export default Login