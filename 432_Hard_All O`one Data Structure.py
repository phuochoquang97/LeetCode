from collections import defaultdict


class AllOne:
    def __init__(self):
        self.string_freq = defaultdict(int)  # map each string with its freq
        self.freq_count = defaultdict(int)  # count how many strings have this freq
        self.freq_string = defaultdict(set)  # store strings with a specific freq

        self.max_freq = 0
        self.min_freq = 0

    def inc(self, key: str) -> None:
        freq_of_current_key = self.string_freq[key]

        if freq_of_current_key > 0:
            # remove key from set of its current freq
            self.freq_string[freq_of_current_key].discard(key)

            # decrease the count of current freq
            self.freq_count[freq_of_current_key] -= 1

            # if there is no string with this freq
            if self.freq_count[freq_of_current_key] == 0:
                del self.freq_count[freq_of_current_key]

                # update min_freq
                if self.min_freq == freq_of_current_key:
                    self.min_freq += 1

        # increase freq of current key
        freq_of_current_key += 1

        # update freq of current key
        self.string_freq[key] = freq_of_current_key

        # add key this set of strings with updated freq
        self.freq_string[freq_of_current_key].add(key)

        # update freq_count
        self.freq_count[freq_of_current_key] += 1

        # update max_freq
        self.max_freq = max(self.max_freq, freq_of_current_key)

        # update min_freq
        if self.min_freq == 0 or self.min_freq > freq_of_current_key:
            self.min_freq = freq_of_current_key

    def dec(self, key: str) -> None:
        # this can be ignored because of constraint: decreased key is always existing
        if key not in self.string_freq:
            return

        freq_of_current_key = self.string_freq[key]

        # Remove key from the set of its current frequency
        self.freq_string[freq_of_current_key].discard(key)

        # update the count of current freq
        self.freq_count[freq_of_current_key] -= 1

        # If frequency count of current frequency becomes 0, clean it up
        if self.freq_count[freq_of_current_key] == 0:
            del self.freq_count[freq_of_current_key]
            if self.max_freq == freq_of_current_key:
                self.max_freq -= 1
            if self.min_freq == freq_of_current_key:
                self.min_freq = min(self.freq_count.keys(), default=0)

        # Decrease key's frequency
        freq_of_current_key -= 1
        if freq_of_current_key == 0:
            # Remove the key completely if its frequency goes to 0
            del self.string_freq[key]
        else:
            self.string_freq[key] = freq_of_current_key
            self.freq_string[freq_of_current_key].add(key)
            self.freq_count[freq_of_current_key] += 1

            # Update min_freq
            self.min_freq = min(self.min_freq, freq_of_current_key)

    def getMaxKey(self) -> str:
        if self.max_freq > 0:
            return next(iter(self.freq_string[self.max_freq]))
        return ""

    def getMinKey(self) -> str:
        if self.min_freq > 0:
            return next(iter(self.freq_string[self.min_freq]))
        return ""
