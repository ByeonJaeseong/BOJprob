import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] arr = new int[N];
		for(int i=0; i<N;i++) {
			arr[i]=sc.nextInt();
		}
		int sum=0;
		int number=0;
		int i=N-1;
		while(M!=sum) {
			if((M-sum)-arr[i]>=0) {
				sum += arr[i];
				number++;
			}else {
				i--;
			}
		}
	
		System.out.println(number);

	}

}