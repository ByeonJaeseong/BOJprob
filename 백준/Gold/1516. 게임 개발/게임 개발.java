import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Unit{
	int n;
	boolean visit;
	int time;//고유 시간값
	int time2;//걸리는 총 시간
	int outcomeSize=0;
	List<Unit> income = new ArrayList<>();
	Unit(int n, int time){
		this.n = n;
		this.time = time;
		
	}
	Unit(int n){
		this.n = n;
	}
	public Unit() {
		// TODO Auto-generated constructor stub
	}
}

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] inputNo = str.trim().split(" ");
		int N = Integer.parseInt(str);
		Unit[] units = new Unit[N];
		for(int i=0; i<N; i++) {
			units[i] =new Unit(i);
		}
		for(int i=0; i<N; i++) {
			str = br.readLine();
			inputNo = str.trim().split(" ");
			int time = Integer.parseInt(inputNo[0]);
			units[i].time=time;
			units[i].time2=time;
			for(int j=1; j<inputNo.length-1; j++) {
				int unit = Integer.parseInt(inputNo[j]);
				units[i].outcomeSize++;//이것을 지어야 다음에 지울수 있는것
				units[unit-1].income.add(units[i]);//짓기 위해서 먼저 지어야하는것
				
			}
		}
		int[] arr = new int[N];
		
		for(int i=0; i<N; i++) {
			arr[i]=units[i].outcomeSize;
		}
		Queue<Unit> queue = new LinkedList<>();
		for(int i=0; i<N; i++) {
			if(arr[i]==0) {
				queue.add(units[i]);
				//System.out.println("실행되었습니다.");
			}
		}
		while(!queue.isEmpty()) {
			Unit qUnit = queue.poll();
			qUnit.visit=true;
			for(int i=0; i<qUnit.income.size(); i++) {
				
				qUnit.income.get(i).time2=
						Math.max(qUnit.income.get(i).time2, 
								qUnit.time2+qUnit.income.get(i).time);
				if(!queue.contains(qUnit.income.get(i)))
				queue.add(qUnit.income.get(i));
				arr[qUnit.income.get(i).n]--;
				if(!units[qUnit.income.get(i).n].visit&&arr[qUnit.income.get(i).n]==0) queue.add(units[i]);
				}
			
			
			
		}
		StringBuilder sb = new  StringBuilder();
		for(int i=0; i<N; i++) {
			sb.append((units[i].time2)+"\n");
		}
		System.out.print(sb);
		

	}

}