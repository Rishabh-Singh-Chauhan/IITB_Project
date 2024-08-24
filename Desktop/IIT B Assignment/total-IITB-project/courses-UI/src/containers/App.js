import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import CourseList from './CourseList';
import CourseDetails from './CourseDetails';
import CourseForm from './CourseForm';

const App = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" exact component={CourseList} />
        <Route path="/courses/:id" component={CourseDetails} />
        <Route path="/create-course" component={CourseForm} />
      </Switch>
    </BrowserRouter>
  );
};

export default App;