"""
Scikit-learn compatible python package for latent-space models.

- **NMF**: Non-negative Matrix Factorization
- **SOM**: Self-Organizing Maps
- **GTM**: Generative Topographic Mapping
- **GSM**: Generative Simplex Mapping
"""

from sklatent.test_funcs import add


def main() -> None:
    """Test out the package functionality by printing a simple statement."""
    print("Hello from scikit-latent!")


__all__ = ["add", "main"]
