import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

public class Main {
	public static int[] arr;
	public static List<Integer> warning = new ArrayList<Integer>();
	public static int find(int n) {
		int a = arr[n];
		int b = n;
		while(a!=b) {
			b=a;
			a=arr[a];
			
		}
		return a;
		
	}
	
	public static void union(int a, int b) {
		int c = Math.max(a, b);
		int d = Math.min(a, b);
		int e = arr[c];
		int f = find(d);
		
		for(int i=0; i<arr.length; i++) {
			if(arr[i]==e) {
				arr[i]=f;
			}
			
		}
		//System.out.println(find(d));
	}
	
	public static void finder(int n) {
		for(int i=0; i<arr.length; i++) {
			if(arr[i]==n) {
				warning.add(i);
	//			System.out.println((i)+"가 추가되었습니다.");
				if(arr[i]!=i) {
					finder(i);
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] inputNo = str.trim().split(" ");
		int N = Integer.parseInt(inputNo[0]);//사람수
		int M = Integer.parseInt(inputNo[1]);//파티수
		arr= new int[N];
		for(int i=0; i<N; i++) {
			arr[i]=i;
		}
		str = br.readLine();
		inputNo = str.trim().split(" ");
		int people = Integer.parseInt(inputNo[0]);
		List<Integer> truth = new ArrayList<>();
			for(int i=1; i<inputNo.length; i++) {
			truth.add(Integer.parseInt(inputNo[i])-1);
//			System.out.println((truth.get(i-1))+"는 진실을 알고 있습니다.");
			//초기에 진실을 알고 있는 사람들
		}
		List<HashSet<Integer>> party = new ArrayList<HashSet<Integer>>();
		
	
		for(int i=0; i<M; i++) {
			party.add(new HashSet<>());
			str = br.readLine();
			inputNo = str.trim().split(" ");
			int a = Integer.parseInt(inputNo[0]);
			//System.out.println(a);
			
			for(int j=1; j<inputNo.length; j++) {
				party.get(i).add(Integer.parseInt(inputNo[j])-1);
			}
			
			for(int j=1; j<inputNo.length-1; j++) {
				if(j!=inputNo.length-1) {
				union(Integer.parseInt(inputNo[j])-1, Integer.parseInt(inputNo[j+1])-1);}
				else {
					union(Integer.parseInt(inputNo[j])-1, Integer.parseInt(inputNo[1]));
				}
			}
	//		System.out.println((i)+"번째 파티 참석자 수"+(party.get(i).size()));
			
		}
		//System.out.println("\n진실을 알고 있는 사람 수"+(truth.size()));
		for(int i=0; i<truth.size(); i++) {
			//System.out.println((truth.get(i))+"의 탐색이 실행되었습니다.");
			
			finder(arr[truth.get(i)]);
			}
	//	for(int i=0; i<N; i++) {
		//	System.out.print((arr[i])+" ");
		//}
		
		//System.out.println("\n말하면 안되는 사람 수"+(warning.size()));
		
		//warning에 거짓말 하면 안되는 사람들 다모음
		int lParty = M;
		for(int i=0; i<party.size(); i++) {
			Iterator<Integer> itr = party.get(i).iterator();
			while(itr.hasNext()) {
				int x =itr.next();
			
				if(warning.contains(x)) {
//			System.out.println("실행되었습니다.");	
					lParty--;
					break;
				}
			}
			
			
		}

		
		System.out.print(lParty);

	}

}
