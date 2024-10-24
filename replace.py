# Python script to replace selected text in index.html with content of main.py

# Step 1: Read the content of main.py
with open('main.py', 'r') as main_file:
    main_content = main_file.read()

# Step 2: Read the content of index.html
with open('index.html', 'r') as index_file:
    index_content = index_file.read()

# Step 3: Replace the selected text in index.html with the content of main.py
# Replace text between #### and #### in index.html with the content of main.py
start_marker = "#--#"
end_marker = "#--#"

start_index = index_content.find(start_marker)
end_index = index_content.find(end_marker, start_index + len(start_marker))

if start_index != -1 and end_index != -1:
    updated_content = (index_content[:start_index + len(start_marker)] + 
                       "\n" + main_content + "\n" + 
                       index_content[end_index:])
else:
    print("Markers not found in index.html")
    updated_content = index_content

# Step 4: Write the updated content back to index.html
with open('index.html', 'w') as index_file:
    index_file.write(updated_content)

print("Content of main.py has been successfully copied to index.html")