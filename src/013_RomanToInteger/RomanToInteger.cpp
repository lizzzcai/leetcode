#include <string>
#include  <map>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        int result = 0;
        int len = s.length();
        
        if (len == 0)
            return result;
        
        // build the map
        map<char, int> dict;
        dict['I'] = 1;
        dict['V'] = 5;
        dict['X'] = 10;
        dict['L'] = 50;
        dict['C'] = 100;
        dict['D'] = 500;
        dict['M'] = 1000;
        
        result = dict[s[len-1]];
        if (len == 1)
            return result;
        
        for (int i = len - 2; i >= 0; --i)
            dict[s[i]] < dict[s[i+1]] ? result -= dict[s[i]] : result +=dict[s[i]];
        return result;               
    }
};