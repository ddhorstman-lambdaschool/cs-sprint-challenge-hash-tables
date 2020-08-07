# Your code here
class Entry:
    def __init__(self,path,next=None):
        self.path = path
        self.next = next


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    path_dict = {}
    result = []
    # Populate dict
    for path in files:
        filename = path.split("/")[-1]
        # If one or more paths already exist, prepend the new path
        old_head = path_dict[filename] if path_dict.get(filename) else None
        path_dict[filename] = Entry(path,old_head)
    
    # Search through dict
    for filename in queries:
        # Do nothing if file not found
        if not path_dict.get(filename):
            continue
        # Add all paths for the given filename
        curr_path = path_dict[filename]
        while curr_path is not None:
            result.append(curr_path.path)
            curr_path = curr_path.next
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
