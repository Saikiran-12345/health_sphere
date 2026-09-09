import { render } from '@testing-library/react';
import { Pagination } from './Pagination';
import { describe, it, expect } from 'vitest';

describe('Pagination Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Pagination />);
    expect(container).toBeTruthy();
  });
});
