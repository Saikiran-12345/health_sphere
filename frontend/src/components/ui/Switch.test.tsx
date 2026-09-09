import { render } from '@testing-library/react';
import { Switch } from './Switch';
import { describe, it, expect } from 'vitest';

describe('Switch Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Switch />);
    expect(container).toBeTruthy();
  });
});
