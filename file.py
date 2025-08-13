import re

class Recipe_Book:
    def __init__(self, filename="recipe.txt"):
        self.filename = filename

    def add_recipe(self):
        title = input("Enter the title: ").strip()
        ingredients = input("Enter the ingredients: ").strip()
        recipe = input("Enter the recipe: ").strip()
        try:
            with open(self.filename, "a", encoding="utf-8") as f:
                f.write(f"Title:{title}\n")
                f.write(f"Ingredients:{ingredients}\n")
                f.write(f"Recipe:{recipe}\n")
                f.write("=====================\n")  # ✅ Only end separator
            print("✅ Recipe added successfully!\n")
        except Exception as e:
            print(f"❌ Error saving recipe: {e}")

    def view_recipe_by_title(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("⚠️ Recipe file not found")
            return

        title = input("Enter the title: ").strip()
        pattern = rf"^Title:{re.escape(title)}$"
        found = False
        block = []

        for line in lines:
            if line.strip() == "=====================":
                if any(re.match(pattern, l.strip(), re.IGNORECASE) for l in block):
                    print("\n".join(block))
                    print("=====================")
                    found = True
                block = []
            else:
                block.append(line.strip())

        if not found:
            print("❌ No recipe found with this title")

    def delete_recipe_by_title(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("⚠️ Recipe file not found")
            return

        title = input("Enter the title to delete: ").strip()
        pattern = rf"^Title:{re.escape(title)}$"
        new_lines = []
        block = []
        found = False

        for line in lines:
            if line.strip() == "=====================":
                if any(re.match(pattern, l.strip(), re.IGNORECASE) for l in block):
                    print("\nMatched Recipe:")
                    print("\n".join(block))
                    confirm = input("Do you want to delete this recipe? (yes/no): ").strip().lower()
                    if confirm == "yes":
                        found = True
                        # skip writing this block
                    else:
                        new_lines.extend(line + "\n" if not line.endswith("\n") else line for line in block)
                        new_lines.append("=====================\n")
                else:
                    new_lines.extend(line + "\n" if not line.endswith("\n") else line for line in block)
                    new_lines.append("=====================\n")
                block = []
            else:
                block.append(line.strip())

        if found:
            with open(self.filename, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            print("✅ Recipe deleted successfully.")
        else:
            print("❌ No recipe found with this title.")

    def edit_recipe(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("⚠️ Recipe file not found")
            return

        title = input("Enter the title to edit: ").strip()
        pattern = rf"^Title:{re.escape(title)}$"
        new_lines = []
        block = []
        found = False

        for line in lines:
            if line.strip() == "=====================":
                if any(re.match(pattern, l.strip(), re.IGNORECASE) for l in block):
                    print("\nCurrent Recipe:")
                    print("\n".join(block))
                    confirm = input("Do you want to update this recipe? (yes/no): ").strip().lower()
                    if confirm == "yes":
                        found = True
                        new_title = input("Enter new title: ").strip()
                        new_ingredients = input("Enter new ingredients: ").strip()
                        new_recipe = input("Enter new recipe: ").strip()
                        new_lines.append(f"Title:{new_title}\n")
                        new_lines.append(f"Ingredients:{new_ingredients}\n")
                        new_lines.append(f"Recipe:{new_recipe}\n")
                        new_lines.append("=====================\n")
                    else:
                        new_lines.extend(line + "\n" if not line.endswith("\n") else line for line in block)
                        new_lines.append("=====================\n")
                else:
                    new_lines.extend(line + "\n" if not line.endswith("\n") else line for line in block)
                    new_lines.append("=====================\n")
                block = []
            else:
                block.append(line.strip())

        if found:
            with open(self.filename, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            print("✅ Recipe updated successfully.")
        else:
            print("❌ No matching title found.")

    def list_all_titles(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
            titles = [line.strip().replace("Title:", "") for line in lines if line.startswith("Title:")]
            if titles:
                print("\n📋 Saved Recipe Titles:")
                for idx, title in enumerate(titles, 1):
                    print(f"{idx}. {title}")
            else:
                print("❌ No recipes found.")
        except FileNotFoundError:
            print("⚠️ No recipe file found.")


if __name__ == "__main__":
    obj = Recipe_Book()
    print("--------- Welcome to the Recipe Book ---------")
    while True:
        menu = input("\nWhat do you want to do?\n1. Add new recipe\n2. View recipe by title\n3. Delete recipe by title\n4. Edit recipe\n5. List all titles\n(1/2/3/4/5) or quit 'q': ").strip()
        if menu == "1":
            obj.add_recipe()
        elif menu == "2":
            obj.view_recipe_by_title()
        elif menu == "3":
            obj.delete_recipe_by_title()
        elif menu == "4":
            obj.edit_recipe()
        elif menu == "5":
            obj.list_all_titles()
        elif menu.lower() == "q":
            print("👋 Thank you for using Recipe Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")
