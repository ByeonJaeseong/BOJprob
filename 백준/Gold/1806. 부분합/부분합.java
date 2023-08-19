import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    String[] input = str.trim().split(" ");
    int N = Integer.parseInt(input[0]);
    int S = Integer.parseInt(input[1]);
    int[] inputNo = new int[N];
    int[] sumArray = new int[N+1];
    str = br.readLine();
    input = str.trim().split(" ");
    for(int i=0; i<N; i++){
      inputNo[i]=Integer.parseInt(input[i]);
    }
    sumArray[0] = 0;
    for(int i=1; i<=N; i++){
      sumArray[i]=sumArray[i-1]+inputNo[i-1];
    }
    int min = 0;
    int start = 0;
    int end=1;
    while(start<N&&end<=N&&start<end){
      if((sumArray[end]-sumArray[start])>=S){
        if(min==0){
          min = end-start;
        }else{
          min = Math.min(min,end-start);
        }
        start++;
      }else{
        end++;
      }
      
    }
    System.out.println(min);
    
    
      
    
  }
}