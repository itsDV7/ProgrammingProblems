class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<pair<int, int>> blocks;
        int area(0);
        for (int i=0; i<heights.size(); i++){
            if (blocks.empty()){
                blocks.push(make_pair(heights[i], i));
            }
            else{
                if (blocks.top().first <= heights[i]){
                    blocks.push(make_pair(heights[i], i));
                }
                else{
                    int last_index(-1);
                    while (!blocks.empty() && blocks.top().first > heights[i]){
                        area = max(area, blocks.top().first * (i-blocks.top().second));
                        last_index = blocks.top().second;
                        blocks.pop();
                    }
                    blocks.push(make_pair(heights[i], last_index));
                }
            }
        }
        while (!blocks.empty()){
            area = max(area, (int)(blocks.top().first * (heights.size()-blocks.top().second)));
            blocks.pop();
        }
        return area;
    }
};
