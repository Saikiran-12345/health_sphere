import { render } from '@testing-library/react';
import { Accordion } from './Accordion';
import { describe, it, expect } from 'vitest';

describe('Accordion Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Accordion />);
    expect(container).toBeTruthy();
  });
});
