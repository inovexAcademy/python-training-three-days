from typing import Iterator

# Step 1: Implement your own iterable class that represents an insurance portfolio.
class InsurancePortfolioIterable:
    def __init__(self) -> None:
        self.policies = []

    def add_policy(self, policy_id: int, policy_holder: str, premium: float) -> None:
        self.policies.append({
            'policy_id': policy_id,
            'policy_holder': policy_holder,
            'premium': premium
        })

    def __iter__(self) -> Iterator:
        pass

# Test your InsurancePortfolio class
portfolio = InsurancePortfolioIterable()
# TODO: add policies here

for policy in portfolio:
    # TODO: print the policies
    pass


### Step 2: Implementing an Iterator (Claims Log)
class ClaimsLogIterator:
    def __init__(self, claims: list[dict[str, int]]) -> None:
        self.claims: list[dict[str, int]] = claims
        self.index: int = 0

    def __iter__(self)-> Iterator:
        pass

    def __next__(self) -> dict[str, int]:
        pass

# TODO: Test your ClaimsLogIterator class by giving some claims
claims = []

claims_log = ClaimsLogIterator(claims)
for claim in claims_log:
    # TODO: print the policies
    pass


### Step 3: Try different itertools