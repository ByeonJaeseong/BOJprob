
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		long[] arr = new long[N];
		if(N>1) {
		arr[0]=1;
		arr[1]=2;}
		else {
			arr[0]=1;
			
		}
		for(int i=2; i<N; i++) {
			arr[i]= (long)(arr[i-1]%10007)+ (arr[i-2]%10007);
		}
		
		System.out.println(arr[N-1]%10007);
		

	}
	
}
