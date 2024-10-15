import React, { useState } from 'react'

function Login(){
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    return (
        <div>
            <form>
                <label>
                    Email:
                </label>
                <input
                    value={email}
                />
                <br/>
                <br/>
                <label>Password: </label>
                <input value={password}/>
                <button>Login</button>
            </form>
            
        </div>
    )
}
export default Login