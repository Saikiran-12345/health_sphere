import { render } from '@testing-library/react';
import { Spinner } from './Spinner';
import { describe, it, expect } from 'vitest';

describe('Spinner Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Spinner />);
    expect(container).toBeTruthy();
  });
});
