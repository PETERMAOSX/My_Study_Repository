#include<iostream>
using namespace std;
struct node{
    int data;
    struct node * next;
};
int main(){
    struct node *head,*temp,*p,*q;
    int n,i,t;
    head = NULL;
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        scanf("%d",&t);
        p = (struct node *)malloc(sizeof(struct node));
        p->data = t;
        p->next = NULL;
        if(head == NULL){
            head = p;
        }
        else{
            q->next = p;
        }
        q = p;
    }
    temp = head;
    while(temp != NULL){
        printf("%d ",temp->data);
        temp = temp->next;
    }
    printf("\n");
    getchar();
    return 0;
}