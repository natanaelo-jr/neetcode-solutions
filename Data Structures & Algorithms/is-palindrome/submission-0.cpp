class Solution {
public:
    bool isPalindrome(string s) {
        string s_alnum;
        for(auto c : s){
            if(isalnum(c)){
                s_alnum += tolower(c);
            }
        }
        s = s_alnum;
        int left = 0;
        int right = s.size() - 1;

        while(left < right){
            if(s[left] != s[right]){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
