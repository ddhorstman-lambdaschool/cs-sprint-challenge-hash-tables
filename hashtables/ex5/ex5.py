# Your code here
class Entry:
    def __init__(self,path,next_=None):
        self.path = path
        self.next = next_


def finder(files, queries):
    """
    YOUR CODE HERE
    """

    # Create a dict of filename->path pairs
    path_dict = {}
    for path in files:
        # Extract filename
        filename = path.split("/")[-1]
        # If one or more paths already exist, prepend the new path
        old_head = path_dict[filename] if path_dict.get(filename) else None
        path_dict[filename] = Entry(path,old_head)
    
    # Check the dict for each requested filename
    result = []
    for filename in queries:
        # Do nothing if file not found
        if not path_dict.get(filename):
            continue
        # Add all paths for the given filename to results
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
