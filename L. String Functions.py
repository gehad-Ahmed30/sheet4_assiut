def process_query(x, y, z, process):
    z = list(z)  # Convert string to list for mutable operations
    result = []
    
    for i in process:
        part = i.split()
        command = part[0]

        if command == 'pop_back':
            if z:  # Ensure list is not empty
                z.pop()
        elif command == "front":
            if z:  # Ensure list is not empty
                result.append(z[0])
        elif command == 'back':
            if z:  # Ensure list is not empty
                result.append(z[-1])
        elif command == 'sort':
            l = int(part[1]) - 1  # Convert to 0-based index
            r = int(part[2])      # Python slicing is end-exclusive
            z[l:r] = sorted(z[l:r])
        elif command == 'reverse':
            l = int(part[1]) - 1
            r = int(part[2])
            z[l:r] = z[l:r][::-1]
        elif command == 'print':
            index = int(part[1]) - 1  # Convert to 0-based index
            if 0 <= index < len(z):  # Ensure index is within bounds
                result.append(z[index])
        elif command == 'substr':
            l = int(part[1]) - 1
            r = int(part[2])
            if 0 <= l <= r <= len(z):  # Ensure indices are within bounds
                result.append(''.join(z[l:r]))  # Convert list to string
        elif command == 'push_back':
            z.append(part[1])
    
    return result

x, y = map(int, input().split())
z = input()
process = [input().strip() for _ in range(y)]


result = process_query(x, y, z, process)
for j in result:
    print(j)
