def vowelStrings(word, queries):
    vowels = set('aeiou')
    prefix_sum = [0] * (len(word)+1)

    for i in range(1, len(word)+1):
        # check if the letter is vowel
        is_vowel = word[i-1] in vowels
        # set the number of vowels for this substring
        prefix_sum[i] = prefix_sum[i-1] + (1 if is_vowel else 0)
    
    result = []
    for left, right in queries:
        num_vowels  = prefix_sum[right+1] - prefix_sum[left]
        result.append(num_vowels)
    
    return result