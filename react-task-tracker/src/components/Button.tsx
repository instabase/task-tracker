const Button = (props: { color: string; text: string; onClick: any }) => {
  return (
    <button
      onClick={props.onClick}
      className="btn"
      style={{ backgroundColor: props.color }}
    >
      {props.text}
    </button>
  );
};

Button.defaultProps = {
  color: 'steelblue',
};

export default Button;
