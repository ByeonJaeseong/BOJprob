import java.util.*;

public class Main {
			public static void main(String args[]){
			Scanner sc = new Scanner(System.in);
			int a,Max,Min;
				int b=1;
	     		int[] A =new int[9];
	            for(int i=0; i<=8; i++) {
	                A[i]=sc.nextInt();
	                }
	            Max = A[0];
	            Min = A[0];
	            for(int i=0; i<=8; i++) {
	            	if(Max<=A[i]) {
	            	Max=A[i];
	            	} else {
	            		Max= Max;
	            	}
	            }
	            int j = 0;
	            while(true) {
	            	int M = Max;
	            	int k = A[j];
	            	if(M==k) {
	            		break;
	            	}else {
	            		j++;
	            		b++;
	            	}
	            		            }	
	       
	        
	           System.out.println(Max);
	           System.out.println(b);

	            
	    }
}

