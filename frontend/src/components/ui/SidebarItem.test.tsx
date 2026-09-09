import { render } from '@testing-library/react';
import { SidebarItem } from './SidebarItem';
import { describe, it, expect } from 'vitest';

describe('SidebarItem Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<SidebarItem />);
    expect(container).toBeTruthy();
  });
});
