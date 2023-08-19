import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str =br.readLine();
    String[] inputNo = str.trim().split(" ");
    int N = Integer.parseInt(inputNo[0]); // 숫자개수
    int M = Integer.parseInt(inputNo[1]); // 숫자변경횟수
    int L = Integer.parseInt(inputNo[2]); // 구간의 곱을 구하는 횟수
    
    int n = 1;
    while(n<N){
      n*=2;
    }
    long[] arr = new long[2*n];
    for(int i=0; i<N; i++){
      arr[i+n]=Long.parseLong(br.readLine());
    }

    for(int i=n-1; i>0; i--){
      arr[i] = (long) arr[2*i]*arr[2*i+1] %1000000007;
    }
    // for(int i=0; i<2*n; i++)
    // System.out.println(arr[i]);
  int count = 0;
   while(count<M){
     int p;
     int q;
     long r;
    
     while(true){
       str = br.readLine();
       inputNo = str.trim().split(" ");
       p = Integer.parseInt(inputNo[0]);
       q = Integer.parseInt(inputNo[1])+n-1;
       r = Long.parseLong(inputNo[2]);
       if(p==1){
       
       arr[q] = r;
       
       while(q>0){
         if((q%2)==1){
           arr[q/2]=(long) arr[q]*arr[q-1]%1000000007;
           
         }else{
           arr[q/2]=(long) arr[q]*arr[q+1]%1000000007;
         }
         q=q/2;
       }
       }else{
         break;
       } 

       
     }
     
      long result = 1;
      int start = q;
      int end = (int)r+n-1;
      while(end>=start){
        if(start%2==1){
          result =(long) (result*arr[start])%1000000007;
        }
        start = (start+1)/2;
        
        if(end%2==0){
          result = (long) result*arr[end]%1000000007;
        }
        end = (end-1)/2;
        
      }
      System.out.println(result);
     count++;

    }
    }
}