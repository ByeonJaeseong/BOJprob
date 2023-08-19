import java.util.*;
public class Main{
		public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int a,Max,Min;
		a = sc.nextInt();
     		int[] A =new int[a];
            for(int i=0; i<=a-1; i++) {
                A[i]=sc.nextInt();
                }
            Max = A[0];
            Min = A[0];
            for(int i=0; i<=a-1; i++) {
            	if(Max<=A[i]) {
            	Max=A[i];
            	} else {
            		Max= Max;
            	}
            }
            	for(int j=0; j<=a-1; j++) {
                	if(A[j]<=Min) {
                	Min=A[j];
                	} else {
                		Min= Min;
                	}            	
            	
            }
           System.out.print(Min);
           System.out.print(' ');
           System.out.print(Max);
            
    }
}