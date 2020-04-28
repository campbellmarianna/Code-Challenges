# https://discuss.codechef.com/t/most-frequent-substring-problem/19922

Given a string, we want to know the maximum no. of occurrences of any substring that satisfies following two conditions:

The substring’s lengths is within in inclusive range of minLength to maxLength.
The total no. of unique characters in the string doesn’t exceed maxUnique.
For example, given a string s = abcde, minLength = 2, maxLength = 5, maxUnique = 3, the substrings matching the criteria are(ab, bc, cd, de, abc, bcd, cde). Any shorter string fails he minLength >= 2 any longer will fail maxUnique <= 3. Each of the substring occurs only one time.

INPUT:
First line contains a string, second line contains minLength, third line contains maxLength, and the last line contains maxUnique.

Constraints:

2 <= n <= 105
2 <= minLength <= maxLength <= 26
maxLength < n
2 <= maxUnique <= 26
SAMPLE INPUT:

ababab
2
3
4
SAMPLE OUTPUT:

3
**EXPLANATIONS: **

We want to find the no. of occurrences of the most frequently occurring substring of s = “ababab” that has the length in the inclusive range from minLength = 2 and maxLength = 3 and contains maximum of maxUnique = 4 unique characters. The substring ab occurs three times aba, bab and ba occurs twice. Because we want maximum of this frequencies we return 3 as our answer.

## Coment
(Part 1)

Obviously we shouldn’t care for maxLength, since we wanna maximize ocuurrence(as lets say if a substring of length x, occurs y times, then there must be a substring of length(x-1) that occurs >= y times)

So we just have to find max no.of occurrences of a substring of length minLength

(Part 2)

unique thing can easily be done using frequency arrays

(Part 3)

One simple way is to use rolling hashing see this: https: // threads-iiith.quora.com/String-Hashing-for-competitive-programming 651

for counting max occurence of a substring of given length

#  ---
(Part 1)

Proof: Lets say a substring s of length x occurs b times, then there will be a substring s’ of length < x occuring >= b times(1 such substring would be a substring of s)

like ababa

ab occurs 2 times, so obviously a occurs >= 2, b >= 2

So better to find minimum Length String, as it will have less unique characters and also occurs greater number of times

# --

(Part 2)

how to check if a substring s[i:j] is valid(no.of unique characters <= maxUnique)

lets construct a prefix sum freq array

where:

freq[i][‘a’] = freq[i-1][‘a’]+(s[i] ==‘a’)

freq[i][‘b’] = freq[i-1][‘b’]+(s[i] ==‘b’)

…

So for calculating no.of unique characters in s[i:j]

uniqueCount = 0
for(c='a'
    c <= 'z'
    c++)
if((freq[j][c]-freq[i-1][c]) > 0)
uniqueCount++
# (Part 3)

# we can now iterate for all substring of length minLength

# so:

for(i=0
    i < s.length()-minLength
    i++)
{
    // so i to i+minLength-1 is substring starting at i
    // first we'll check if its valid(unique characters ...), i have explained it in part 2
    // if its unique, find hash value of substring s[i:i+minLength-1], which can be found quickly
    // if u use rolling hashing(read the link i provided)
    int hashValue = hash(i, i+minLength-1)
    map[hashValue]++
}
Now iterate through the map to find highest frequency hash value
