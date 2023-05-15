#include <limits>
#include <algorithm>
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> A = (nums1.size() < nums2.size()) ? nums2 : nums1;
        vector<int> B = (nums1.size() < nums2.size()) ? nums1 : nums2;

        if (B.empty()){
            int left = 0;
            int right = A.size() - 1;
            int mid = left + (right - left)/2;
            if (A.size() % 2){
                return A[mid];
            }
            else{
                return (A[mid] + A[mid + 1])/2.0;
            }
        }

        int left = 0;
        int right = A.size() - 1;
        int group = (A.size() + B.size())/2;

        while (left <= right && B.size() > 1){
            int mid = left + (right - left)/2;
            int rem = group - mid - 2;

            if (rem < 0){
                break; // Dumb Code Here :)
                rem = -1;
                left -= 1;
                continue;
            }
            else if (rem >= B.size()){
                break;
                rem = B.size()-1;
                right += 1;
                continue;
            }
            
            int aleft = (mid >= 0) ? A[mid] : numeric_limits<int>::min();
            int aright = ((mid + 1) < A.size()) ? A[mid + 1] : numeric_limits<int>::max();
            int bleft = (rem >= 0) ? B[rem] : numeric_limits<int>::min();
            int bright = ((rem + 1) < B.size()) ? B[rem + 1] : numeric_limits<int>::max();

            if ((aleft <= bright) && (bleft <= aright)){
                if ((A.size() + B.size()) % 2){
                    cout << "O";
                    return min(aright, bright);
                }
                else{
                    cout << "E";
                    return static_cast<double>(max(aleft, bleft) + min(aright, bright))/2.0;
                }
            }
            else if (aleft > bright){
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }

        }
        // One elem in A
        A.insert(A.end(), B.begin(), B.end());
        sort(A.begin(), A.end());
        int mid = (A.size() - 1)/2;
        if (A.size() % 2){
            cout << "OO";
            return A[mid];
        }
        else{
            cout << "OE";
            return static_cast<double>(A[mid] + A[mid + 1])/2.0;
        }
    }
};
