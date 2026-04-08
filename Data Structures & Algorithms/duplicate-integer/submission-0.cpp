class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> checked;
            for (auto num : nums) {
            if (checked.find(num) != checked.end()) {
                return true;
            }
            checked.insert(num);
            }
        return false;
    }
};