import { render, screen } from '@testing-library/react';
import { Card } from './Card';
import { describe, it, expect } from 'vitest';

describe('Card Component', () => {
  it('renders children correctly', () => {
    render(<Card>Test Content</Card>);
    expect(screen.getByText('Test Content')).toBeInTheDocument();
  });

  it('applies custom class names', () => {
    const { container } = render(<Card className="bg-red-500">Test</Card>);
    expect(container.firstChild).toHaveClass('bg-red-500');
  });
});
