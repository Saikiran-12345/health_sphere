import { render } from '@testing-library/react';
import { Input } from './Input';
import { describe, it, expect } from 'vitest';

describe('Input Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Input />);
    expect(container).toBeTruthy();
  });
});
