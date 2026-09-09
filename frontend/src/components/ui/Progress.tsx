export const Progress = ({ val=50 }) => <div className='w-full bg-gray-200 rounded'><div className='bg-blue-600 h-2 rounded' style={{width: `${val}%`}}></div></div>;
