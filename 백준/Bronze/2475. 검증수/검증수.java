import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = 0;
		for(int i=0; i<5; i++) {
			int b = sc.nextInt();
			a += b*b;
		}
		System.out.println(a%10);

	}

}
