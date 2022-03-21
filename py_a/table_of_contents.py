def tableOfContents(text):
    # Write your code here
    
    current_chapter = 0
    current_section = 0
    
    table_of_contents = []
    
    for line in text:
        if line.startswith('# '):
            current_chapter += 1
            # reset section
            current_section = 0
            table_of_contents.append('{}. {}'.format(current_chapter, line[2:]))
        elif line.startswith('## '):
            current_section += 1
            table_of_contents.append('{}.{}. {}'.format(current_chapter, current_section, line[3:]))
        # else it's just content and we don't need to worry
        
    return table_of_contents
    

if __name__ == '__main__':
    text_count = int(input().strip())

    text = []

    for _ in range(text_count):
        text_item = input()
        text.append(text_item)

    result = tableOfContents(text)

    print(result)