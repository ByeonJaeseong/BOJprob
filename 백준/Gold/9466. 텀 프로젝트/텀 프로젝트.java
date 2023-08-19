import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

class pStudent{
	int no;
	boolean visit;
	public pStudent() {
	
		// TODO Auto-generated constructor stub
	}
	public pStudent(int no) {
		this.no=no;
	}
	List<pStudent> outcome = new ArrayList<>();
}

public class Main{
	public static Set<pStudent> set;
	public static Set<pStudent> stSet;
	public static void bfs(pStudent st, int n) {
		st.visit=true;
		stSet.add(st);
		
		for(pStudent s : st.outcome) {
			if(s.no==n) {
				set.addAll(stSet);
			}else if(s.no!=n&&!s.visit) {
			bfs(s, n);
			}
		}
		stSet.remove(st);
		
		
		
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int x=0; x<T; x++) {
			int N = Integer.parseInt(br.readLine());
			pStudent[] students = new pStudent[N];
			for(int i=0; i<N; i++) {
				students[i] = new pStudent(i);
			}
			String[] inputNo = br.readLine().trim().split(" ");
			for(int i=0; i<N; i++) {
				int p = Integer.parseInt(inputNo[i])-1;
				students[p].outcome.add(students[i]);
				//나가는 사이클
			}
			set = new HashSet<>();
			for(int i=0; i<N; i++) {
				if(!students[i].visit) {
				stSet=new HashSet<>();
				bfs(students[i], i);
				}
			}
//			stSet = new HashSet<pStudent>();
//			bfs(students[5], 5);
//			Iterator<pStudent> itr = set.iterator();
//			while(itr.hasNext()) {
//				System.out.println(itr.next().no);
//			}
			System.out.println(N-set.size());
		}

	}

}