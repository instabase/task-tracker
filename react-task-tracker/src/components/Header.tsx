import Button from './Button';
import { useLocation } from 'react-router-dom';

const Header = (props: {
  title: string;
  toggleAddTask: any;
  showAdd: boolean;
}) => {
  const location = useLocation();
  return (
    <header className="header">
      <h1> Task Tracker {props.title}</h1>
      {location.pathname === '/' && (
        <Button
          color={props.showAdd ? 'darkred' : 'green'}
          text={props.showAdd ? 'Close' : 'Add'}
          onClick={props.toggleAddTask}
        />
      )}
    </header>
  );
};

Header.defaultProps = {
  title: '',
};

// CSS in tsx
// const headingStyle = {
//     color: 'red',
//     backgroundColor: 'black'
// }

export default Header;
