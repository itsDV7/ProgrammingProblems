class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size() - 1;
        int maxL = height[0];
        int maxR = height[n];
        int water = 0;
        int i=0, j=n;
        while (i < j){
            if (maxL <= maxR){
                i += 1;
                maxL = max(maxL, height[i]);
                water += maxL - height[i];
            }
            else{
                j -= 1;
                maxR = max(maxR, height[j]);
                water += maxR - height[j];
            }
        }
        return water;
    }
};
