//#include <iostream>
//#include <vector>
//
//using namespace std;
//
//int main() {
//
//	int n;
//	cin >> n;
//
//	vector<int> arr(n);
//	for (int i = 0; i < n; i++) {
//		cin >> arr[i];
//	}
//
//	vector<pair<int, int>> swaps;
//	for (int i = (arr.size() / 2) + 1; i >= 0; i--) {
//		int index = i;
//		while (index < arr.size()) {
//			int left_child = 2 * index + 1;
//			int right_child = 2 * index + 2;
//			int swap_index = -1;
//			if (left_child && left_child < arr.size() && arr[left_child] < arr[index]) {
//				swap_index = left_child;
//			}
//			if (right_child && right_child < arr.size() && arr[right_child] < arr[index] && arr[right_child] < arr[left_child]) {
//				swap_index = right_child;
//			}
//			if (swap_index > -1) {
//				int temp = arr[index];
//				arr[index] = arr[swap_index];
//				arr[swap_index] = temp;
//				swaps.push_back(make_pair(index, swap_index));
//				index = swap_index;
//			}
//			else {
//				break;
//			}
//		}
//	}
//
//	cout << swaps.size() << "\n";
//	for (auto swap : swaps) {
//		cout << swap.first << " " << swap.second << "\n";
//	}
//
//	return 0;
//}

#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::cin;
using std::cout;
using std::swap;
using std::pair;
using std::make_pair;

class HeapBuilder {
private:
    vector<int> data_;
    vector< pair<int, int> > swaps_;

    void WriteResponse() const {
        cout << swaps_.size() << "\n";
        for (int i = 0; i < swaps_.size(); ++i) {
            cout << swaps_[i].first << " " << swaps_[i].second << "\n";
        }
    }

    void ReadData() {
        int n;
        cin >> n;
        data_.resize(n);
        for (int i = 0; i < n; ++i)
            cin >> data_[i];
    }

    void GenerateSwaps() {
        swaps_.clear();
        // The following naive implementation just sorts 
        // the given sequence using selection sort algorithm
        // and saves the resulting sequence of swaps.
        // This turns the given array into a heap, 
        // but in the worst case gives a quadratic number of swaps.
        //
        // TODO: replace by a more efficient implementation
        for (int i = (data_.size() / 2) + 1; i >= 0; i--) {
            int index = i;
            while (index < data_.size()) {
                int left_child = 2 * index + 1;
                int right_child = 2 * index + 2;
                int swap_index = -1;
                if (left_child && left_child < data_.size() && data_[left_child] < data_[index]) {
                    swap_index = left_child;
                }
                if (right_child && right_child < data_.size() && data_[right_child] < data_[index] && data_[right_child] < data_[left_child]) {
                    swap_index = right_child;
                }
                if (swap_index > -1) {
                    swap(data_[index], data_[swap_index]);
                    swaps_.push_back(make_pair(index, swap_index));
                    index = swap_index;
                }
                else {
                    break;
                }
            }
        }
    }

public:
    void Solve() {
        ReadData();
        GenerateSwaps();
        WriteResponse();
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);
    HeapBuilder heap_builder;
    heap_builder.Solve(); 
    return 0;
}
