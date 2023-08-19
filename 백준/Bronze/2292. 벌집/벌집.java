import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int N = sc.nextInt();
		if(N==1) {
			System.out.println(N);
		}else {
		for(int i=0; i<=N; i++)
			if(3*i*(i-1)+1< N && N<=3*i*(i+1)+1 ) {
				System.out.println(i+1);
				break;
			}
		}

	}
}
