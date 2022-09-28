#include <iostream>
#include <cmath>
using namespace std;
int main()
{
        int n,m,a;
        unsigned long long n_tiles, m_tiles;
        cin >> n >> m >> a;
        n_tiles =  ceil(n/a);
        if (n%a)
                n_tiles++;
        m_tiles = ceil(m/a);
        if (m%a)
                m_tiles++;
        cout << n_tiles * m_tiles;
}
