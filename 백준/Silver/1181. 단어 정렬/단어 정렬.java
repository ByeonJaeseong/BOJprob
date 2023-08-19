import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		TreeSet<String> treeset= new TreeSet<String>();
		List<String> list = new ArrayList();
		for(int i=0; i<N;i++) {
			treeset.add(sc.next());
		}
		
		while(!treeset.isEmpty()) {
			list.add(treeset.pollFirst());
		}
		int i=1;
		int k=0;
		while(k!=list.size()) {
			
			for(int j=0; j<list.size();j++) {
			if(list.get(j).length() == i) {
				System.out.println(list.get(j));
				
				k++;
			}
			}
			i++;
		}

	}
}
