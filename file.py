import re
class Recipe_Book:
  def __init__(self,filename="recipe.txt"):
    self.filename=filename
    self.book=[]
  def add_recipe(self):
    title=input("Enter the title: ")
    ingredients=input("Enter the ingredients: ")
    recipe=input("Enter the recipe: ")
    self.book.append({"title":title,"ingredients":ingredients,"recipe":recipe})
    try:
      with open(self.filename,"a") as f:
        f.write("=====================\n")
        f.write(f"Title:{title}\n")
        f.write(f"Ingredients:{ingredients}\n")
        f.write(f"Recipe:{recipe}\n")
        f.write("=====================\n")
      print("Recipe added successfully!\n")
    except Exception as e:
      print(f"Error saving recipe: {e}")
  def view_recipe_by_title(self):
      try:
        with open(self.filename,"r") as f:
          lines=f.readlines()
      except FileNotFoundError:
        print("Recipe file not found")
        return
      title=input("Enter the title: ").strip()
      pattern = rf"^Title:{re.escape(title)}\b.*"
      found=False
      for i,line in enumerate(lines):
        if re.match(pattern,line,re.IGNORECASE):
          for j in range(i-1,i+4):
            if 0<=j<len(lines):
              print(lines[j].strip())
          found=True
          break 
      if not found:
        print("No recipe found of this title")
  def delete_recipe_by_title(self):
    title=input("Enter the title: ")
    pattern = rf"^Title:{re.escape(title)}\b.*"
    new_lines=[]
    found=False
    skip=False
    try:
      with open(self.filename,"r") as f:
        lines=f.readlines()
    except FileNotFoundError:
      print("Recipe file not found")
      return
    i=0
    while i<len(lines):
        line=lines[i]
        if  re.match(pattern,line,re.IGNORECASE):
          found=True
          while i>0 and not lines[i-1].startswith("="):
            i-=1
          while i<len(lines) and not lines[i].startswith("="):
            i+=1 
          if i<len(lines):
            i+=1 
        else:
          new_lines.append(line)
          i+=1
    if found:
      with open(self.filename,"w")as f:
        f.write("".join(new_lines))
      print("Recipe deleted successfully.")   
    else:
      print("No recipe found of this title")    
  def edit_recipe(self):
    asky=input("Enter the the title which recipe you want to edit: ")
    pattern = rf"^Title:{re.escape(asky)}\b.*"
    new_lines=[]
    found=False
    try:
      with open(self.filename,"r") as f:
        lines=f.readlines()
    except FileNotFoundError:
      print("Recipe file not found")
      return
    i=0
    while i<len(lines):
      line=lines[i]
      if re.match(pattern,line,re.IGNORECASE):
          found=True
          while i>0 and not lines[i-1].startswith("="):
            i-=1
          while i<len(lines) and not lines[i].startswith("="):
            i+=1 
          if i<len(lines):
            i+=1 
          new_title=input("Enter the new title: ")
          new_ingredients=input("Enter the new ingredients: ")
          new_recipe=input("Enter the new recipe: ")
          new_lines.append("=====================\n")
          new_lines.append(f"Title:{new_title}\n")
          new_lines.append(f"Ingredients:{new_ingredients}\n")
          new_lines.append(f"Recipe:{new_recipe}\n")
          new_lines.append("=====================\n")
      else:
          new_lines.append(line)
          i+=1
        
    if found: 
      with open(self.filename,"w") as f:
        f.write("".join(new_lines))
        print("Recipe updated successfully.")
    else:
      print("No title found of this name")
  def list_all_titles(self):
    try:
      with open(self.filename,"r") as f:
        lines=f.readlines()
        titles=[line.strip().replace("Title:","")for line in lines if line.startswith("Title:")]
      if titles:
        print("\n---Saved Recipe Titles---")
        for idx,title in enumerate(titles,1):
          print(f"{idx}.{title}")
        print("-----------------------------\n")
      else:
        print("No recipes found.")
    except FileNotFoundError:
      print("No recipe file found.")
obj=Recipe_Book()
print("---------Welcome to the recipe book---------")
while True:
  menu=input("Enter what you want to do\n1.Add new recipe\n2.View recipe by title\n3.Delete recipe by title\n4.Edit recipe\n5.List all titles\n(1/2/3/4/5) or quit 'q': ")
  if menu=="1":
    obj.add_recipe()
  elif menu=="2":
    obj.view_recipe_by_title()
  elif menu=="3":
    obj.delete_recipe_by_title()
  elif menu=="4":
    obj.edit_recipe()
  elif menu=="5":
    obj.list_all_titles()
  elif menu.lower()=="q":
    print("Thankyou for using Recipe Book.Goodbye!")
    break




    