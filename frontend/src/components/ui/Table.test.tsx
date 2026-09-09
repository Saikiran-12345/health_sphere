import { render } from '@testing-library/react';
import { Table } from './Table';
import { describe, it, expect } from 'vitest';

describe('Table Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Table />);
    expect(container).toBeTruthy();
  });
});
