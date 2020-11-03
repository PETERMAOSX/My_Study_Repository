#include<iostream>
#include<string>
#include<vector>
#include<fstream>
using namespace std;
class Lecture{
public:
    string lecture_name;
    virtual string get_lecturename(int judge){
		return NULL;
	};
};
class Art : public Lecture{
public:
    string get_lecturename(int judge){
          if(judge == 0){
            return "音乐";
        }
        else if(judge == 1){
            return "设计";
        }
        else{
            return "编程";
        }
    }
    
};
class Sport : public Lecture{
public:
    string get_lecturename(int judge){
        if(judge == 0){
             return "拳击";
         }
         else{
             return "跆拳道";
         }
    }
};
class Student{
public:
    Student* next;
    Student(){
        this->next = NULL;
    }
    string name;
    int age;
    void show(){
        cout<<name<<endl<<age<<endl;
    }
};
class Node{
public:
    int value;
    Node* next;
    Node(int value){
        this->value = value;
        this->next = NULL;
    }
};
class NodeList{
public:
    Node* head;
    Node* tail;
    int count ;
    NodeList(){
        this->head = NULL;
        this->tail = NULL;
    }
    bool isEmpty(){
        return this->count == 0;
    }
    int getCount(){
        return this->count;
    }
    void addElementToTail(int value){
        if(this->tail != NULL){
            tail->next = new Node(value);
            tail = tail->next;
            count++;
        }
        else{
            head = tail = new Node(value);
            count++;
        }
    }
    void show(){
        Node* current = head;
        while(current != NULL){
            cout<<current->value<<endl;
            current = current->next;
        }
    }
    void delete_element(int value){
       Node* newNode;
       Node* temp;
       if(this->head->value == value){
           head = head->next;
       }
       else if(tail->value == value){
           newNode = head;
           while(newNode->next != tail) newNode = newNode->next;
           newNode->next = NULL;
           tail = newNode;
       }
       else{
           newNode = head;
           temp = NULL;
           while(newNode->value != value){
               temp = newNode;
               newNode = newNode->next;
           }
           temp->next = newNode->next;
       }
    }
};
int main(){
    Student stu1 = Student();
    Student stu2 = Student();
    Student stu3 = Student();
    stu1.name = "maoshaoxiong";
    stu1.age = 20;
    stu2.name = "Raymound";
    stu2.age = 21;
    stu3.name = "Peter";
    stu3.age = 22;
    vector<Student> svec;
    vector<Student>::iterator it;
    svec.push_back(stu1);
    svec.push_back(stu2);
    svec.push_back(stu3);
    //svec.erase(remove(svec.begin(),svec.end(),stu2),svec.end());
    for(it = svec.begin();it!=svec.end();){
        if(it->name == "Raymound"){
            it = svec.erase(it);
        }
        else{
            ++it;
        }
    }
    for(int i=0;i<svec.size();i++){
        cout<<svec[i].name<<endl;
    }
    ofstream write;
    write.open("data.txt");
    for(int i=0;i<svec.size();i++){
        write<<svec[i].name<<endl;
    }
    write.close();
	// vector<string> vec;
    // for(int i=0;i<svec.size();i++){
    //     svec[i].show();
    // }
    // vec.push_back("aaa");
    // vec.push_back("bbb");
    // vec.push_back("ccc");
    // vec.erase(remove(vec.begin(),vec.end(),"aaa"),vec.end());
    // for(int i=0;i<vec.size();i++){
    //     cout<<vec[i]<<endl;
    // }
    // NodeList list = NodeList();
    // list.addElementToTail(1);
    // list.addElementToTail(2);
    // list.addElementToTail(3);
    // list.addElementToTail(4);
    // list.addElementToTail(5);
    // list.addElementToTail(6);
    // list.addElementToTail(7);
    // list.addElementToTail(8);
    // list.delete_element(4);
    // list.show();
	return 0;
}
