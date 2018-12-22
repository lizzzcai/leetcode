#include <vector>
#include <unordered_map>


using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // hash [i] contains the number index with value i
        unordered_map<int, int> hash;
        vector<int> result;
        
        // go through every number and add them into hashmap
        for (int i = 0; i < nums.size();i++){  // for every data in the nums set
            //hash.find(target - nums[i]) != hash.end()
            if (hash.count(target - nums[i])){ 
                // the index of target - nums[i] is smaller, place in the front
                result.push_back(hash[target-nums[i]]);
                result.push_back(i);
                return result;
            }
            hash[nums[i]]=i;
        }
        
        // if no solution
        result.push_back(-1);
        result.push_back(-1);
        return result;
        
    }
};