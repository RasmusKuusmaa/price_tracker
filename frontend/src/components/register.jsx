import React, {useState} from 'react'

function Register(){
    return (
        <div>
            <form>
                <label>
                    Email:
                </label>
                <input />
                <br/>
                <label>
                    Password: 
                </label>
                <input/>
                <label>
                    Repeat Password:
                </label>
                <input/>
                <button> Register</button>
            </form>
        </div>
    )
}   
export default Register