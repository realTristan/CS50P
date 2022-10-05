def main():
    plate = input("Plate: ")

    if is_valid(plate):
        return True
    else:
        return False


def is_valid(s):
    length = len(s)

    # max 6, min 2 chars
    if length >= 2 and length <= 6:
        for letters in s:
            # break if not alpha or num (punct, space, etc case)
            if not s.isalnum():
                return False
                
            if s[0].isdigit() or s[1].isdigit():
                return False

            #  first 2 char are letters
            if s[0:2].isalpha():
                # middle part of entry
                middle = s[1:-1]
                if middle.isnumeric() and middle.find(0):
                    break

                # endswith nums, but num group cannot start with 0
                zeroIndex = s.find("0") - 1
                if s[-(zeroIndex)].isdigit():
                    for x in s:
                        if x.isdigit():
                            if x.startswith('0'):
                                return False
                            else:
                                return True

                # true if ends with digit
                elif s[-2].isdigit() and s[-1].isalpha():
                    return False
                elif s[-2].isdigit():
                    return True
                elif s[0:2].isalpha():
                    return True
            else:
                False

    else:
        return False

if __name__ == "__main__":
    main()