//#include <iostream>
//#include <vector>
//
//using namespace std;
//
//int main() {
//
//	vector<int> ans;
//
//	int n, m;
//	cin >> n >> m;
//
//	int maxdata(0);
//	vector<int> rows(n);
//	for (int i = 0; i < n; i++) {
//		cin >> rows[i];
//		maxdata = max(maxdata, rows[i]);
//	}
//
//	vector<int> links(n, -1);
//	int fr, to;
//	for (int i = 0; i < m; i++) {
//		cin >> fr >> to;
//		fr -= 1;
//		to -= 1;
//		if (links[fr] == -1 && links[to] == -1) {
//			links[fr] = to;
//			links[to] = to;
//			if (fr != to) {
//				rows[to] += rows[fr];
//				maxdata = max(maxdata, rows[to]);
//			}
//		}
//		else if (links[fr] == fr && links[to] == to) {
//			if (links[fr] != links[to]) {
//				links[fr] = to;
//				links[to] = to;
//				rows[to] += rows[fr];
//				maxdata = max(maxdata, rows[to]);
//			}
//		}
//		else if (links[fr] == fr && links[to] == -1) {
//			if (links[fr] != links[to]) {
//				links[fr] = to;
//				links[to] = to;
//				rows[to] += rows[fr];
//				maxdata = max(maxdata, rows[to]);
//			}
//		}
//		else if (links[fr] == -1 && links[to] == to) {
//			if (links[fr] != links[to]) {
//				links[fr] = to;
//				links[to] = to;
//				rows[to] += rows[fr];
//				maxdata = max(maxdata, rows[to]);
//			}
//		}
//		else if (links[fr] == -1 && links[to] != to) {
//			while (links[to] != to) {
//				to = links[to];
//			}
//			if (links[fr] != links[to]) {
//				links[fr] = to;
//				links[to] = to;
//				rows[to] += rows[fr];
//				maxdata = max(maxdata, rows[to]);
//			}
//		}
//		else {
//			while (links[to] != to) {
//				to = links[to];
//			}
//			while (links[fr] != fr) {
//				int nextlink(links[fr]);
//				links[fr] = to;
//				fr = nextlink;
//			}
//			if (links[fr] != links[to]) {
//				links[fr] = to;
//				links[to] = to;
//				rows[to] += rows[fr];
//				maxdata = max(maxdata, rows[to]);
//			}
//		}
//		//cout << maxdata << "\n";
//		ans.push_back(maxdata);
//	}
//
//	for (int a : ans) {
//		cout << a << "\n";
//	}
//
//	return 0;
//}

#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::max;
using std::vector;

struct DisjointSetsElement {
	int size, parent, rank;

	DisjointSetsElement(int size = 0, int parent = -1, int rank = 0) :
		size(size), parent(parent), rank(rank) {}
};

struct DisjointSets {
	int size;
	int max_table_size;
	vector <DisjointSetsElement> sets;

	DisjointSets(int size) : size(size), max_table_size(0), sets(size) {
		for (int i = 0; i < size; i++)
			sets[i].parent = i;
	}

	int getParent(int table) {
		// find parent and compress path
		int initial_table = table;
		while (sets[table].parent != table) {
			table = sets[table].parent;
		}
		while (sets[initial_table].parent != table) {
			int next_table = sets[initial_table].parent;
			sets[initial_table].parent = table;
			initial_table = next_table;
		}
		return table;
	}

	void merge(int destination, int source) {
		int realDestination = getParent(destination);
		int realSource = getParent(source);
		if (realDestination != realSource) {
			// merge two components
			// use union by rank heuristic
						// update max_table_size
			if (sets[realDestination].rank >= sets[realSource].rank) {
				sets[realDestination].size += sets[realSource].size;
				sets[realDestination].rank += 1;
				sets[realSource].parent = realDestination;
				max_table_size = max(max_table_size, sets[realDestination].size);
			}
			else {
				sets[realSource].size += sets[realDestination].size;
				sets[realSource].rank += 1;
				sets[realDestination].parent = realSource;
				max_table_size = max(max_table_size, sets[realSource].size);
			}
		}
	}
};

int main() {
	int n, m;
	cin >> n >> m;

	DisjointSets tables(n);
	for (auto& table : tables.sets) {
		cin >> table.size;
		tables.max_table_size = max(tables.max_table_size, table.size);
	}

	for (int i = 0; i < m; i++) {
		int destination, source;
		cin >> destination >> source;
		--destination;
		--source;

		tables.merge(destination, source);
		cout << tables.max_table_size << endl;
	}

	return 0;
}
