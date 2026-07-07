# Represents a very simplified "semantic core"
# Concepts are nodes, relationships are edges.
# This aims to illustrate a step towards meaning-based understanding
# rather than just statistical word association, as discussed in the article.

semantic_network = {
    "Cat": {
        "IS_A": ["Animal"],
        "HAS_PROPERTY": ["Playful", "Independent", "Mammal"]
    },
    "Dog": {
        "IS_A": ["Animal"],
        "HAS_PROPERTY": ["Loyal", "Playful", "Mammal"]
    },
    "Animal": {
        "IS_A": ["Living_Being"],
        "HAS_PROPERTY": ["Breathes", "Moves"]
    },
    "Plant": {
        "IS_A": ["Living_Being"],
        "HAS_PROPERTY": ["Photosynthesizes", "Grows"]
    },
    "Living_Being": {
        "IS_A": [], # Top-level concept in this small graph
        "HAS_PROPERTY": ["Exists"]
    }
}

def query_concept_properties(concept_name):
    """
    Retrieves direct and inherited properties of a concept.
    This simulates deriving 'meaning' through relationships, not just word recognition.
    """
    properties = set()
    if concept_name in semantic_network:
        # Add direct properties
        if "HAS_PROPERTY" in semantic_network[concept_name]:
            properties.update(semantic_network[concept_name]["HAS_PROPERTY"])

        # Recursively add properties from parent concepts (IS_A relationships)
        if "IS_A" in semantic_network[concept_name]:
            for parent in semantic_network[concept_name]["IS_A"]:
                properties.update(query_concept_properties(parent))
    return sorted(list(properties))

def check_relationship(subject, relationship_type, target):
    """
    Checks if a direct or inherited relationship exists.
    Illustrates how the 'core' can answer questions about meaning.
    """
    if subject not in semantic_network:
        return False

    # Check direct relationship
    if relationship_type in semantic_network[subject] and target in semantic_network[subject][relationship_type]:
        return True

    # Check inherited relationship (for IS_A)
    if relationship_type == "IS_A" and "IS_A" in semantic_network[subject]:
        for parent in semantic_network[subject]["IS_A"]:
            if check_relationship(parent, relationship_type, target):
                return True
    return False

# --- Demonstration --- 
print("--- Semantic Core Demonstration ---")

# Example 1: Querying properties of a concept
concept = "Cat"
print(f"\nProperties of '{concept}':")
# This goes beyond just knowing the word "cat" and tries to list its inherent characteristics.
for prop in query_concept_properties(concept):
    print(f"- {prop}")

concept = "Animal"
print(f"\nProperties of '{concept}':")
for prop in query_concept_properties(concept):
    print(f"- {prop}")

# Example 2: Checking relationships
print(f"\nIs 'Cat' an 'Animal'? {check_relationship('Cat', 'IS_A', 'Animal')}")
print(f"Is 'Dog' a 'Plant'? {check_relationship('Dog', 'IS_A', 'Plant')}")
print(f"Is 'Cat' a 'Living_Being'? {check_relationship('Cat', 'IS_A', 'Living_Being')}") # Inherited relationship
print(f"Does 'Cat' have property 'Loyal'? {check_relationship('Cat', 'HAS_PROPERTY', 'Loyal')}")
print(f"Does 'Dog' have property 'Loyal'? {check_relationship('Dog', 'HAS_PROPERTY', 'Loyal')}")

# Example 3: Illustrating the "language-independent" aspect (conceptual)
# The concepts themselves (Cat, Animal, Playful) are abstract identifiers.
# They could be mapped to different languages without changing the core network.
print("\n--- Conceptual Language-Independence ---")
print("The 'semantic_network' uses abstract identifiers (e.g., 'Cat', 'Animal').")
print("These could be mapped to 'Kedi' (Turkish), 'Gato' (Spanish), 'Katze' (German)")
print("without altering the underlying relationships or derived meaning within this core.")
print("This is a step towards understanding meaning beyond specific linguistic forms.")
