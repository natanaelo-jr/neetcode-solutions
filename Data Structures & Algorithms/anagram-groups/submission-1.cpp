class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, int> indexes;
        vector<vector<string>> groups;
        int unique_idx = 0;

        for(int i = 0; i < strs.size(); i++){
            string str = strs[i];
            sort(str.begin(), str.end());
            if(indexes.find(str) == indexes.end()){
                indexes[str] = unique_idx;
                unique_idx++;
                groups.push_back({strs[i]});
            } else{
                groups[indexes[str]].push_back(strs[i]);
            }
        }
    return groups;
    }
};
