import React, { useState } from 'react';
import axios from 'axios';

const CourseForm = () => {
  const [title, setTitle] = useState('');
  const [code, setCode] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = event => {
    event.preventDefault();
    axios.post('http://backend:8000/api/courses/', { title, code, description })
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Title:
        <input type="text" value={title} onChange={event => setTitle(event.target.value)} />
      </label>
      <br />
      <label>
        Code:
        <input type="text" value={code} onChange={event => setCode(event.target.value)} />
      </label>
      <br />
      <label>
        Description:
        <textarea value={description} onChange={event => setDescription(event.target.value)} />
      </label>
      <br />
      <button type="submit">Create Course</button>
    </form>
  );
};

export default CourseForm;