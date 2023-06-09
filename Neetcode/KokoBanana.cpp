#include <iomanip>
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        std::cout << std::fixed << std::setprecision(10);
        int left = 1;
        int right = -1;
        for (int i=0; i<piles.size(); i++){
            right = max(right, piles[i]);
        }
        int mid = -1;
        int minspeed = right+1;
        while (left <= right){
            mid = left + (right - left)/2;
            long long int hours = 0;
            // cout << mid << "\n";
            for (int i=0; i<piles.size(); i++){
                // cout << static_cast<long double>(piles[i])/static_cast<long double>(mid) << "\n";
                hours += ceil(static_cast<long double>(piles[i])/static_cast<long double>(mid));
                // cout << hours << "\n";
            }
            if (hours <= h){
                minspeed = min(minspeed, mid);
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        return minspeed;
    }
};
