//#include <iostream>
//#include <vector>
//
//using namespace std;
//typedef long long int ll;
//
//
//class MinHeap {
//private:
//	vector<pair <ll, ll>> heap;
//
//	void _siftup(ll index) {
//		ll parent = (index - 1) / 2;
//		if (parent >= 0) {
//			if (this->heap[parent].second > this->heap[index].second) {
//				swap(this->heap[parent], this->heap[index]);
//				index = parent;
//				_siftup(index);
//			}
//			if (this->heap[parent].second == this->heap[index].second && this->heap[parent].first > this->heap[index].first) {
//				swap(this->heap[parent], this->heap[index]);
//				index = parent;
//				_siftup(index);
//			}
//		}
//	}
//
//	void _siftdown(ll index) {
//		ll left_child = 2 * index + 1;
//		ll right_child = 2 * index + 2;
//		ll swap_index = -1;
//
//		if (left_child < this->heap.size() && this->heap[left_child].first == -1 && this->heap[left_child].second < this->heap[index].second) {
//			swap_index = left_child;
//		}
//		if (right_child < this->heap.size() && this->heap[right_child].first == -1 && this->heap[right_child].second < this->heap[index].second && this->heap[right_child].second < this->heap[left_child].second) {
//			swap_index = right_child;
//		}
//
//		if (left_child < this->heap.size() && this->heap[left_child].first != -1 && this->heap[left_child].second < this->heap[index].second) {
//			swap_index = left_child;
//		}
//		if (right_child < this->heap.size() && this->heap[right_child].first != -1 && this->heap[right_child].second < this->heap[index].second && this->heap[right_child].second <= this->heap[left_child].second) {
//			if (this->heap[right_child].second == this->heap[left_child].second && this->heap[right_child].first < this->heap[left_child].first) {
//				swap_index = right_child;
//			}
//			if (this->heap[right_child].second < this->heap[left_child].second) {
//				swap_index = right_child;
//			}
//		}
//
//		if (left_child < this->heap.size() && this->heap[left_child].first != -1 && this->heap[left_child].second == this->heap[index].second && this->heap[left_child].first < this->heap[index].first) {
//			swap_index = left_child;
//		}
//		if (right_child < this->heap.size() && this->heap[left_child].first != -1 && this->heap[left_child].second == this->heap[index].second && this->heap[right_child].first < this->heap[index].first && this->heap[right_child].second <= this->heap[left_child].second) {
//			if (this->heap[right_child].second == this->heap[left_child].second && this->heap[right_child].first < this->heap[left_child].first) {
//				swap_index = right_child;
//			}
//			if (this->heap[right_child].second < this->heap[left_child].second) {
//				swap_index = right_child;
//			}
//		}
//
//		if (swap_index != -1) {
//			swap(this->heap[index], this->heap[swap_index]);
//			index = swap_index;
//			_siftdown(index);
//		}
//
//	}
//
//public:
//	void insert(pair <ll, ll> pair) {
//		this->heap.push_back(pair);
//		if (!this->heap.empty()) {
//			_siftup(this->heap.size() - 1);
//		}
//	}
//
//	pair <ll, ll> extractmin() {
//		if (!this->heap.empty()) {
//			pair <ll, ll> minval(this->heap[0]);
//			swap(this->heap[0], this->heap[this->heap.size() - 1]);
//			this->heap.pop_back();
//			_siftdown(0);
//			return minval;
//		}
//		else {
//			return make_pair(-1, -1);
//		}
//	}
//
//	pair <ll, ll> getmin() {
//		if (!this->heap.empty()) {
//			return this->heap[0];
//		}
//		else {
//			return make_pair(-1, -1);
//		}
//	}
//};
//
//
//int main() {
//
//	MinHeap timeheap;
//	MinHeap procheap;
//
//	ll n, m;
//	cin >> n >> m;
//
//	vector <ll> parr(m);
//	for (ll i = 0; i < m; i++) {
//		cin >> parr[i];
//	}
//
//	for (ll i = 0; i < n; i++) {
//		procheap.insert(make_pair(-1, i));
//	}
//
//	vector<ll> time(n, 0);
//
//	ll i(0);
//	while (i < m) {
//		pair <ll, ll> procmin = procheap.getmin(), timemin;
//		if (procmin.first != -1 or procmin.second != -1) {
//			procmin = procheap.extractmin();
//			cout << procmin.second << " " << time[procmin.second] << "\n";
//			time[procmin.second] += parr[i];
//			timeheap.insert(make_pair(procmin.second, time[procmin.second]));
//			i += 1;
//		}
//		else {
//			timemin = timeheap.extractmin();
//			procheap.insert(make_pair(-1, timemin.first));
//		}
//	}
//
//	return 0;
//}

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using std::vector;
using std::cin;
using std::cout;
using std::priority_queue;

class Processor {
public:
    int proc;
    long long int freetime;

    Processor(int proc) {
        this->proc = proc;
        this->freetime = 0;
    }
};

struct CompareTime {
    bool operator()(Processor& a, Processor& b) {
        if (a.freetime == b.freetime) {
            return a.proc > b.proc;
        }
        return a.freetime > b.freetime;
    }
};

class JobQueue {
private:
    int num_workers_;
    vector<int> jobs_;

    vector<int> assigned_workers_;
    vector<long long> start_times_;

    void WriteResponse() const {
        for (int i = 0; i < jobs_.size(); ++i) {
            cout << assigned_workers_[i] << " " << start_times_[i] << "\n";
        }
    }

    void ReadData() {
        int m;
        cin >> num_workers_ >> m;
        jobs_.resize(m);
        for (int i = 0; i < m; ++i)
            cin >> jobs_[i];
    }

    void AssignJobs() {
        // TODO: replace this code with a faster algorithm.
        assigned_workers_.resize(jobs_.size());
        start_times_.resize(jobs_.size());
        priority_queue<Processor, vector<Processor>, CompareTime> pq;

        for (int i = 0; i < num_workers_; i++) {
            pq.push(Processor(i));
        }

        for (int i = 0; i < jobs_.size(); i++) {
            Processor freeproc = pq.top();
            pq.pop();
            assigned_workers_[i] = freeproc.proc;
            start_times_[i] = freeproc.freetime;
            freeproc.freetime += jobs_[i];
            pq.push(freeproc);
        }

        //vector<long long> next_free_time(num_workers_, 0);
        //for (int i = 0; i < jobs_.size(); ++i) {
        //    int duration = jobs_[i];
        //    int next_worker = 0;
        //    for (int j = 0; j < num_workers_; ++j) {
        //        if (next_free_time[j] < next_free_time[next_worker])
        //            next_worker = j;
        //    }
        //    assigned_workers_[i] = next_worker;
        //    start_times_[i] = next_free_time[next_worker];
        //    next_free_time[next_worker] += duration;
        //}
    }

public:
    void Solve() {
        ReadData();
        AssignJobs();
        WriteResponse();
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);
    JobQueue job_queue;
    job_queue.Solve();
    return 0;
}
