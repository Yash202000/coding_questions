#include<iostream>
#include <bits/stdc++.h>
using namespace std;

void nNoaccending(){
	int k;
	cout<<"Enter No of elements: ";
	cin>>k;
	int arr[k];
	cout<<"Enter three Nos: "<<endl;
	
	// int n = 4*k / 4
	int n = sizeof(arr) / sizeof(arr[0]);
	for(int i=0;i<k;i++) cin>>arr[i];
	
	//stdc++ sort() function
	sort(arr,arr+n);
	cout<<endl;
	cout<<"Sorted Nos are: ";
	for(int i=0;i<k;i++){
		cout<<arr[i]<<" ";
	}
		
}
int main(){
	nNoaccending();
	return 0;
}
