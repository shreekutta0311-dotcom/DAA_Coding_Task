# Hack a OTP authentication system using brute force methodology,
#  where OTP is of 4 digits long. 

import time
from itertools import product


CORRECT_OTP = "4321"     
MAX_ATTEMPTS = 5          
LOCKOUT_SECONDS = 60      
OTP_TTL_SECONDS = 120      

class MockOTPVerifier:
    def __init__(self, correct_otp, max_attempts=5, lockout_seconds=60, ttl=120):
        self.correct_otp = correct_otp
        self.max_attempts = max_attempts
        self.lockout_seconds = lockout_seconds
        self.ttl = ttl
        self.failed_attempts = 0
        self.locked_until = 0
        self.issued_at = time.time()

    def is_expired(self):
        return (time.time() - self.issued_at) > self.ttl

    def verify(self, otp_attempt: str) -> bool:
        now = time.time()
        if now < self.locked_until:
            # locked
            raise RuntimeError(f"Account locked until {time.ctime(self.locked_until)}")

        if self.is_expired():
            raise RuntimeError("OTP expired")

        if otp_attempt == self.correct_otp:
            # success -> reset counters
            self.failed_attempts = 0
            return True
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= self.max_attempts:
                self.locked_until = now + self.lockout_seconds
            return False

def brute_force_simulation(verifier: MockOTPVerifier, max_attempts_to_try=None, delay_between_attempts=0.0):
    """
    Try all 4-digit codes from '0000'..'9999' against the verifier.
    - max_attempts_to_try: stop early for demo (None -> try all until lockout/expiry)
    - delay_between_attempts: seconds between attempts to simulate throttling/latency
    """
    attempts = 0
    start = time.time()

    for digits in product("0123456789", repeat=4):
        code = "".join(digits)
        attempts += 1
        try:
            ok = verifier.verify(code)
        except RuntimeError as e:
            print(f"[{attempts}] {code} -> ERROR: {e}")
            return None, attempts

        if ok:
            elapsed = time.time() - start
            print(f"[{attempts}] {code} -> SUCCESS (found). Elapsed: {elapsed:.2f}s")
            return code, attempts

        if attempts % 1000 == 0:
            print(f"Attempted {attempts} codes so far...")

        if delay_between_attempts:
            time.sleep(delay_between_attempts)

        if max_attempts_to_try and attempts >= max_attempts_to_try:
            print("Demo limit reached; stopping.")
            return None, attempts

    print("Exhausted all codes (no success).")
    return None, attempts

if __name__ == "__main__":
    print("=== Fast attacker (no delay) ===")
    v = MockOTPVerifier(CORRECT_OTP, MAX_ATTEMPTS, LOCKOUT_SECONDS, OTP_TTL_SECONDS)
    brute_force_simulation(v)

    print("\nWaiting for lockout to expire...")
    time.sleep(LOCKOUT_SECONDS + 1)

    print("\n=== Slow attacker (1 attempt / 10s) ===")
    v2 = MockOTPVerifier(CORRECT_OTP, MAX_ATTEMPTS, LOCKOUT_SECONDS, OTP_TTL_SECONDS)
    # Demonstration: stop early to avoid very long runs
    brute_force_simulation(v2, max_attempts_to_try=20, delay_between_attempts=10)
