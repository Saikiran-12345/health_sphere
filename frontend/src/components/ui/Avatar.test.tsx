import { render } from '@testing-library/react';
import { Avatar } from './Avatar';
import { describe, it, expect } from 'vitest';

describe('Avatar Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Avatar />);
    expect(container).toBeTruthy();
  });
});
