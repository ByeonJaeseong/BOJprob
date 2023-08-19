import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int fibo= sc.nextInt();
		int[] fibonachhi = {0 , 1};
		for(int i=0; i<fibo/2; i++) {
			fibonachhi[0] = fibonachhi[0] + fibonachhi[1];
			fibonachhi[1] = fibonachhi[0] + fibonachhi[1];
		}
		if(fibo%2==0) {
			System.out.println(fibonachhi[0]);
		}else {
			System.out.println(fibonachhi[1]);
		}
						
	}
}
