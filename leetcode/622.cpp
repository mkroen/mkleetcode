/*
 * @lc app=leetcode.cn id=622 lang=cpp
 *
 * [622] 设计循环队列
 */
/*
另可以使用k+1长度数组判断是否满空
或者使用链表实现
*/
#include <iostream>
#include <vector>
using namespace std;
// @lc code=start
class MyCircularQueue
{
private:
    vector<int> queue;
    int front = 0;
    int end = -1;
    int count = 0;
    int MAX_INDEX;

public:
    MyCircularQueue(int k)
    {
        this->queue = vector<int>(k);
        this->MAX_INDEX = k;
    }

    bool enQueue(int value)
    {
        if (isFull())
        {
            return false;
        }
        ++end;
        end %= MAX_INDEX;
        queue[end] = value;
        ++count;
        return true;
    }

    bool deQueue()
    {
        if (isEmpty())
        {
            return false;
        }
        ++front;
        front %= MAX_INDEX;
        --count;
        return true;
    }
    int Front()
    {
        if (isEmpty())
        {
            return -1;
        }
        return queue[front];
    }

    int Rear()
    {
        if (isEmpty())
        {
            return -1;
        }
        return queue[end];
    }

    bool isEmpty()
    {
        return true ? count == 0 : false;
    }

    bool isFull()
    {
        return true ? count == MAX_INDEX : false;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
// @lc code=end
int main()
{
    MyCircularQueue S = MyCircularQueue(5);
    cout << S.isEmpty() << endl;
    cout << S.enQueue(5) << endl;
    cout << S.Front() << endl;
    cout << S.isFull() << endl;
    return 0;
}