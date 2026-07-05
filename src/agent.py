"""
Agent module for handling faculty profile display and information retrieval.
"""

import os


def normalize_name(name):
    """Normalize faculty name for file lookup."""
    name = name.lower()
    name = name.replace("dr.", "")
    name = name.replace("dr", "")
    name = name.strip()
    name = "_".join(name.split())

    return name


def load_faculty_profile(faculty_name):

    faculty_name = normalize_name(faculty_name)

    faculty_dir = "./data/faculty"

    for file in os.listdir(faculty_dir):

        if file.lower().replace(".txt", "") == faculty_name:

            with open(os.path.join(faculty_dir, file), "r", encoding="utf-8") as f:

                print("\n👤 Faculty Profile")
                print("=" * 60)
                print(f.read())
                print("=" * 60)

                return True

    print("\n❌ Faculty not found.\n")

    print_available_faculty()

    return False


def print_available_faculty():

    faculty_dir = "./data/faculty"

    print("\n📚 Available Faculty")

    print("-" * 40)

    for file in sorted(os.listdir(faculty_dir)):

        if file.endswith(".txt"):

            print(file.replace(".txt", "").replace("_", " ").title())


def get_faculty_suggestions():

    faculty_dir = "./data/faculty"

    return [

        file.replace(".txt", "").replace("_", " ").title()

        for file in os.listdir(faculty_dir)

        if file.endswith(".txt")

    ]