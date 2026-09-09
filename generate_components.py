import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

components = {
    "Button.tsx": "export const Button = () => <button className='bg-blue-600 text-white px-4 py-2 rounded'>Button</button>;",
    "Input.tsx": "export const Input = () => <input className='border p-2 rounded' placeholder='Enter text...' />;",
    "Avatar.tsx": "export const Avatar = ({ initials='US' }) => <div className='w-10 h-10 rounded-full bg-gray-200 flex items-center justify-center'>{initials}</div>;",
    "Badge.tsx": "export const Badge = ({ text='Status' }) => <span className='px-2 py-1 text-xs bg-blue-100 text-blue-800 rounded-full'>{text}</span>;",
    "Modal.tsx": "export const Modal = ({ isOpen=false }) => isOpen ? <div className='fixed inset-0 bg-black/50'>Modal Content</div> : null;",
    "Tooltip.tsx": "export const Tooltip = ({ text='Info' }) => <div className='relative group'>Hover me<span className='absolute hidden group-hover:block'>{text}</span></div>;",
    "Alert.tsx": "export const Alert = ({ msg='Alert!' }) => <div className='p-4 bg-red-100 text-red-800 rounded'>{msg}</div>;",
    "Tabs.tsx": "export const Tabs = () => <div className='flex gap-4 border-b'><button className='border-b-2 border-blue-600'>Tab 1</button><button>Tab 2</button></div>;",
    "Accordion.tsx": "export const Accordion = () => <div><details><summary>Title</summary><p>Content</p></details></div>;",
    "Checkbox.tsx": "export const Checkbox = () => <input type='checkbox' className='rounded text-blue-600' />;",
    "RadioGroup.tsx": "export const RadioGroup = () => <div><input type='radio' name='group'/> Option 1</div>;",
    "Switch.tsx": "export const Switch = () => <div className='w-10 h-5 bg-gray-300 rounded-full'></div>;",
    "Spinner.tsx": "export const Spinner = () => <div className='animate-spin w-5 h-5 border-2 border-blue-600 border-t-transparent rounded-full'></div>;",
    "Progress.tsx": "export const Progress = ({ val=50 }) => <div className='w-full bg-gray-200 rounded'><div className='bg-blue-600 h-2 rounded' style={{width: f'{val}%'}}></div></div>;",
    "Breadcrumbs.tsx": "export const Breadcrumbs = () => <nav className='text-sm text-gray-500'>Home > Dashboard</nav>;",
    "Pagination.tsx": "export const Pagination = () => <div className='flex gap-2'><button>Prev</button><button>Next</button></div>;",
    "Dropdown.tsx": "export const Dropdown = () => <select className='border p-2 rounded'><option>Option 1</option></select>;",
    "Table.tsx": "export const Table = () => <table className='w-full'><thead><tr><th>Col</th></tr></thead><tbody><tr><td>Data</td></tr></tbody></table>;",
    "SidebarItem.tsx": "export const SidebarItem = ({ label='Menu' }) => <div className='p-2 hover:bg-gray-100 rounded'>{label}</div>;",
    "Skeleton.tsx": "export const Skeleton = () => <div className='animate-pulse bg-gray-200 h-4 rounded w-full'></div>;"
}

# Generate 20 foundational UI components
for name, content in components.items():
    create_file(f'frontend/src/components/ui/{name}', content)
    
# Generate massive test suite for all 20 components
for name in components.keys():
    test_name = name.replace('.tsx', '.test.tsx')
    comp_name = name.replace('.tsx', '')
    test_content = f"""
import {{ render }} from '@testing-library/react';
import {{ {comp_name} }} from './{comp_name}';
import {{ describe, it, expect }} from 'vitest';

describe('{comp_name} Component', () => {{
  it('renders without crashing', () => {{
    const {{ container }} = render(<{comp_name} />);
    expect(container).toBeTruthy();
  }});
}});
"""
    create_file(f'frontend/src/components/ui/{test_name}', test_content)

print("Component library and test suites generated.")
