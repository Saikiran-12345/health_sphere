import { render } from '@testing-library/react';
import { Tabs } from './Tabs';
import { describe, it, expect } from 'vitest';

describe('Tabs Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Tabs />);
    expect(container).toBeTruthy();
  });
});
