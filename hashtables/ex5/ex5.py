# Your code here
class Entry:
    def __init__(self,path,next=None):
        self.path = path
        self.next = next


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    path_dict = {}
    result = []
    # Populate dict
    for path in files:
        filename = path.split("/")[-1]
        old_head = path_dict[filename] if path_dict.get(filename) else None
        path_dict[filename] = Entry(path,old_head)
    
    # Search through dict
    for filename in queries:
        if not path_dict.get(filename):
            continue
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
