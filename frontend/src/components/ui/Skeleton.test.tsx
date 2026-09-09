import { render } from '@testing-library/react';
import { Skeleton } from './Skeleton';
import { describe, it, expect } from 'vitest';

describe('Skeleton Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Skeleton />);
    expect(container).toBeTruthy();
  });
});
