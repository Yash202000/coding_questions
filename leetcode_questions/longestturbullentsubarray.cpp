class Solution {
public:
    int maxTurbulenceSize(vector<int>& A) {
         int n = A.size();
      int prevBig = 1;
      int prevSmall = 1;
      int currBig = 1;
      int currSmall = 1;
      int ret = 1;
      for(int i = 1; i < n; i++){
         if(A[i] > A[i - 1]){
            currBig = 1 + prevSmall;
         }
         if(A[i] < A[i - 1]){
            currSmall = 1 + prevBig;
         }
         ret = max({ret, currBig, currSmall});
         prevSmall = currSmall;
         prevBig = currBig;
         currSmall = 1;
         currBig = 1;
      }
      return ret;
        
    }
};