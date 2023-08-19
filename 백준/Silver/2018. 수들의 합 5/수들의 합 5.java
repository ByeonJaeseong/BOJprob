import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		List<Integer> dividor = new ArrayList<Integer>();
		double a = Math.sqrt(2*N);
		int b = (int) a;
		int c;
		int ans =0;
		if((a-b)==0) {
			c = b;
		}else {
			c = b+1;
		}
		for(int i = c; i<=2*N; i++) {
			if(2*N%i==0) {
				dividor.add(i);
			}
			
		}
		
		for(int i = 0; i<dividor.size(); i++) {
			
			double p = (double) (dividor.get(i)+2*N/dividor.get(i)-1)/2;
			
			int q = (int) p;
			if((q-p)==0) {
				ans++;
			}
		
		}
		System.out.println(ans);
	}

}