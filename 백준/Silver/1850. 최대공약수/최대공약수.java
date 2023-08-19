import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long N = sc.nextLong();
		long M = sc.nextLong();
		long p = Math.max(N, M);
		long q = Math.min(M, N);
		while(p%q!=0){
			Long x=q;
			q=p%q;
			p=x;				
		}
		StringBuilder sb =new StringBuilder();
		for(int i=0; i<q; i++) sb.append(1);
		System.out.print(sb);

	}

}
