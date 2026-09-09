export const Tooltip = ({ text='Info' }) => <div className='relative group'>Hover me<span className='absolute hidden group-hover:block'>{text}</span></div>;
