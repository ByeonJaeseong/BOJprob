
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.TreeSet;


public class Main {
	public static int L;
	public static int C;
	public static char[] arr;
	public static boolean[] arr2;
	public static List<Character> list2;
	public static int counter = 0;
	public static int counter2 = 0;
	public static void bfs(int i) {
		if(!arr2[i]&&list2.size()<L&&i<C) {
			arr2[i]=true;
			list2.add(arr[i]);
			if(arr[i]=='a'||
					arr[i]=='e'||
					arr[i]=='i'||
					arr[i]=='o'||
					arr[i]=='u') {
				counter++;
			}else {
				counter2++;
			}
			for(int j=i+1; j<C; j++) {
				bfs(j);
			}
			if(list2.size()==L&&counter>0&&counter2>1) {
				for(int j=0; j<L; j++) {
					System.out.print(list2.get(j));
				}
				System.out.println();
			}
			arr2[i]=false;
			list2.remove((Character)arr[i]);
			if(arr[i]=='a'||
					arr[i]=='e'||
					arr[i]=='i'||
					arr[i]=='o'||
					arr[i]=='u') {
				counter--;
			}else {
				counter2--;
			}
		}
		
		
	}
	

	

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		String[] input = br.readLine().trim().split(" ");
		L=Integer.parseInt(input[0]);//몇자리 암호
		C=Integer.parseInt(input[1]);//사용되는 알파벳
		List<Character> list = new ArrayList<>();//알파벳 받아서 저장
		input = br.readLine().trim().split(" ");
		for(int i=0; i<C; i++) {
			list.add(input[i].charAt(0));
		}
		list.sort(null);
		list2 = new ArrayList<>();
		arr = new char[C];
		arr2= new boolean[C];
		for(int i=0; i<C; i++) {
			arr[i]=list.get(i);
		}
		for(int i=0; i<C-L+1; i++) {
			bfs(i);
		}
	}

}
