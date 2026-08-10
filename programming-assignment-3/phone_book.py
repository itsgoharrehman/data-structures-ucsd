# python3
import sys

def process_queries(queries):
    result = []
    # Direct addressing array for phone numbers up to 7 digits (0 to 9,999,999)
    contacts = [None] * 10000000
    
    for query in queries:
        type_ = query[0]
        number = int(query[1])
        
        if type_ == 'add':
            contacts[number] = query[2]
        elif type_ == 'del':
            contacts[number] = None
        else:  # 'find'
            name = contacts[number]
            result.append(name if name is not None else 'not found')
            
    return result

def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    n = int(input_data[0])
    queries = [line.split() for line in input_data[1:n + 1]]
    print('\n'.join(process_queries(queries)))

if __name__ == '__main__':
    main()