class Solution():
    def is_valid_password(self, password: str) -> bool:
        if len(password) < 8:
            return False
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()-+" for c in password)
        
        return has_upper and has_lower and has_digit and has_special


example = Solution()
print(example.is_valid_password("Password123!"))  # True
print(example.is_valid_password("pass"))          # False