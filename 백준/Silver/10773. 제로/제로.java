import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String str = bf.readLine();
		int N =Integer.parseInt(str);
		long a = 0;
		List<Long> list = new ArrayList<Long>();
		for(int i=0; i<N; i++) {
			long b = Integer.parseInt(bf.readLine());
			if(b!=0) {
				list.add(b);
			}else {
				int c = list.size();
				list.remove(c-1);
			}
		}
		for(int i=0; i<list.size(); i++) {
			a+=list.get(i);
		}
		System.out.print(a);

		
	}

}
