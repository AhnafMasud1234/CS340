
# Stable Matching Problem: Implement the Gale-Shapley Algorithm

"""
Background:
You are given two groups: a set of men and a set of women. Each person has ranked all members of the opposite group in order of preference. 
Your task is to implement the Gale-Shapley algorithm to produce a stable matching between the two groups.

Instructions:
1. Create preference lists for a set of 4 men and 4 women.
2. Implement the Gale-Shapley algorithm where men propose to women.
3. Output the final stable matching.
4. Ensure the result is stable by checking that no unmatched man and woman pair prefer each other over their current matches.

Bonus:
- Add an option to switch proposers (i.e., let women propose instead).
- Compare the resulting matchings.

This exercise is expected to take about 1 hour.
"""

# Sample data
men_preferences = {
    'A': ['X', 'Y', 'Z', 'W'],
    'B': ['W', 'Y', 'X', 'Z'],
    'C': ['Y', 'X', 'W', 'Z'],
    'D': ['Z', 'W', 'X', 'Y']
}

women_preferences = {
    'X': ['B', 'A', 'D', 'C'],
    'Y': ['A', 'B', 'C', 'D'],
    'Z': ['C', 'D', 'A', 'B'],
    'W': ['D', 'C', 'B', 'A']
}

# Implement Gale-Shapley Algorithm

    
def gale_shapley(men_prefs, women_prefs):
    # Start with all men free
    free_men = list(men_prefs.keys())

    # Engagements stored as: woman -> man
    engaged = {}

    # Track proposals made by each man
    proposals = {man: [] for man in men_prefs}

    while free_men:
        man = free_men.pop(0)  # Take one free man

        # Go through his preferences in order
        for woman in men_prefs[man]:
            if woman not in proposals[man]:
                proposals[man].append(woman)  # Mark that he has proposed

                if woman not in engaged:
                    # If the woman is free, engage
                    engaged[woman] = man
                    break
                else:
                    current_partner = engaged[woman]
                    # Check if she prefers the new man over her current one
                    if women_prefs[woman].index(man) < women_prefs[woman].index(current_partner):
                        # She switches to the new man
                        engaged[woman] = man
                        free_men.append(current_partner)  # The old partner becomes free
                        break
                    # Otherwise, she stays with her current partner

    # Convert to man -> woman format for output
    return {man: woman for woman, man in engaged.items()}


# Function to verify if the matching is stable
def is_stable(matching, men_prefs, women_prefs):
    # Reverse matching to woman -> man
    reverse_matching = {v: k for k, v in matching.items()}

    for man in men_prefs:
        current_woman = matching[man]
        man_rank = men_prefs[man].index(current_woman)

        # Check all women he prefers more than his current match
        for preferred in men_prefs[man][:man_rank]:
            her_current_partner = reverse_matching[preferred]
            if women_prefs[preferred].index(man) < women_prefs[preferred].index(her_current_partner):
                # They both prefer each other over current matches — unstable
                return False
    return True


# Run the algorithm
stable_matching = gale_shapley(men_preferences, women_preferences)

# Output the stable matches
print("Stable Matching Result:")
for man, woman in stable_matching.items():
    print(f"{man} is matched with {woman}")

# Check stability
if is_stable(stable_matching, men_preferences, women_preferences):
    print("\nThe matching is stable.")
else:
    print("\nThe matching is NOT stable.")