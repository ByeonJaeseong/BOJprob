import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;

class City{
	int n=0;
	boolean visit;
	int max;
	List<City> outcome = new ArrayList<>();
	List<City> income = new ArrayList<>();	
	Set<String> set = new HashSet<>();
	public City() {
		// TODO Auto-generated constructor stub
	}
	public City(int n) {
		this.n = n;
	}
}


public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		int[][] times = new int[N][N];
		String str;
		String[] inputNo;
		City[] cities = new City[N];
		for(int i=0; i<N; i++) {
			cities[i]= new City(i);
		}
		for(int i=0; i<M; i++) {
			str=br.readLine();
			inputNo= str.trim().split(" ");
			int p = Integer.parseInt(inputNo[0])-1;
			int q = Integer.parseInt(inputNo[1])-1;
			int r = Integer.parseInt(inputNo[2]);
			times[p][q] = r;
			cities[p].outcome.add(cities[q]);
			cities[q].income.add(cities[p]);
		}
		str=br.readLine();
		inputNo = str.trim().split(" ");
		int start = Integer.parseInt(inputNo[0])-1;
		int end = Integer.parseInt(inputNo[1])-1;
		br.close();
		int[] incomeNo = new int[N];
		for(int i=0; i<N; i++) {
			incomeNo[i] = cities[i].income.size();
		}
		Queue<City> queue = new LinkedList<>();
		int[] min = new int[N];
		for(int i=0; i<N; i++) {
			min[i]=Integer.MAX_VALUE;
		}
		int[] max = new int[N];
		queue.add(cities[start]);
		cities[start].visit=true;

		while(!queue.isEmpty()) {
			City city = queue.poll();

			if(city.n==end) break;

			for(int i=0; i<city.outcome.size(); i++) {
				City out = city.outcome.get(i);
				incomeNo[out.n]--;
				max[out.n]=Math.max(max[out.n], max[city.n]+times[city.n][out.n]);
				out.max=max[out.n];
			}

			for(int i=0; i<N; i++) {
				if(!cities[i].visit&&incomeNo[i]==0) {
					cities[i].visit=true;
					queue.add(cities[i]);
				}
			}
		}
		queue.clear();
		for(int i=0; i<N; i++) {
			cities[i].visit=false;
		}
		
		queue.add(cities[end]);
		cities[end].visit=true;
		Set<String> set = new HashSet<>();
		while(!queue.isEmpty()) {
			City city=queue.poll();
			//System.out.println(city.income.size());
			//if(city.n==start) break;
			for(int i=0; i<city.income.size(); i++) {
				City out = city.income.get(i);
				if(out.max==city.max-times[out.n][city.n]) {
					set.add((out.n)+""+city.n);	
					if(!out.visit) {
					out.visit=true;
					queue.add(out);}
				}
			}
		}

		System.out.println((max[end]));

		System.out.print(set.size());

	}

}
