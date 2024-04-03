from collections import Counter

def extract_ranks_suits(cards):
    ranks = [card["rank"] for card in cards]
    suits = [card["suit"] for card in cards]
    return ranks, suits

def is_pair(ranks):
    counts = Counter(ranks)
    return any(count == 2 for count in counts.values())

def is_two_pair(ranks):
    counts = Counter(ranks)
    pairs = [count for count in counts.values() if count == 2]
    return len(pairs) == 2

def is_three_of_a_kind(ranks):
    counts = Counter(ranks)
    return any(count == 3 for count in counts.values())

def is_four_of_a_kind(ranks):
    counts = Counter(ranks)
    return any(count == 4 for count in counts.values())

def rank_to_numeric(rank):
    if rank.isdigit():
        return int(rank)
    elif rank == 'J':
        return 11
    elif rank == 'Q':
        return 12
    elif rank == 'K':
        return 13
    elif rank == 'A':
        return 14

def is_straight(ranks):
    numeric_ranks = [rank_to_numeric(rank) for rank in ranks]
    sorted_ranks = sorted(numeric_ranks, reverse=True)
    return sorted_ranks == list(range(sorted_ranks[0], sorted_ranks[0]-5, -1))

def is_flush(suits):
    return len(set(suits)) == 1

def is_full_house(ranks):
    counts = Counter(ranks)
    return sorted(counts.values()) == [2, 3]

def rank_hand(cards):
    ranks, suits = extract_ranks_suits(cards)
    
    if is_straight(ranks) and is_flush(suits):
        return 8, max(ranks)
    elif is_four_of_a_kind(ranks):
        return 7, max(set(ranks), key=ranks.count)
    elif is_full_house(ranks):
        return 6, max(set(ranks), key=ranks.count)
    elif is_flush(suits):
        return 5, max(ranks)
    elif is_straight(ranks):
        return 4, max(ranks)
    elif is_three_of_a_kind(ranks):
        return 3, max(set(ranks), key=ranks.count)
    elif is_two_pair(ranks):
        return 2, max(set(ranks), key=ranks.count)
    elif is_pair(ranks):
        return 1, max(set(ranks), key=ranks.count)
    else:
        return 0, max(ranks)

# Example usage:
cards = [
    {"rank": "7", "suit": "hearts"},
    {"rank": "6", "suit": "diamonds"},
    {"rank": "2", "suit": "diamonds"},
    {"rank": "7", "suit": "spades"},
    {"rank": "4", "suit": "clubs"},
    {"rank": "Q", "suit": "clubs"},
    {"rank": "K", "suit": "hearts"},
]

rank_id, first_value = rank_hand(cards)
print("Rank ID:", rank_id)
print("First Value:", first_value)
