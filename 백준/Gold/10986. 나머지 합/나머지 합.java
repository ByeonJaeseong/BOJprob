import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] inputNo = br.readLine().trim().split(" ");
		
		int M = Integer.parseInt(inputNo[0]);
		int N = Integer.parseInt(inputNo[1]);
		
		long[] arr = new long[M];
		long[] sumarr = new long[M];
		long[] number = new long[N];
		
		inputNo = br.readLine().trim().split(" ");
		
		for(int i=0; i<M; i++) {
			arr[i]=Long.parseLong(inputNo[i]);
			if(i==0) {
				sumarr[i] = (long)arr[i]%N;
			}else {
				sumarr[i]= (long)(arr[i]+sumarr[i-1])%N;
			}
			number[(int) sumarr[i]]++;
			
		}
		
		/*
		 * for(int i=0; i<N; i++) { System.out.print(number[i]);
		 * 
		 * }
		 */
		
		long count = 0;
		
		for(int i=0; i<N; i++) {
			if(i==0) {
				count =(long) count + (number[i]*(number[i]+1))/2;
			} else {
				count =(long) count + (number[i]*(number[i]-1))/2;
				
			}
				
			
		}
		System.out.println(count);
		
	}

}
