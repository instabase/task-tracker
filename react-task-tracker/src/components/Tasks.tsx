import { taskType } from '../types/task';
import Task from './Task';

const Tasks = (props: { tasks: taskType[]; onDelete: any; onToggle: any }) => {
  return (
    <div>
      {props.tasks.map((task) => (
        <Task
          key={task.id}
          task={task}
          onDelete={props.onDelete}
          onToggle={props.onToggle}
        />
      ))}
    </div>
  );
};

export default Tasks;
