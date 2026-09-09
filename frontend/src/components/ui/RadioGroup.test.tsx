import { render } from '@testing-library/react';
import { RadioGroup } from './RadioGroup';
import { describe, it, expect } from 'vitest';

describe('RadioGroup Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<RadioGroup />);
    expect(container).toBeTruthy();
  });
});
