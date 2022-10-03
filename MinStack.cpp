class Node {
    private:
        int val;
        Node* prev;
    friend class MinStack;
};


class MinStack {
    private:
        Node* head;
        Node* min = nullptr;
    public:
        MinStack() {
            head = new Node();
            head->prev = nullptr;
        }
        
        void push(int val) {
            Node* new_head = new Node();
            new_head->val = val;
            new_head->prev = head;
            head = new_head;

            findNewMin();
        }
        
        void pop() {
            if (head->prev == nullptr)
                ;
            else
            {
                Node* temp = head;
                head = head->prev;
                delete temp; 
            }

            findNewMin();
        }
        
        int top() {
            if (head->prev == nullptr)
                ;
            
            return head->val;
        }
        
        int getMin() {
            if (min == nullptr)
                ;

            return min->val;
        }

        void findNewMin() {
            Node* temp = head;
            min = head;
            while (true)
            {
                if (temp->prev != nullptr)
                {
                    if (temp->val < min->val)
                        min = temp;
                }
                else
                    break;

                temp = temp->prev;
            }
        }
};