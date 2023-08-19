import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int n =sc.nextInt();
		int[] test = new int[n];
		for(int i=0; i<n; i++) {
			test[i]=sc.nextInt();
		}
		long[] arr = new long[101];
		arr[0]=1;
		arr[1]=1;
		arr[2]=1;
		arr[3]=1;
		arr[4]=2;
		arr[5]=2;
		for(int i=6; i<101; i++) {
			arr[i]=arr[i-5]+arr[i-1];
		}
		
		for(int i = 0; i<n; i++) {
			System.out.println(arr[test[i]]);
		}
		




	}

}
