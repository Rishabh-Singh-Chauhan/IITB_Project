import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CourseList = () => {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    axios.get('http://backend:8000/api/courses/')
      .then(response => {
        setCourses(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h1>Courses</h1>
      <ul>
        {courses.map(course => (
          <li key={course.id}>
            <a href={`/courses/${course.id}`}>{course.title}</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CourseList;