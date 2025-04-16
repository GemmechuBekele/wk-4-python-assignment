with open("assignment.txt", "w") as file:
   file.write("Create a program that reads a file and writes a modified version to a new file.\n")
   file.write("Ask the user for a filename and handle errors if it doesn't exist or can't be read.\n")
   
#Ask the user for a filename
filename = input("Enter the filename: ")
try:
   with open(filename, "r") as file:
      content = file.read()
      
      #Modify the content
      # Count the number of words in the file
      wordCount = len(content.split())
      # Convert to uppercase
      upperWords = content.upper()
   
      #Prepare for modified version
      modifiedContent = f"{upperWords}\n\n word count: {wordCount}"
   
      with open("modified_version.txt", "w") as modifiedFile:
         modifiedFile.write(modifiedContent)
      print("File modified successfully!")
   
except FileNotFoundError:
   print("File not found. Please check the filename and try again.")