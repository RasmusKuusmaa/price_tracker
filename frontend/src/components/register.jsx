import React, {useState} from 'react'

function Register(){
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [password2, setPassword2] = useState('');
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:5000/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({email, password, password2})
        });
        const res = await response.json();
        if (response.ok) {
            alert('account registered')
        } else {
            alert(res.error || 'not registered')
        }
    } catch (error) {
            console.error('reg err', error)
            alert('No Bueno')

        }
    }
    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    Email:
                </label>
                <input value={email} onChange={(e) => setEmail(e.target.value)} />
                <br/>
                <label>
                    Password: 
                </label>
                <input
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                />
                <label>
                    Repeat Password:
                </label>
                <input 
                value={password2}
                onChange={(e) => setPassword2(e.target.value)}/>
                <button type='submit'> Register</button>
            </form>
        </div>
    )
}   
export default Register