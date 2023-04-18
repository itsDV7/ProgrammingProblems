class MinStack {
public:
    stack<int> s;
    stack<int> ms;

    MinStack() {
    }
    
    void push(int val) {
        s.push(val);
        if(ms.empty()){
            ms.push(val);
        }
        else{
            if(val < ms.top()){
                ms.push(val);
            }
            else{
                ms.push(ms.top());
            }
        }
    }
    
    void pop() {
        s.pop();
        ms.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return ms.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
