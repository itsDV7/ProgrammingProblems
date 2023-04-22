//#include <iostream>
//#include <map>
//#include <vector>
//#include <stack>
//#include <queue>
//
//using namespace std;
//
//int main() {
//	
//	int n;
//	cin >> n;
//
//	int p;
//	vector<int> parent;
//
//	for (int i = 0; i < n; i++) {
//		cin >> p;
//		parent.push_back(p);
//	}
//
//	int height = 0;
//	vector<int> dp(n, 0);
//	for (int i = 0; i < n; ++i) {
//		if (parent[i] == -1) {
//			dp[i] = 0;
//			continue;
//		}
//		if (dp[i] == 0) {
//			p = parent[i];
//			while (p != -1) {
//				if (dp[p] != 0) {
//					height += dp[p] + 1;
//					break;
//				}
//				else {
//					height += 1;
//					p = parent[p];
//				}
//			}
//			dp[i] = height;
//			height = 0;
//		}
//	}
//	
//	cout << *max_element(dp.begin(), dp.end()) + 1;
//
//	return 0;
//}

#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
#if defined(__unix__) || defined(__APPLE__)
#include <sys/resource.h>
#endif

class Node;

class Node {
public:
    int key;
    Node* parent;
    std::vector<Node*> children;

    Node() {
        this->parent = NULL;
    }

    void setParent(Node* theParent) {
        parent = theParent;
        parent->children.push_back(this);
    }
};

int calc_height(Node* head) {
    std::queue<Node*> nodeq;
    nodeq.push(head);
    int height = 0;
    while (!nodeq.empty()) {
        int qsize = nodeq.size();
        for (int i = 0; i < qsize; i++) {
            for (auto c : nodeq.front()->children) {
                nodeq.push(c);
            }
            nodeq.pop();
        }
        height += 1;
    }
    return height;
}

int main_with_large_stack_space() {
    std::ios_base::sync_with_stdio(0);
    int n;
    std::cin >> n;

    std::vector<Node> nodes;
    nodes.resize(n);
    int head_index;
    Node* head;
    for (int child_index = 0; child_index < n; child_index++) {
        int parent_index;
        std::cin >> parent_index;
        if (parent_index >= 0)
            nodes[child_index].setParent(&nodes[parent_index]);
        else
            head_index = child_index;
        nodes[child_index].key = child_index;
    }
    head = &nodes[head_index];
    std::cout << calc_height(head);

    // Replace this code with a faster implementation -> Calculates height from every node to apex. Return maxheight. O(n^2).
    /*int maxHeight = 0;
    for (int leaf_index = 0; leaf_index < n; leaf_index++) {
        int height = 0;
        for (Node* v = &nodes[leaf_index]; v != NULL; v = v->parent)
            height++;
        maxHeight = std::max(maxHeight, height);
    }

    std::cout << maxHeight << std::endl;*/
    return 0;
}

int main(int argc, char** argv)
{
#if defined(__unix__) || defined(__APPLE__)
    // Allow larger stack space
    const rlim_t kStackSize = 16 * 1024 * 1024;   // min stack size = 16 MB
    struct rlimit rl;
    int result;

    result = getrlimit(RLIMIT_STACK, &rl);
    if (result == 0)
    {
        if (rl.rlim_cur < kStackSize)
        {
            rl.rlim_cur = kStackSize;
            result = setrlimit(RLIMIT_STACK, &rl);
            if (result != 0)
            {
                std::cerr << "setrlimit returned result = " << result << std::endl;
            }
        }
    }

#endif
    return main_with_large_stack_space();
}
