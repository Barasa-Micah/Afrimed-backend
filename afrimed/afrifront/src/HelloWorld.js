import React, {useState, useEffect} from 'react'
import axios from 'axios'

function HelloMedic(){
    const [message, setMessage] = useState('');

    useEffect(() => {
        axios.get('http://localhost:8000/medicapi/hello-medic/')
        .then(response => {
            setMessage(response.data.message);
        })
        .catch(error => {
            console.log(error);
        });

    }, []);

    return (
        <div>
            <h1>Afrimed</h1>
            <p>{message}</p>
        </div>
    );
}

export default HelloMedic