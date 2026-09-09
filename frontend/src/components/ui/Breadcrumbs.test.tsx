import { render } from '@testing-library/react';
import { Breadcrumbs } from './Breadcrumbs';
import { describe, it, expect } from 'vitest';

describe('Breadcrumbs Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Breadcrumbs />);
    expect(container).toBeTruthy();
  });
});
