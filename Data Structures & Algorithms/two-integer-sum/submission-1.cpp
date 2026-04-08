class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> table; // number; its pair position
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            if (table.find(num) != table.end()) {
             return {table[num], i};
            }
            table[target - num] = i;
        }
    return {-1, -1};
  }

};
