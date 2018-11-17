// 对每一个数，都需要根号N次判断。
// 从2到根号N遍历，判断是否能整除num。  // 容易理解，效率极低。

#include <iostream>
using namespace std;

bool isPrime(int num)
{
    for(int i=2; i*i < num+1; ++i)
    {
        if(!(num % i))
        {
            return false;
        }
    }
    return true;
}

int main(int argc, char* const argv[])
{
    for(int i=0; i<50; ++i)
    {
        if( isPrime(i) )
        {
            cout << i << endl;
        }
    }
}
