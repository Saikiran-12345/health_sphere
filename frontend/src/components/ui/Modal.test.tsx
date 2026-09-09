import { render } from '@testing-library/react';
import { Modal } from './Modal';
import { describe, it, expect } from 'vitest';

describe('Modal Component', () => {
  it('renders without crashing', () => {
    const { container } = render(<Modal />);
    expect(container).toBeTruthy();
  });
});
