import java.util.Scanner;

public class Main {
	

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long N = sc.nextLong();
		long n = N%1500000;
		int[] arr = new int[1500002];
		arr[0]=0;
		arr[1]=1;
		for(int i=2; i<1500002; i++) {
			arr[i]=(arr[i-1]+arr[i-2])%1000000;
			
//			if(arr[i]==1&&arr[i-1]==1&&i>3) {
//			System.out.println(i);
//			break;
//			}
		}
		
		System.out.println(arr[(int) n]);
	}

}
