import java.util.*;

public class Test {
    static long sum(int[] a) {
        long ans = 0;
        for (int i:a){
            ans += i;
        }
        return ans;
    }

public static void main(String[] args){
    Scanner sc= new Scanner(System.in);
    int n = sc.nextInt();
    int[] ar= new int[n] ;
        for(int j=0; j<n; j++){
            ar[j]=sc.nextInt();
        }
    System.out.println(sum(ar));
        
}
}