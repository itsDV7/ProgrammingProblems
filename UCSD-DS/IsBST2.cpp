#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
#if defined(__unix__) || defined(__APPLE__)
#include <sys/resource.h>
#endif

using std::vector;
using std::ios_base;
using std::cin;
using std::cout;
using std::endl;

int prevkey = std::numeric_limits<int>::min();

struct Node {
    int key;
    int left;
    int right;

    Node() : key(0), left(-1), right(-1) {}
    Node(int key_, int left_, int right_) : key(key_), left(left_), right(right_) {}
};

bool lrri(int index, vector<Node> tree, bool isbst, bool rightsubtree) {
    if (index == -1) {
        return isbst;
    }
    isbst = isbst && lrri(tree[index].left, tree, isbst, rightsubtree);
    if (!rightsubtree) {
        if (tree[index].key <= prevkey) {
            isbst = false;
        }
        else {
            prevkey = tree[index].key;
            isbst = isbst && true;
        }
    }
    else {
        if (tree[index].key < prevkey) {
            isbst = false;
        }
        else {
            prevkey = tree[index].key;
            isbst = isbst && true;
        }
    }
    rightsubtree = true;
    isbst = isbst && lrri(tree[index].right, tree, isbst, rightsubtree);
    return isbst;
}

bool IsBinarySearchTree(const vector<Node>& tree) {
    // Implement correct algorithm here

    if (tree.empty()) {
        return true;
    }
    
    bool inrightsubtree = false;

    if (tree[0].left != -1) {
        return lrri(0, tree, true, false);
    }
    else {
        return lrri(0, tree, true, true);
    }

}

int main_with_large_stack_space() {
    ios_base::sync_with_stdio(0);
    int nodes;
    cin >> nodes;
    vector<Node> tree;
    for (int i = 0; i < nodes; ++i) {
        int key, left, right;
        cin >> key >> left >> right;
        tree.push_back(Node(key, left, right));
    }
    if (IsBinarySearchTree(tree)) {
        cout << "CORRECT" << endl;
    }
    else {
        cout << "INCORRECT" << endl;
    }
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
