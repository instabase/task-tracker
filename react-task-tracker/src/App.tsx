import React from 'react';
import { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Header from './components/Header';
import Tasks from './components/Tasks';
import AddTask from './components/AddTask';
import Footer from './components/Footer';
import About from './components/About';
import { taskType } from './types/task';
import renderRequest from "./Backend.js"

function App() {
  const [showAddTask, setShowAddTask] = useState(false);
  const [tasks, setTasks] = useState<taskType[]>([]);

  useEffect(() => {
    const getTasks = async () => {
      const tasksFromServer = await fetchTasks();
      setTasks(tasksFromServer);
    };
    getTasks();
  }, []);

  // Fetch tasks
  const fetchTasks = async () => {
    const res = await renderRequest('task/');
    const response = await res.json();
    return response['data'];
  };

  // Fetch task
  const fetchTask = async (id: number) => {
    const res = await renderRequest(`task/${id}`);
    const response = await res.json();
    const data = response['data'];
    return data;
  };

  // Delete task
  const deleteTask = async (id: number) => {
    await renderRequest(`task/${id}`, { method: 'DELETE' });
    setTasks(tasks.filter((task) => task.id !== id));
  };

  // Add task
  const addTask = async (task: taskType) => {
    const res = await renderRequest('task', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(task),
    });
    const response = await res.json();
    const data = response['data'];
    setTasks([...tasks, data]);

    // const taskId = Math.floor(Math.random() * 10000) + 1;
    // const newTask = { taskId, ...task };
    // setTasks([...tasks, newTask]);
  };

  // Toggle Reminder
  const toggleReminder = async (id: number) => {
    const taskToToggle = await fetchTask(id);
    const updatedTask = { ...taskToToggle, reminder: !taskToToggle.reminder };
    const res = await renderRequest(`task/${id}`, {
      method: 'PUT',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(updatedTask),
    });

    const response = await res.json();
    const data = response['data'];

    setTasks(
      tasks.map((task) =>
        task.id === id ? { ...task, reminder: data.reminder } : task
      )
    );
  };

  return (
    <Router>
      <div className="container">
        <Header
          toggleAddTask={() => setShowAddTask(!showAddTask)}
          showAdd={showAddTask}
        />
        <Route
          path="/"
          exact
          render={(props: any) => (
            <>
              {showAddTask && <AddTask onAdd={addTask} />}
              {tasks.length > 0 ? (
                <Tasks
                  tasks={tasks}
                  onDelete={deleteTask}
                  onToggle={toggleReminder}
                />
              ) : (
                <p>You are all done!</p>
              )}
            </>
          )}
        />
        <Route path="/about" component={About} />
        <Footer />
      </div>
    </Router>
  );
}

export default App;
