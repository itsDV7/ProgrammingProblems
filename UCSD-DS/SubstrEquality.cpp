#include <iostream>
#include <vector>

using namespace std;

typedef unsigned long long ull;
constexpr auto UMOD = 18446744073709551557;

class Solver {
	string s;
	vector<ull> hashvals;

	ull pow_mod(ull base, ull exponent, ull modulus) {
		ull result = 1;
		while (exponent) {
			if (exponent % 2) {
				result = (result * result) % modulus;
			}
			base = (base * base) % modulus;
			exponent /= 2;
		}
		return result;
	}

public:
	Solver(string s) : s(s) {
		// initialization, precalculation
		ull randomval = 2;
		for (ull i = 0; i < s.length(); i++) {
			ull currenthash = 0;
			currenthash = (s[i] * (pow_mod(randomval, s.length() - 1 - i, UMOD))) % UMOD;
			if (i) {
				currenthash = (currenthash + hashvals[i - 1]) % UMOD;
			}
			hashvals.push_back(currenthash);
			//cout << s[i] << " " << hashvals[i] << "\n";
		}
	}
	bool ask(int a, int b, int l) {
		if ((hashvals[a + l - 1] - hashvals[a-1]) == (hashvals[b + l - 1] - hashvals[b-1])) {
			return s.substr(a, l) == s.substr(b, l);
		}
		else {
			return false;
		}
	}
};

int main() {
	ios_base::sync_with_stdio(0), cin.tie(0);

	string s;
	int q;
	cin >> s >> q;
	Solver solver(s);
	for (int i = 0; i < q; i++) {
		int a, b, l;
		cin >> a >> b >> l;
		cout << (solver.ask(a, b, l) ? "Yes\n" : "No\n");
	}
}
