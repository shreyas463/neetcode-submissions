class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        window, max_window, satisfied = 0,0,0

        for r in range(len(customers)):

            # If the owner is grumpy at r,
            # these customers are currently unsatisfied
            # and can potentially be saved by the secret technique.
            if grumpy[r] == 1:
                window += customers[r]
            else:
                # These customers are already satisfied so just add it
                satisfied += customers[r]

            # If the window becomes too large,
            # remove the leftmost element and starting slding window
            if r - l + 1 > minutes:

                # Only remove from window if it was
                # originally added to window.
                if grumpy[l] == 1:
                    window -= customers[l]

                l += 1

            # Keep track of the maximum number of
            # unhappy customers we can save.
            max_window = max(window, max_window)

        return satisfied + max_window