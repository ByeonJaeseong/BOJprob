import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] input = new int[N];
		int[] sumarr = new int[N];
		for(int i=0; i<N; i++) {
			input[i] = sc.nextInt();
			if(i==0) {
				sumarr[i] = input[i];
			}else {
				sumarr[i] = input[i]+sumarr[i-1];
			}
		}
		for(int i=0; i<M; i++) {
			int Q= sc.nextInt();
			int P= sc.nextInt();
			if(Q==1) {
				System.out.println(sumarr[P-1]);
			}else {
				System.out.println(sumarr[P-1]-sumarr[Q-2]);
			}

		}

	}

}
