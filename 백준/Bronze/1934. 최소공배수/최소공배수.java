import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		for(int x=0; x<N; x++) {
			int p = sc.nextInt();
			int q = sc.nextInt();
			int r=Math.max(p, q);
			int s=Math.min(p, q);
			while(s!=0) {
				int y = s;
				s=r%s;
				r=y;
			}
			System.out.println(p*q/r);
			
		}
	}

}