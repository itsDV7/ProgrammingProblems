//#include <iostream>
//#include <stack>
//#include <sstream>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//int main() {
//
//	stack<int> input_stack, max_stack;
//	int n;
//	cin >> n;
//
//	vector<int> ans;
//	string line;
//	for (int i = 0; i < n; i++) {
//		getline(cin >> ws, line);
//		if (line == "max") {
//			ans.push_back(max_stack.top());
//		}
//		else if (line == "pop") {
//			input_stack.pop();
//			max_stack.pop();
//		}
//		else {
//			istringstream ss(line);
//			vector<string> ins;
//			string x;
//			while (ss >> x) {
//				ins.push_back(x);
//			}
//			input_stack.push(stoi(ins.back()));
//			if (max_stack.empty()) {
//				max_stack.push(input_stack.top());
//			}
//			else {
//				max_stack.push(max(max_stack.top(), input_stack.top()));
//			}
//		}
//	}
//	for (int i = 0; i < ans.size() - 1; i++) {
//		cout << ans[i] << "\n";
//	}
//	cout << ans.back();
//
//	return 0;
//}

#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <algorithm>

using std::cin;
using std::string;
using std::vector;
using std::cout;
using std::max_element;
using std::max;

class StackWithMax {
    vector<int> stack;
    vector<int> max_stack;
public:

    void Push(int value) {
        stack.push_back(value);
        if (max_stack.empty())
            max_stack.push_back(value);
        else
            max_stack.push_back(max(max_stack.back(), value));
    }

    void Pop() {
        assert(stack.size());
        stack.pop_back();
        max_stack.pop_back();
    }

    int Max() const {
        assert(stack.size());
        return max_stack.back();
        //return *max_element(stack.begin(), stack.end());
    }
};

int main() {
    int num_queries = 0;
    cin >> num_queries;
    
    string query;
    string value;

    StackWithMax stack;
    vector<int> ans;

    for (int i = 0; i < num_queries; ++i) {
        cin >> query;
        if (query == "push") {
            cin >> value;
            
            stack.Push(std::stoi(value));
        }
        else if (query == "pop") {
            stack.Pop();
        }
        else if (query == "max") {
            ans.push_back(stack.Max());
        }
        else {
            assert(0);
        }
    }
    for (int i = 0; i < ans.size(); i++) {
        if (i != ans.size()-1)
            cout << ans[i] << '\n';
        else
            cout << ans[i];
    }
    return 0;
}
