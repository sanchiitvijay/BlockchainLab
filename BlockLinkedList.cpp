#include <iostream>
using namespace std;

struct Node {
    string block;
    string nonce;
    string data;
    string timestamp;
    Node* prev;
    string hash;
};

class block {
    Node* head;

public:
    block() : head(NULL) {}
    
    void block_insert(string block, string nonce, string data, string hash, string timestamp) {
        Node* newNode = new Node(); 
        newNode->data = data;
        newNode->prev = NULL;
        newNode->block = block;
        newNode->hash = hash;
        newNode->nonce = nonce;
        newNode->timestamp = timestamp;

        if (!head) {
            head = newNode;
            return;
        }

        Node* temp = head;
        while (temp->prev) {
            temp = temp->prev;
        }

        temp->prev = newNode;
    }


    void block_delete() {
        if (!head) {
            cout << "List is empty." << endl;
            return;
        }

        if (!head->prev) {
            delete head;   
            head = NULL;   
            return;
        }

        Node* temp = head;
        while (temp->prev->prev) {
            temp = temp->prev;
        }
        
        delete temp->prev; 
        temp->prev = NULL; 
    }

    void display() {
        if (!head) {
            cout << "List is empty." << endl;
            return;
        }

        Node* temp = head;
        while (temp) {
            cout<<"("<<temp->block<<","<<temp->nonce<<","<<temp->timestamp<<","<<temp->data<<","<<temp->prev<<","<<temp->hash<<")"<< " -> "; 
            temp = temp->prev;
        }
        cout << "END" << endl; 
    }
};

int main() {
    // string block;
    // string nonce;
    // string timespamp;
    // string data;
    // Node* prev;
    // string hash;
    block b1;

    b1.block_insert("block1", "nounce1", "data1", "hash1", "time1");
    b1.block_insert("block2", "nounce2", "data2", "hash2", "time2");
    b1.block_insert("block3", "nounce3", "data3", "hash3", "time3");
    
    b1.display();
    cout<<"Deleting the last one\n";
    b1.block_delete();
    b1.display();

    return 0;
}
