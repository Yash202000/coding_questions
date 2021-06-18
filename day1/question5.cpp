#include <iostream>
using namespace std;

int getNthFib(int n){
	if(n==0) return 0;
	else if(n==1) return 1;
	else return (getNthFib(n-1)+getNthFib(n-2));
}

int main(){
	cout<<"Enter no: ";
	int n;
	cin>>n;
	cout<<getNthFib(n-1);
	return 0;
}
