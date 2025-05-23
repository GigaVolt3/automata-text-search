class AutomataSearch:
    def __init__(self, pattern):
        self.pattern = pattern
        self.len_pat = len(pattern)
        self.alphabet = set(pattern)
        self.transition_table = self._build_transition_table()

    def _build_transition_table(self):
        """Build the transition table for the pattern."""
        table = [{} for _ in range(self.len_pat + 1)]
        
        for state in range(self.len_pat + 1):
            for char in self.alphabet:
                next_state = min(self.len_pat, state + 1)
                while next_state > 0 and (self.pattern[:next_state] != (self.pattern[state - next_state + 1:state] + char)[-next_state:]):
                    next_state -= 1
                table[state][char] = next_state
        
        return table

    def search(self, text):
        """Search for the pattern in the given text using the automaton."""
        state = 0
        results = []
        
        for i, char in enumerate(text):
            if char in self.transition_table[state]:
                state = self.transition_table[state][char]
            else:
                state = 0
                
            if state == self.len_pat:
                results.append(i - self.len_pat + 1)
                state = self.transition_table[state].get(char, 0)
                
        return results
