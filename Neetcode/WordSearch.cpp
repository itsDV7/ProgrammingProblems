class Solution {
public:
    bool check(vector<vector<char>> board, string word, int i, int j, vector<vector<bool>>& visited, int w){
        if (w == word.size()-1){
            return true;
        }
        visited[i][j] = true;
        bool next = false;
        if (i >= 0 && i < board.size() && j-1 >= 0 && j-1 < board[0].size() && board[i][j-1] == word[w+1] && !visited[i][j-1]){
            next = next || check(board, word, i, j-1, visited, w+1);
            if (next){
                return next;
            }
        }
        if (i >= 0 && i < board.size() && j+1 >= 0 && j+1 < board[0].size() && board[i][j+1] == word[w+1] && !visited[i][j+1]){
            next = next || check(board, word, i, j+1, visited, w+1);
            if (next){
                return next;
            }
        }
        if (i-1 >= 0 && i-1 < board.size() && j >= 0 && j < board[0].size() && board[i-1][j] == word[w+1] && !visited[i-1][j]){
            next = next || check(board, word, i-1, j, visited, w+1);
            if (next){
                return next;
            }
        }
        if (i+1 >= 0 && i+1 < board.size() && j >= 0 && j < board[0].size() && board[i+1][j] == word[w+1] && !visited[i+1][j]){
            next = next || check(board, word, i+1, j, visited, w+1);
            if (next){
                return next;
            }
        }
        visited[i][j] = false;
        return next;
    }
    bool exist(vector<vector<char>>& board, string word) {
        vector<vector<bool>> visited(board.size(), vector<bool> (board[0].size(), false));
        set<char> boardSet;
        set<char> wordSet(word.begin(), word.end());
        for(int i=0; i<board.size(); i++){
            for(int j=0; j<board[0].size(); j++){
                boardSet.insert(board[i][j]);
            }
        }
        // cout << "BS " << boardSet.size();
        // cout << "\n";
        // cout << "WS " << wordSet.size();
        // cout << "\n";
        // for(auto b:boardSet){
        //     cout << b << " ";
        // }
        // cout << "\n";
        // for(auto w:wordSet){
        //     cout << w << " ";
        // }
        // cout << "\n";
        for(auto w:wordSet){
            if(find(boardSet.begin(), boardSet.end(), w) == boardSet.end()){
                // cout << "didnt match";
                return false;
            }
        }
        for(int i=0; i<board.size(); i++){
            for(int j=0; j<board[0].size(); j++){
                if(board[i][j] == word[0] && check(board, word, i, j, visited, 0)){
                    return true;
                }
            }
        }
        return false;
    }
};
