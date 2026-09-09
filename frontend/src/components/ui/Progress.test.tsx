import { render } from '@testing-library/react';
import { Progress } from './Progress';
import { describe, it, expect } from 'vitest';

describe('Progress Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Progress />);
    expect(container).toBeTruthy();
  });
});
