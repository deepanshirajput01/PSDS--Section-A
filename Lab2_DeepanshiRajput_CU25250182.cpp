//ENQUEUE and DEQUEUE
#include <iostream>
using namespace std;

int main() {
    int queue[100];
    int front = 0;
    int rear = -1;

    // ENQUEUE
    queue[++rear] = 10;
    queue[++rear] = 20;
    queue[++rear] = 30;

    cout << "Queue after ENQUEUE:" << endl;

    for (int i = front; i <= rear; i++) {
        cout << queue[i] << " ";
    }

    cout << endl;

    // DEQUEUE
    while (front <= rear) {
        cout << "Dequeued: " << queue[front] << endl;
        front++;
    }

    return 0;
}