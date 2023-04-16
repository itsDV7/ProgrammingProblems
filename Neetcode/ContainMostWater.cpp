class Solution {
public:
    int maxArea(vector<int>& height) {
        // Naive O(n^2)
        // int n = height.size();
        // int vol(0);
        // for(int i=0; i<n; i++){
        //     for(int j=i+1; j<n; j++){
        //         vol = max(vol, min(height[i], height[j]) * (j-i));
        //     }
        // }
        // return vol;
        
        int n = height.size();
        int i = 0, j = n-1;
        int vol = 0;
        while (i<j){
            vol = max(vol, min(height[i], height[j]) * (j-i));
            if (height[i] < height[j]){
                i += 1;
            }
            else{
                j -= 1;
            }
        }
        return vol;
    }
};
