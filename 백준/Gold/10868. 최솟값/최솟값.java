import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str =br.readLine();
    String[] inputNo = str.trim().split(" ");
    int N = Integer.parseInt(inputNo[0]); // 숫자개수
    int M = Integer.parseInt(inputNo[1]); // 순서쌍개수
    int n = 1;
    while(n<N){
      n*=2;
    }
    int[] arr = new int[2*n];
    for(int i=0; i<N; i++){
      arr[i+n]=Integer.parseInt(br.readLine());
    }

    for(int i=n-1; i>0; i--){
      arr[i] = Math.min(arr[2*i], arr[2*i+1]);
    }
    // for(int i=0; i<2*n; i++)
    // System.out.println(arr[i]);

   for(int i=0; i<M; i++){
      int result = Integer.MAX_VALUE;
      str = br.readLine();
      inputNo = str.trim().split(" ");
      int start = Integer.parseInt(inputNo[0])+n-1;
      int end = Integer.parseInt(inputNo[1])+n-1;
      while(end>=start){
        if(start%2==1){
          result = Math.min(result,arr[start]);
        }
        start = (start+1)/2;
        
        if(end%2==0){
          result = Math.min(result, arr[end]);
        }
        end = (end-1)/2;
        
      }
      System.out.println(result);

    }
  
    }
}