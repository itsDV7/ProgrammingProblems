class Solution {
public:
    // set<int> rows;
    set<int> cols;
    set<int> posdiag;
    set<int> negdiag;
    vector<vector<string>> out;
    void bt(vector<vector<string>> board, int n, int i){
        if(i == n){
            vector<string> row;
            for(auto r:board){
                string s = "";
                for(auto p:r){
                    s += p;
                }
                row.push_back(s);
            }
            out.push_back(row);
            return;
        }
        for(int j=0; j<n; j++){
            if(find(cols.begin(), cols.end(), j) == cols.end() && find(posdiag.begin(), posdiag.end(), j+i) == posdiag.end() && find(negdiag.begin(), negdiag.end(), j-i) == negdiag.end()){
                cols.insert(j);
                posdiag.insert(j+i);
                negdiag.insert(j-i);
                board[i][j] = "Q";
                bt(board, n, i+1);
                board[i][j] = ".";
                cols.erase(j);
                posdiag.erase(j+i);
                negdiag.erase(j-i);
            }
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> board(n, vector<string>(n, "."));
        bt(board, n, 0);
        return out;
    }
};
