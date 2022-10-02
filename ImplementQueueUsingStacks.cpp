class MyQueue {
public:
    vector<int> q;
    MyQueue(vector<int> v = {}) {
        q = v;
    }
    
    void push(int x) {
        q.push_back(x);
    }
    
    int pop() {
        int popped = q[0];
        q.erase(q.begin());
        return popped;
    }
    
    int peek() {
        return q.front();
    }
    
    bool empty() {
        return q.empty();
    }
};
