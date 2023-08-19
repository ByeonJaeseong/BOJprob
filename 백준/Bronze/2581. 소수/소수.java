import java.util.Scanner;

public class Main {

		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			int M = sc.nextInt();
			int N = sc.nextInt();
			int[] primeArray = new int[N-M+1];
			for(int i=0; i< primeArray.length; i++) {
				primeArray[i]=M+i;
			}
			int sum = 0;
			for(int x : primeArray) {
				int b=0;
				for(int j=1; j<=x; j++) {
					if(x%j==0) {
						b++;
					}
				}
				if(b==2) {
					sum += x;
				}
			}
			if(sum !=0) {
				System.out.println(sum);
			}	
				int sum1 = 0;
				minPrime :for(int x : primeArray) {
					int b=0;
					for(int j=1; j<=x; j++) {
						if(x%j==0) {
							b++;
						}
					}
					if(b==2) {
						sum1 += x;
						break minPrime;
					}
				}
				if(sum1 == 0) {
					System.out.println(-1);
				}else {
					System.out.println(sum1);	
				}
				

	}
}

