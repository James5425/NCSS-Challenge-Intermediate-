primeans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
            107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
            227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
            349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
            467, 479, 487, 491, 499, 503, 509, 521, 523, 541]


def check_domain(number):
    domains = ''
    # Find the domains this number belongs to
    if number % 5 == 0:
        domains = domains + 'Pentadian '
    # Check if it belongs to other domains after this

    if number < 0:
        domains = domains + 'Minutian '
    else:
        pass

    if len(str(number)) == 2:
        domains = domains + 'Disiphine '
    else:
        pass

    if number in primeans:
        domains = domains + 'Primean '
    else:
        pass

    return f"is a {domains}citizen."


# Write the rest of your program after this
dic = {}
numbers = []
counter = 0
nums = input("Enter numbers: ").split()
for x in nums:
    numbers.append(int(x))

for y in numbers:
    dic[y] = check_domain(y)

for z, m in dic.items():

    if m == "is a citizen.":
        counter += 1
        pass
    else:
        print(z, m)
print(f"Free numbers: {counter}")

