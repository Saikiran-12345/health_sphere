import { render } from '@testing-library/react';
import { Checkbox } from './Checkbox';
import { describe, it, expect } from 'vitest';

describe('Checkbox Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Checkbox />);
    expect(container).toBeTruthy();
  });
});
