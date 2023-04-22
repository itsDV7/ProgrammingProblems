#include <iostream>
#include <vector>
//#include <stack>
#include <deque>

using namespace std;
typedef long long int ll;

vector<ll> sol(vector<ll> arr, ll n, ll w) {
	vector<ll> sol_ans;
	deque<ll> Q;
	ll i = 0;
	for (; i < w; ++i) {
		while ((!Q.empty()) && arr[i] >= arr[Q.back()]) {
			Q.pop_back();
		}
		Q.push_back(i);
	}
	for (; i < n; ++i) {
		sol_ans.push_back(arr[Q.front()]);
		while ((!Q.empty()) && Q.front() <= i-w) {
			Q.pop_front();
		}
		while ((!Q.empty()) && arr[i] >= arr[Q.back()]) {
			Q.pop_back();
		}
		Q.push_back(i);
	}
	sol_ans.push_back(arr[Q.front()]);
	return sol_ans; 
}

int main() {
	
	int n;
	cin >> n;

	vector<ll> arr(n);
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	
	int w;
	cin >> w;

	for (int c : sol(arr, n, w)) {
		cout << c << " ";
	}

	return 0;
}
