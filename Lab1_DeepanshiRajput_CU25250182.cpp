//PUSH and POP

#include <iostream>
using namespace std;

int main() {
    int stack[100];
    int top = -1;

    // PUSH
    stack[++top] = 10;
    stack[++top] = 20;
    stack[++top] = 30;

    cout << "Stack after PUSH:" << endl;
    for (int i = 0; i <= top; i++) {
        cout << stack[i] << " ";
    }

    cout << endl;

    // POP
    while (top >= 0) {
        cout << "Popped: " << stack[top] << endl;
        top--;
    }

    return 0;
}

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