class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());

        for(int i = 0; i < nums.size(); i++){
            int j = i + 1;
            int k = nums.size()-1;
            while(j < k){
                int sum = nums[i] + nums[j] + nums[k];
                if(sum == 0){
                    result.push_back(vector<int>{nums[i], nums[j], nums[k]});
                    while(j < k){
                        j++;
                        if(nums[j] != nums[j-1]) break;
                    }
                }else{
                    sum < 0 ? j++ : k--;
                }
                
            }
            while(nums[i] == nums[i+1]){
                i++;
            }
        }
        return result;
    }
};
