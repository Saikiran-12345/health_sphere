import { render } from '@testing-library/react';
import { Button } from './Button';
import { describe, it, expect } from 'vitest';

describe('Button Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Button />);
    expect(container).toBeTruthy();
  });
});
