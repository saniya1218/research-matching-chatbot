"""
Research Matching System - Interactive Chatbot
A terminal-based chatbot that helps users find relevant faculty researchers
and explore research collaboration opportunities.
"""

from src.retrieve import search_faculty, display_search_results
from src.web_search import get_trending_topics, find_collaborations
from src.agent import load_faculty_profile, print_available_faculty
import string 

def display_welcome_message():
    """Display a welcome message and instructions for the user."""
    print("\n" + "=" * 60)
    print("🔬 Welcome to the Research Matching System")
    print("=" * 60)
    print("\nYou can ask questions like:")
    print("  • 'Who works on machine learning?'")
    print("  • 'Tell me about Dr. Anil Kumar'")
    print("  • 'Show trending research topics'")
    print("  • 'Find collaboration opportunities in AI'")
    print("  • Type 'exit' to quit the chatbot")
    print("-" * 60)


def handle_faculty_search(query):

    search_query = query.lower()

    search_query = search_query.replace("who works on", "")

    search_query = search_query.translate(

        str.maketrans("", "", string.punctuation)

    ).strip()

    print(f"\n🔍 Searching for '{search_query}'...")

    results = search_faculty(search_query)

    display_search_results(results)

    answer = input(

        "\nDo you want to select the first faculty recommendation? (yes/no): "

    )

    if answer.lower() == "yes":

        print("\n✅ Recommendation confirmed.")

    else:

        print("\n👍 No faculty selected.")


def handle_faculty_profile(query):

    faculty_name = query.lower()

    faculty_name = faculty_name.replace("tell me about", "")

    faculty_name = faculty_name.strip()

    load_faculty_profile(faculty_name)

def handle_trending_topics(query):
    """
    Handle queries about trending research topics.
    
    Args:
        query (str): User's query about trending topics
    """
    get_trending_topics()


def handle_collaboration(query):

    research_area = query.lower()

words_to_remove = [
    "find",
    "collaboration",
    "collaborations",
    "opportunity",
    "opportunities",
    "in",
    "for"
]

for word in words_to_remove:
    research_area = research_area.replace(word, "")

research_area = research_area.strip()

if not research_area:
    research_area = "Artificial Intelligence"

    find_collaborations(research_area)

    answer = input(

        "\nWould you like to save this collaboration recommendation? (yes/no): "

    )

    if answer.lower() == "yes":

        print("✅ Collaboration recommendation saved.")

    else:

        print("👍 Recommendation discarded.")

def process_user_query(query):
    """
    Process user input and route to appropriate handler function.
    
    Args:
        query (str): The user's input query
    
    Returns:
        bool: True to continue chatbot, False to exit
    """
    # Normalize query to lowercase for comparison
    query_lower = query.lower().strip()
    
    # Check exit condition
    if query_lower == "exit":
        print("\n👋 Thank you for using the Research Matching System. Goodbye!")
        return False
    
    # Handle help/info requests
    if query_lower in ["help", "?"]:
        print_available_faculty()
        return True
    
    # Route to appropriate handler based on query keywords
    if "who works on" in query_lower:
        handle_faculty_search(query_lower)
    
    elif "tell me about" in query_lower:
        handle_faculty_profile(query_lower)
    
    elif "trend" in query_lower:
        handle_trending_topics(query_lower)
    
    elif "collaboration" in query_lower:
        handle_collaboration(query_lower)
    
    else:
        # Default: treat as general research search
        print(f"\n🔍 Searching for: '{query}'...")
        results = search_faculty(query, num_results=3)
        display_search_results(results)
    
    return True


def main():
    """Main chatbot loop - continuously prompts for user input."""
    display_welcome_message()
    
    while True:
        try:
            # Get user input
            user_input = input("\n💬 You: ").strip()
            
            # Skip empty inputs
            if not user_input:
                continue
            
            # Process query and check if we should continue
            if not process_user_query(user_input):
                break
        
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n⚠️  Chatbot interrupted by user. Goodbye!")
            break
        except Exception as e:
            # Handle any unexpected errors
            print(f"\n❌ An error occurred: {e}")
            print("Please try again with a different query.")


if __name__ == "__main__":
    main()
