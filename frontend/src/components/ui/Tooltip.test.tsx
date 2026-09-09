import { render } from '@testing-library/react';
import { Tooltip } from './Tooltip';
import { describe, it, expect } from 'vitest';

describe('Tooltip Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Tooltip />);
    expect(container).toBeTruthy();
  });
});
