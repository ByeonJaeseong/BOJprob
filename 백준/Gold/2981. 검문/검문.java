import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		List<Integer> list = new ArrayList<Integer>();
		TreeSet<Integer> ts = new TreeSet<>();
		for(int i=0; i<N; i++) {
			list.add(Integer.parseInt(br.readLine()));
		}
		list.sort(null);//데이터 받음
		for(int i=1; i<N; i++) {
			ts.add(list.get(i)-list.get(i-1));
		}
		while(ts.size()!=1) {
			int a =ts.pollFirst();
			int b = ts.pollFirst();
			ts.add(gcd(a, b));
		}
		int a = ts.pollFirst();
		for(int i=2; i<=a; i++) {
			if(a%i==0) {
				System.out.print((i)+" ");
			}
		}
		

	}

	public static int gcd(int p, int q) {
		int r=Math.max(p, q);
		int s=Math.min(p, q);
		while(s!=0) {
			int y = s;
			s=r%s;
			r=y;
		}
		return r;
	}
}	

	

