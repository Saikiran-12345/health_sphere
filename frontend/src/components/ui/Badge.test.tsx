import { render } from '@testing-library/react';
import { Badge } from './Badge';
import { describe, it, expect } from 'vitest';

describe('Badge Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Badge />);
    expect(container).toBeTruthy();
  });
});
