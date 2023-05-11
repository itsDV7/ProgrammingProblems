#include <iostream>

using namespace std;

struct Answer {
	size_t i, j, len;
};

Answer solve(const string& s, const string& t) {
	string smaller, larger;
	bool flip(false);
	if (s.length() < t.length()) {
		smaller = s;
		larger = t;
	}
	else {
		smaller = t;
		larger = s;
		flip = true;
	}

	Answer ans{};
	ans.i = 0;
	ans.j = 0;
	ans.len = 0;
	int left(0), right(smaller.length() - 1);
	while (left <= right) {
		int mid = left + (right - left) / 2;
		int l1(0);
		int r1(mid);
		bool breakall(false);
		while (r1 < smaller.length()) {
			int l2(0);
			int r2(mid);
			while (r2 < larger.length()) {
				if (smaller.substr(l1, mid + 1) == larger.substr(l2, mid + 1)) {
					if (flip) {
						ans.i = l2;
						ans.j = l1;
					}
					else {
						ans.i = l1;
						ans.j = l2;
					}
					ans.len = mid + 1;
					left = mid + 1;
					breakall = true;
					break;
				}
				l2 += 1;
				r2 += 1;
			}
			if (breakall) {
				break;
			}
			l1 += 1;
			r1 += 1;
		}
		if (!breakall) {
			right = mid - 1;
		}
	}

	return ans;

}

int main() {
	ios_base::sync_with_stdio(false), cin.tie(0);
	string s, t;
	while (cin >> s >> t) {
		auto ans = solve(s, t);
		cout << ans.i << " " << ans.j << " " << ans.len << "\n";
	}
}
