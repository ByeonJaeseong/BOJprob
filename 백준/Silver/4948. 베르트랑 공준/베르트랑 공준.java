import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while(true) {
			int n = Integer.parseInt(br.readLine());
			if(n==0) {
				break;
			}
			TreeSet<Integer> ts = new TreeSet<Integer>();
			TreeSet<Integer> ts2 = new TreeSet<Integer>();
			for(int i=n+1; i<=2*n; i++) {
				ts.add(i);
			}
			for(int i=2; i<=Math.sqrt(2*n)+1; i++) {
				ts2.add(i);
			}
			int a=ts2.pollFirst();
			int b=1;
			while(Math.sqrt(2*n)>=a) {
				int i=2;
				
				while(i*a<=2*n) {
					if(n<i*a) {
					ts.remove(i*a);}
					if(Math.sqrt(2*n)>=i*a) {
					ts2.remove(i*a);}
					i++;
				}
				
				
				if(ts2.isEmpty()) {
					break;
				}
				a=ts2.pollFirst();
				
				
			}
			ts.remove(1);
			System.out.println(ts.size());
		
		}

	}

}