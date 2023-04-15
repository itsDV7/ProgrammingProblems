class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> r(9, std::unordered_set<char>());
        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                if (board[i][j] != '.'){
                    if (r[i].count(board[i][j]) != 0){
                        // cout << "row";
                        return false;
                    }
                    else{
                        r[i].insert(board[i][j]);
                    }
                }
            }
        }

        vector<unordered_set<char>> c(9, std::unordered_set<char>());
        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                if (board[j][i] != '.'){
                    if (c[i].count(board[j][i]) != 0){
                        // cout << "col";
                        return false;
                    }
                    else{
                        c[i].insert(board[j][i]);
                    }
                }
            }
        }

        vector<unordered_set<char>> b(9, std::unordered_set<char>());
        int s=-1, bl=-1;
        for(int i=0; i<9; i++){
            if(i%3==0){
                s++;
            }
            bl = (3*s) - 1;
            for(int j=0; j<9; j++){
                if(j%3==0){
                    bl++;
                }
                if (board[i][j] != '.'){
                    if (b[bl].count(board[i][j]) != 0){
                        // cout << "block";
                        return false;
                    }
                    else{
                        b[bl].insert(board[i][j]);
                    }
                }
            // cout << "i: " << i << ", j: " << j << ", s: " << s << ", bl: " << bl << endl;
            }
        }
        return true;
    }
};
