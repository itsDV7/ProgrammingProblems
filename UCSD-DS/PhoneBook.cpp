#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using std::string;
using std::vector;
using std::cin;
using std::unordered_map;

struct Query {
    string type, name;
    int number;
};

vector<Query> read_queries() {
    int n;
    cin >> n;
    vector<Query> queries(n);
    for (int i = 0; i < n; ++i) {
        cin >> queries[i].type;
        if (queries[i].type == "add")
            cin >> queries[i].number >> queries[i].name;
        else
            cin >> queries[i].number;
    }
    return queries;
}

void write_responses(const vector<string>& result) {
    for (size_t i = 0; i < result.size(); ++i)
        std::cout << result[i] << "\n";
}

vector<string> process_queries(const vector<Query>& queries) {

    vector<string> result;
    //vector<string> contacts;
	//contacts.reserve(1e8);
	unordered_map<int, string> contacts;

    for (int i = 0; i < queries.size(); i++) {
        if (queries[i].type == "add") {
            contacts[queries[i].number] = queries[i].name;
        }
        else if (queries[i].type == "del") {
            //contacts[queries[i].number] = "not found";
			if (contacts.find(queries[i].number) != contacts.end()){
				contacts.erase(contacts.find(queries[i].number));
			}
        }
        else if (queries[i].type == "find") {
			//if (contacts[queries[i].number] == ""){
			//	result.push_back("not found");
			//}
			//else{
			//	result.push_back(contacts[queries[i].number]);
			//}
			if (contacts.find(queries[i].number) != contacts.end()){
				result.push_back(contacts[queries[i].number]);
			}
			else{
				result.push_back("not found");
			}
        }
    }

    return result;

}

int main() {
    write_responses(process_queries(read_queries()));
    return 0;
}
