#include<bits/stdc++.h>
using namespace std;

void display(int *arr,int n){
    for(int i =0; i<n;i++)
    cout<<arr[i]<<" ";
    cout<<endl;
}
void display(string &s,int n){
    for(int i =0; i<n;i++)cout<<s[i];
    cout<<endl;
}
int main(){
    int t;
    cin>>t;
    while(t--){
    int n,k;
    cin>>n>>k;
   // int *arr = new int[n];
   string s;
   cin>>s;

    //for(int i =0; i<n;i++) cin>>arr[i];

    int *num = new int[n];
    for(int i =0; i <n;i++) num[i] =-2;

   /* for(int i =0; i<n;i++) num[i]=-1;

    // k =0;
    int lowzero = -1;
    for(int i =n-1; i>=0;i--){
        if(s[i]=='0') {
            lowzero = i;
            num[i] = lowzero;
    
        }
        else{
            num[i] = lowzero;

        }
    }
    */
   /*cout<<"GIVEN STRING IS \n";
   display(s,n);
   */

    for(int i =0;i<n;i++){
       if(s[i]=='1'){
        //bool ff = false;
        num[i] =0;
        if(i-1!=-1)
        {
            if(s[i-1]=='0') num[i-1] = 0;
            else if(num[i-1]==-2) {
                num[i-1] =-1;
                // if(ff==false)
                // num[i] =-1;
            }
            
            
        }
        if(i+1!=n){
            if(s[i+1]=='0') num[i+1] = 0;
            else if(num[i+1]==-2) {
                num[i+1] = -1;
                // if(ff==false)
                // num[i] =-1;
        }

       }
       }

       else if(num[i]!=-2) continue;
       else 
       num[i] = -1;

    }

    display(num,n);
    //return 0;
    
   /* cout<<"THIS IS NUM ARRAY FOR ALL 0 FLIP \n";
    display(num,n);
    */

    
    int *z = new int[n];
    int lowzero = -1;
    for(int i =n-1; i>=0;i--){
        if(num[i]==0) {
            lowzero = i;
            z[i] = lowzero;
    
        }
        else{
            z[i] = lowzero;

        }
    }
    display(z,n);
    lowzero =-1;
    int r = -1;
    for(int i =0 ;i<n;i++){
        if(num[i]==0){
            lowzero = i;
            if(z[i]==-1 && lowzero==-1) {
                cout<<s<<endl;
               
               r=0;
                break;
            }
            else if(z[i]!=-1 && lowzero!=-1){
                num[i] = min(abs(lowzero-i),abs(z[i]-i));
            }
            else if(z[i]==-1 &&lowzero!=-1)
            num[i] = abs(lowzero-i);
            else 
            num[i] = abs(z[i]-i);


        }
        else{
            if(z[i]==-1 && lowzero==-1) {
                cout<<s<<endl;
                r=0;
                break;
            }
            else if(z[i]!=-1 && lowzero!=-1){
                num[i] = min(abs(lowzero-i),abs(z[i]-i));
            }
            else if(z[i]==-1 &&lowzero!=-1)
            num[i] = abs(lowzero-i);
            else 
            num[i] = abs(z[i]-i);

        }

    }
    display(num,n);
    if(r!=0){
   /* cout<<"ALL VALID 0's INDEX FROM RIGHT SIDE \n";

    display(z,n);

    cout<<"FINAL NUM ARRAY \n";
    display(num,n);
    */
   for(int i =0;i<n;i++){
     if((k-num[i])%2==0) cout<<s[i];
     else{
        if(s[i]=='1')cout<<"0";
        else
        cout<<"1";
     }
   }
   cout<<endl;
    }

}
   




}