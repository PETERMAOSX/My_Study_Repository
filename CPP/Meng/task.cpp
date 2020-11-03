#include<iostream>
#include<string>
#include<vector>  //容器
#include<fstream>
using namespace std;

class Student{
public:
    int age;
    string name;
    string sex;
    vector<string> lectures;
    string lectures_list;
public:
    Student(){
        
    }
    ~Student(){

    }
    void input(){
        cout<<"请输入姓名: ";
        string name;
        cin>>name;
        this->name = name;
        cout<<endl;
        cout<<"请输入性别: ";
        string sex;
        cin>>sex;
        this->sex = sex;
        cout<<endl;
        cout<<"请输入年龄: ";
        int age;
        cin>>age;
        this->age = age;
    }
    void show(){
        cout<<"名字是: "<<this->name<<endl;
        cout<<"性别是: "<<this->sex<<endl;
        cout<<"年龄是: "<<this->age<<endl;
    }
    void add_lecture(string lecture_name){
        this->lectures.push_back(lecture_name);
        
    }
    void show_lecture(){
        for(int i=0;i<this->lectures.size();i++){
            cout<<this->lectures[i]<<endl;
        }
    }
    void addLectureName(){
        for(int i=0;i<this->lectures.size();i++){
            this->lectures_list += this->lectures[i]+" ";
        }
    }
    void delete_lecture(string value){
        //this->lectures.erase(remove(this->lectures.begin(),this->lectures.end(),value),this->lectures.end());
        vector<string> :: iterator it;
        for(it = this->lectures.begin();it != this->lectures.end();){
            if(*it == value){
                it = this->lectures.erase(it);
            }
            else{
                ++it;
            }
        }
    }
};
vector<Student> students; //学生总名单
class Lecture{  
public:
    string lecture_name;
    //虚函数
    virtual string get_lecturename(int judge){
        return NULL;
    };
};
class Art : public Lecture{  //文艺类
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
class Sport : public Lecture{  //体育类
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
void add_student(){  //添加学生
    Student stu = Student();
    Lecture* lecture_Type;
    Art art = Art();
    Sport sport = Sport();
    stu.input();
    while(1){
    cout<<"请选择学生想要学习的类型"<<endl;
    cout<<"0、体育类"<<endl<<"1、文艺类"<<endl;
    int chose;
    cin>>chose;
    if(chose == 0){
        lecture_Type = &sport;
        cout<<"0、拳击"<<endl<<"1、跆拳道"<<endl;
    }
    else{
        lecture_Type = &art;
        cout<<"0、音乐"<<endl<<"1、设计"<<endl<<"2、编程"<<endl;
    }
    int chose_lec;
    cin>>chose_lec;
    string lecture_name = lecture_Type->get_lecturename(chose_lec);
    stu.add_lecture(lecture_name);
    cout<<"是否添加课程? y/n";
    char chose_continue;
    cin>>chose_continue;
    if(chose_continue == 'n'){
        students.push_back(stu);
        break;
    }
    }

}
void delete_student(){  //删除某个学生
    cout<<"请输入需要删除的学生姓名:"<<endl;
    string name;
    cin>>name;
    vector<Student>::iterator it;
    bool is_find = false;
    for(it = students.begin();it!=students.end();){
        if(it->name == name){
            it = students.erase(it);
            is_find = true;
        }
        else{
            ++it;
        }
    }
    if(is_find == true){
        cout<<"已经成功删除 "<<name<<" 同学的信息。"<<endl;
    }
    else{
        cout<<"没有找到，请重新确认输入是否有误"<<endl;
    }
}
void recompose_student(){ //修改学生信息
    cout<<"请输入想要修改的学生姓名"<<endl;
    bool is_find = false;
    Student* FindStu = NULL;
    string name;
    cin>>name;
    for(int i=0;i<students.size();i++){
        if(students[i].name == name){
            is_find = true;
            FindStu = &students[i];
        }
    }
    if(FindStu == NULL){
        cout<<"没有找到该学生，请确认输入是否有误。"<<endl;
    }
    else{
        cout<<"查找的学生是"<<FindStu->name<<"同学."<<endl;
        cout<<"该学生的补课内容是:"<<endl;
        FindStu->show_lecture();
        cout<<"请输入想要删除的课程名字。"<<endl;
        string name_lecture;
        cin>>name_lecture;
        vector<string>:: iterator it;
        it = find(FindStu->lectures.begin(),FindStu->lectures.end(),name_lecture);
        bool is_Consist = false;
        if(it != FindStu->lectures.end()){
            is_Consist = true;
        }
        else{
            is_Consist = false;
        }
        if(is_Consist == true){
            FindStu->delete_lecture(name_lecture);
            cout<<name_lecture<<"课程已经删除成功!"<<endl;
        }
        else{
            cout<<"没有找到该课程，请重新操作!"<<endl;
        }
    }
}
void see_student(){   //查询特定学生
    cout<<"您想要查询哪个学生? 请输入姓名:"<<endl;;
    string name;
    cin>>name;
    bool isFind = false;
    for(int i=0;i<students.size();i++){
        if(students[i].name == name){
            cout<<name<<"的基本信息如下:"<<endl;
            students[i].show();
            students[i].show_lecture();
            isFind = true;
            break;
        }
        
    }
    if(isFind == true){}
    else{
        cout<<name<<"没有找到！请确认输入是否有误！"<<endl;
    }
    
}
void show_nameList(){   //展示已报名的学生列表
    int count = 0;
    for(int i = 0;i<students.size();i++){
        cout<<++count<<"-"<<students[i].name<<endl;
    }
}
void save(){  //保存信息到本地文件
    int count = 0;
    fstream write;
    ofstream outfile("data.txt");
    write.open("data.txt");
    for(int i=0;i<students.size();i++){
        students[i].addLectureName();
        write<<++count<<" "<<students[i].name<<" "<<students[i].sex<<" "<<students[i].age<<" | "<<students[i].lectures_list<<endl;
        students[i].lectures_list = "";
    }
    write.close();
}

int main(){
    //主菜单
    cout<<"欢迎使用梦泽补习班 信息管理系统"<<endl;
    while(1){
        cout<<"1、添加学生"<<endl;
        cout<<"2、删除学生"<<endl;
        cout<<"3、修改学生"<<endl;
        cout<<"4、查询学生"<<endl;
        cout<<"5、列出现有的学生名单"<<endl;
        cout<<"6、将信息输出到一个txt文件中"<<endl;
        cout<<"9、退出程序"<<endl;
        int input;
        cin>>input;
        if(input == 9){
            break;
        }
        else if(input == 1){
            add_student();
        }
        else if(input == 2){
            delete_student();
        }
        else if(input == 3){
            recompose_student();
        }
        else if(input == 4){
            see_student();
        }
        else if(input == 5){
            show_nameList();
        }
        else if(input == 6){
            save();
        }
        else{
            break;
        }
    }
}