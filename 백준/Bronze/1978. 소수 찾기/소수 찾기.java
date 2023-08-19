import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		int[] primeArray = new int[T];
		for(int i=0; i< primeArray.length; i++) {
			primeArray[i]=sc.nextInt();
		}
		int a = 0;
		for(int x : primeArray) {
			int b=0;
			for(int j=1; j<=x; j++) {
				if(x%j==0) {
					b++;
				}
			}
			if(b==2) {
				a++;
			}
		}
			System.out.println(a);

	}

}
