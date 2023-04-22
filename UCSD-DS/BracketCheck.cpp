//#include <iostream>
//#include <vector>
//#include <string>
//typedef long long int ll;
//
//using namespace std;
//
//int main() {
//
//	string s;
//	getline(cin, s);
//
//	vector<char> stack;
//	vector<ll> index;
//
//	for (int c = 0; c < s.length(); c++) {
//
//		if ((char(s[c]) == char('(')) || (char(s[c]) == char('{')) || (char(s[c]) == char('[')) ||
//			(char(s[c]) == char(')')) || (char(s[c]) == char('}')) || (char(s[c]) == char(']'))) {
//			stack.push_back(s[c]);
//			index.push_back(c);
//		}
//
//		if (stack.size() >= 2) {
//			if ( ((stack[stack.size()-2] == char('(')) && (stack.back() == char(')'))) ||
//				 ((stack[stack.size()-2] == char('{')) && (stack.back() == char('}'))) ||
//				 ((stack[stack.size()-2] == char('[')) && (stack.back() == char(']'))) ) {
//				stack.pop_back();
//				stack.pop_back();
//				index.pop_back();
//				index.pop_back();
//			}
//		}
//	}
//
//	if (stack.empty()) {
//		cout << "Success";
//	}
//	else {
//		cout << index.back()+1;
//	}
//
//	return 0;
//
//}

#include <iostream>
#include <stack>
#include <string>

struct Bracket {
    Bracket(char type, int position) :
        type(type),
        position(position)
    {}

    bool Matchc(char c) {
        if (type == '[' && c == ']')
            return true;
        if (type == '{' && c == '}')
            return true;
        if (type == '(' && c == ')')
            return true;
        return false;
    }

    char type;
    int position;
};

int main() {
    std::string text;
    getline(std::cin, text);

    std::stack <Bracket> opening_brackets_stack;
    for (int position = 0; position < text.length(); ++position) {
        char next = text[position];
        
        if (next == '(' || next == '[' || next == '{') {
            // Process opening bracket, write your code here
            opening_brackets_stack.push(Bracket(next, position));
            continue;
        }
        
        if (next == ')' || next == ']' || next == '}') {
            // Process closing bracket, write your code here
            if (opening_brackets_stack.empty()) {
                std::cout << position + 1;
                return 0;
            }
            if (opening_brackets_stack.top().Matchc(next)) {
                opening_brackets_stack.pop();
                continue;
            }
            else {
                std::cout << position + 1;
                return 0;
            }
        }
    }

    // Printing answer, write your code here
    if (opening_brackets_stack.empty()) {
        std::cout << "Success";
    }
    else {
        std::cout << opening_brackets_stack.top().position + 1;
    }

    return 0;
}
