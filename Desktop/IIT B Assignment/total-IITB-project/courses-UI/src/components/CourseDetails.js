import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CourseDetails = ({ match }) => {
  const [course, setCourse] = useState({});

  useEffect(() => {
    axios.get(`http://backend:8000/api/courses/${match.params.id}/`)
      .then(response => {
        setCourse(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, [match.params.id]);

  return (
    <div>
      <h1>{course.title}</h1>
      <p>{course.description}</p>
    </div>
  );
};

export default CourseDetails;