import { render } from '@testing-library/react';
import { Alert } from './Alert';
import { describe, it, expect } from 'vitest';

describe('Alert Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Alert />);
    expect(container).toBeTruthy();
  });
});
