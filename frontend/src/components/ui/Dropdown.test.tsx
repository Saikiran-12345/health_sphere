import { render } from '@testing-library/react';
import { Dropdown } from './Dropdown';
import { describe, it, expect } from 'vitest';

describe('Dropdown Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Dropdown />);
    expect(container).toBeTruthy();
  });
});
