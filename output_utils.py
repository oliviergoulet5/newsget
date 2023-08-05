def promptInt(prompt):
    result = input(prompt)
    if not result.isdigit():
        return None
    return int(result)

def promptIntOrPanic(prompt):
    result = promptInt(prompt)
    if result == None:
        exit(1)
    else:
        return result

def paginatedPrompt(options, page_size=5, curr=1):
    prompt = "\n"

    page_first_index = (curr * page_size) - page_size
    page_last_index = page_first_index + page_size 

    for i, option in enumerate(options[page_first_index : page_last_index]):
        text = option['text'] 
        prompt += "\033[1m" + str(i + 1) + ". " + text + "\033[0m" + "\n\n"

    result = input(prompt + f"\nSelect an option 1-{page_size} (n = next page, p = prev page): ")
    
    # Todo: check boundary for paginating
    if result == "n":
        return paginatedPrompt(options, page_size=page_size, curr=curr + 1)

    if result == "p":
        return paginatedPrompt(options, page_size=page_size, curr=curr - 1)
    
    # Convert result into an integer for non-pagination options
    if not result.isdigit():
        exit(1)

    result = int(result)

    if result > page_size or result < 1:
        exit(1)

    # Return the selected option
    return options[(page_size * curr) - (page_size - result) - 1]['value']

