class Solution {
public:
    bool isValid(string s) {
        vector<char> buffer;
        for (char i: s)
        {
            if (isOpening(i))
                buffer.push_back(i);
            else
            {
                if (buffer.size() > 0)
                    if (closingPar(buffer.back()) == i)
                        buffer.pop_back();
                    else
                        return false;
                else
                    return false;
                
            }
        }
        if (buffer.size() > 0)
            return false;
        else
            return true;
    }
    
    bool isOpening(char c)
    {
        if (c == '(' || c == '[' or c == '{')
            return true;
        else
            return false;
    }
    
    char closingPar(char c)
    {
        if (c == '(')
            return c + 1;
        else
            return c + 2;
    }
};
