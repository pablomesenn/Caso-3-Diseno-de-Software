import random
from typing import List, Tuple

class TripartiteService:
    def __init__(self):
        self.shares_storage = {}  # In-memory storage for shares
        self.prime = 2**127 - 1  # Large prime for finite field arithmetic

    def _evaluate_polynomial(self, coefficients: List[int], x: int) -> int:
        """Evaluate polynomial at x in finite field."""
        result = 0
        for coef in reversed(coefficients):
            result = (result * x + coef) % self.prime
        return result

    def _generate_polynomial(self, secret: int, threshold: int) -> List[int]:
        """Generate random polynomial with secret as constant term."""
        coefficients = [secret] + [random.randint(0, self.prime - 1) for _ in range(threshold - 1)]
        return coefficients

    def _string_to_int(self, s: str) -> int:
        """Convert string to integer for secret sharing."""
        return int.from_bytes(s.encode('utf-8'), 'big') % self.prime

    def _int_to_string(self, n: int) -> str:
        """Convert integer back to string."""
        byte_length = (n.bit_length() + 7) // 8
        return n.to_bytes(byte_length, 'big').decode('utf-8', errors='ignore')

    def generate_key_shares(self, secret: str, dataset_id: str, shares: int = 3, threshold: int = 2) -> List[str]:
        """Generate shares for the secret using Shamir's Secret Sharing."""
        try:
            if isinstance(secret, str):
                secret_int = self._string_to_int(secret)
            else:
                raise ValueError("El secreto debe ser una cadena")
            
            if shares < threshold or threshold < 1:
                raise ValueError("Parámetros inválidos: shares >= threshold >= 1")
            
            # Generate polynomial and shares
            coefficients = self._generate_polynomial(secret_int, threshold)
            shares_list = [(i, self._evaluate_polynomial(coefficients, i)) for i in range(1, shares + 1)]
            
            # Store shares as hex strings
            shares_hex = [f"{x}:{y:064x}" for x, y in shares_list]
            self.shares_storage[dataset_id] = shares_hex
            return shares_hex
        except Exception as e:
            raise ValueError(f"Error generando partes: {str(e)}")

    def reconstruct_secret(self, shares: List[str], dataset_id: str) -> str:
        """Reconstruct the secret from shares using Lagrange interpolation."""
        try:
            if len(shares) < 2:  # Minimum threshold
                raise ValueError("Se requieren al menos 2 partes")
            
            # Parse shares from hex strings
            points = []
            for share in shares:
                x, y = share.split(':')
                points.append((int(x), int(y, 16)))
            
            # Lagrange interpolation in finite field
            secret_int = 0
            for i, (xi, yi) in enumerate(points):
                numerator = denominator = 1
                for j, (xj, _) in enumerate(points):
                    if i != j:
                        numerator = (numerator * (0 - xj)) % self.prime
                        denominator = (denominator * (xi - xj)) % self.prime
                # Compute modular inverse for denominator
                inv_denominator = pow(denominator, -1, self.prime)
                term = (yi * numerator * inv_denominator) % self.prime
                secret_int = (secret_int + term) % self.prime
            
            return self._int_to_string(secret_int)
        except Exception as e:
            raise ValueError(f"Error reconstruyendo secreto: {str(e)}")