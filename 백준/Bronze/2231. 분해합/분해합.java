import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N=sc.nextInt();
		int c=0;
		for(int i=0; i<N;i++) {
			int a=i;
			int b=i;
			for(int j=0; j<=10; j++) {
				a = a+ (b%10);
				b = b/10;
			}
			if(a==N) {
				System.out.println(i);
				break;
			}
			c++;
		}
		if(c==N && N!=2) {
		System.out.println(0);
		}
	}

}
