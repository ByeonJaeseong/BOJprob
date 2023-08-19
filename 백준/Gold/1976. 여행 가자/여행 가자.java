import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.Stack;

class City{
	int value;
	boolean visit=false;
	City(){}
	City(int value){
		
	}
	List<City> adj = new ArrayList<>();
}

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		int N = Integer.parseInt(str);
		str=br.readLine();
		int M = Integer.parseInt(str);
		City[] cities = new City[N];
		for(int i=0; i<N; i++) {
			cities[i]=new City(i);
		}
		String[] adjCity = str.trim().split(" ");
		for(int i=0; i<adjCity.length; i++) {
			str=br.readLine();
			adjCity = str.trim().split(" ");
			for(int j=0; j<N; j++) {
				if(adjCity[j].equals("1")) {
					cities[i].adj.add(cities[j]);
				}
				
			}			
		}
		str = br.readLine();
		adjCity=str.trim().split(" ");
		Set<City> set = new HashSet<>();
		Set<City> set2 = new HashSet<>();
		for(int i=0; i<M; i++) {
			int p =Integer.parseInt(adjCity[i]);
			set.add(cities[p-1]);
		}
		Stack<City> stack = new Stack<>();
		stack.add(cities[Integer.parseInt(adjCity[0])-1]);
		while(!stack.isEmpty()) {
			City vCity = stack.pop();
			set2.add(vCity);
			vCity.visit=true;
			//System.out.println(vCity.adj.size());
			for(int i=0; i<vCity.adj.size(); i++) {
				if(!vCity.adj.get(i).visit) {
					stack.add(vCity.adj.get(i));
					vCity.adj.get(i).visit=true;
				}
			}
			//System.out.println(stack.size());
			
		}
	//	System.out.println(set.size());
	//	System.out.println(set2.size());
		if(set2.containsAll(set)) {
			System.out.println("YES");
		}else {
			System.out.println("NO");
		}

	}

}